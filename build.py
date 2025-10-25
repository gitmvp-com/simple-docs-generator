#!/usr/bin/env python3
"""Documentation Builder

Builds HTML documentation from Markdown files based on toc.yml structure.
Matches the Markdown processing approach from OutSystems/docs-odc.
"""

import os
import sys
import yaml
import markdown
from pathlib import Path
import shutil

# Configuration
INPUT_FOLDER = "src"
OUTPUT_FOLDER = "build"
TOC_FILE = "toc.yml"
TEMPLATE_FILE = "templates/default.html"

# Markdown extensions matching the parent project
MARKDOWN_EXTENSIONS = [
    'markdown.extensions.extra',      # Meta-extension (tables, def lists, etc.)
    'markdown.extensions.meta',       # Front-matter metadata
    'markdown.extensions.toc',        # Table of contents with bookmarks
    'markdown.extensions.fenced_code',# Fenced code blocks
    'markdown.extensions.codehilite', # Syntax highlighting
]


class DocBuilder:
    """Documentation builder class"""
    
    def __init__(self):
        self.md = markdown.Markdown(extensions=MARKDOWN_EXTENSIONS)
        self.template = self.load_template()
        self.toc = self.load_toc()
        
    def load_template(self):
        """Load HTML template"""
        try:
            with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Warning: Template file {TEMPLATE_FILE} not found. Using basic template.")
            return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif; line-height: 1.6; max-width: 900px; margin: 0 auto; padding: 20px; color: #333; }}
        h1, h2, h3, h4, h5, h6 {{ margin-top: 1.5em; margin-bottom: 0.5em; font-weight: 600; }}
        h1 {{ border-bottom: 2px solid #eee; padding-bottom: 0.3em; }}
        code {{ background: #f4f4f4; padding: 2px 6px; border-radius: 3px; font-size: 0.9em; }}
        pre {{ background: #f4f4f4; padding: 16px; border-radius: 6px; overflow-x: auto; }}
        pre code {{ background: none; padding: 0; }}
        a {{ color: #0366d6; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        blockquote {{ border-left: 4px solid #ddd; margin: 0; padding-left: 16px; color: #666; }}
        table {{ border-collapse: collapse; width: 100%; margin: 1em 0; }}
        th, td {{ border: 1px solid #ddd; padding: 8px 12px; text-align: left; }}
        th {{ background-color: #f4f4f4; font-weight: 600; }}
        img {{ max-width: 100%; height: auto; }}
    </style>
</head>
<body>
    <nav><a href="index.html">← Back to Home</a></nav>
    <main>{content}</main>
</body>
</html>"""
    
    def load_toc(self):
        """Load table of contents from YAML"""
        try:
            with open(TOC_FILE, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f) or []
        except FileNotFoundError:
            print(f"Error: {TOC_FILE} not found!")
            sys.exit(1)
        except yaml.YAMLError as e:
            print(f"Error parsing {TOC_FILE}: {e}")
            sys.exit(1)
    
    def extract_files_from_toc(self, items=None):
        """Recursively extract all markdown files from TOC"""
        if items is None:
            items = self.toc
        
        files = []
        for item in items:
            if isinstance(item, dict):
                if 'href' in item:
                    files.append(item['href'])
                if 'topics' in item:
                    files.extend(self.extract_files_from_toc(item['topics']))
        return files
    
    def convert_markdown_to_html(self, md_path):
        """Convert a Markdown file to HTML"""
        input_path = Path(INPUT_FOLDER) / md_path
        
        if not input_path.exists():
            print(f"Warning: {input_path} not found, skipping...")
            return None
        
        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                md_content = f.read()
            
            # Reset Markdown instance for each file
            self.md.reset()
            html_content = self.md.convert(md_content)
            
            # Extract metadata if available
            title = self.md.Meta.get('title', [md_path])[0] if hasattr(self.md, 'Meta') and self.md.Meta else md_path
            
            # Generate final HTML from template
            final_html = self.template.format(
                title=title,
                content=html_content
            )
            
            return final_html
            
        except Exception as e:
            print(f"Error converting {md_path}: {e}")
            return None
    
    def build(self):
        """Build all documentation files"""
        print("Starting documentation build...")
        
        # Clean and create output folder
        output_path = Path(OUTPUT_FOLDER)
        if output_path.exists():
            shutil.rmtree(output_path)
        output_path.mkdir(parents=True)
        
        # Extract all files from TOC
        files = self.extract_files_from_toc()
        print(f"Found {len(files)} files in table of contents")
        
        # Convert each file
        built_count = 0
        for md_file in files:
            html = self.convert_markdown_to_html(md_file)
            if html:
                # Create output path
                output_file = output_path / md_file.replace('.md', '.html')
                output_file.parent.mkdir(parents=True, exist_ok=True)
                
                # Write HTML file
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(html)
                
                built_count += 1
                print(f"✓ Built: {md_file} -> {output_file}")
        
        # Create index page
        self.create_index()
        
        print(f"\n✅ Build complete! {built_count} files generated in {OUTPUT_FOLDER}/")
        print(f"Run 'python serve.py' to preview your documentation")
    
    def create_index(self):
        """Create an index.html with TOC navigation"""
        def render_toc_items(items, level=0):
            html = '<ul>' if level > 0 else '<ul style="list-style: none; padding-left: 0;">'
            for item in items:
                if isinstance(item, dict):
                    if 'href' in item:
                        href = item['href'].replace('.md', '.html')
                        title = item.get('title', item['href'].split('/')[-1].replace('.md', '').replace('-', ' ').title())
                        html += f'<li><a href="{href}">{title}</a>'
                        if 'topics' in item:
                            html += render_toc_items(item['topics'], level + 1)
                        html += '</li>'
            html += '</ul>'
            return html
        
        toc_html = render_toc_items(self.toc)
        
        index_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Documentation</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif; line-height: 1.6; max-width: 900px; margin: 0 auto; padding: 20px; color: #333; }}
        h1 {{ border-bottom: 2px solid #eee; padding-bottom: 0.3em; }}
        ul {{ line-height: 1.8; }}
        a {{ color: #0366d6; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        li {{ margin: 8px 0; }}
    </style>
</head>
<body>
    <h1>📚 Documentation</h1>
    <p>Welcome to the documentation. Browse the topics below:</p>
    {toc_html}
</body>
</html>"""
        
        index_path = Path(OUTPUT_FOLDER) / 'index.html'
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)
        
        print(f"✓ Created index.html")


if __name__ == '__main__':
    builder = DocBuilder()
    builder.build()
