---
title: Building Documentation
---

# Building Documentation

Learn how to build and customize your documentation.

## Build Process

The build process converts your Markdown files to HTML:

1. **Read** the `toc.yml` table of contents
2. **Process** each Markdown file with Python-Markdown
3. **Apply** the HTML template
4. **Generate** static HTML files in `build/`
5. **Create** an index page with navigation

## Build Script

Run the build script:

```bash
python build.py
```

### What Happens During Build

- The `src/` directory is scanned for Markdown files
- Each file is converted to HTML
- The directory structure is preserved
- An `index.html` is generated with the table of contents

## Output Structure

After building, your `build/` directory mirrors your `src/` structure:

```
build/
├── index.html
├── getting-started/
│   ├── intro.html
│   ├── installation.html
│   └── quickstart.html
└── building/
    ├── intro.html
    └── extensions.html
```

## Markdown Processing

The builder uses the same Markdown extensions as the parent OutSystems/docs-odc project:

- `markdown.extensions.extra` - Tables, definition lists, and more
- `markdown.extensions.meta` - Front-matter metadata
- `markdown.extensions.toc` - Automatic heading anchors
- `markdown.extensions.fenced_code` - Code blocks with syntax

Learn more in [Markdown Extensions](extensions.md).

## Customization

You can customize:

- **Template**: Edit `templates/default.html`
- **Styles**: Modify the CSS in the template
- **Extensions**: Add more Markdown extensions in `build.py`
