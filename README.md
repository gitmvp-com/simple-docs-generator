# Simple Documentation Generator

A simplified MVP version of [OutSystems/docs-odc](https://github.com/OutSystems/docs-odc) - a static documentation site generator that converts Markdown files to HTML with YAML-based table of contents.

## Features

- **Markdown to HTML Conversion**: Converts Markdown files to HTML using Python-Markdown
- **YAML Table of Contents**: Organizes documentation with a simple YAML structure
- **Multiple Markdown Extensions**: Support for extra syntax, metadata, TOC, and more
- **Static Site Generation**: Build static HTML pages for easy deployment
- **Built-in Web Server**: Preview your documentation locally

## Installation

1. Clone the repository:
```bash
git clone https://github.com/gitmvp-com/simple-docs-generator.git
cd simple-docs-generator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Quick Start

1. **Add your Markdown files** to the `src/` directory

2. **Update the table of contents** in `toc.yml`:
```yaml
- href: getting-started/intro.md
- topics:
    - href: getting-started/installation.md
    - href: getting-started/quickstart.md
```

3. **Build the documentation**:
```bash
python build.py
```

4. **Preview locally**:
```bash
python serve.py
```

Open your browser to `http://localhost:8000`

## Project Structure

```
simple-docs-generator/
├── src/               # Markdown documentation files
│   └── getting-started/
│       ├── intro.md
│       └── installation.md
├── build/             # Generated HTML files (created after build)
├── templates/         # HTML templates
│   └── default.html
├── toc.yml            # Table of contents
├── build.py           # Build script
├── serve.py           # Local web server
└── requirements.txt   # Python dependencies
```

## Configuration

The generator supports the following Markdown extensions (matching the parent project):

- **markdown.extensions.extra** - Adds support for tables, definition lists, and more
- **markdown.extensions.meta** - Read metadata from Markdown front-matter
- **markdown.extensions.toc** - Generate table of contents with automatic bookmarks
- **markdown.extensions.fenced_code** - Code blocks with syntax highlighting

## Writing Documentation

All documentation should be written in standard Markdown syntax:

### Front Matter (Optional)

Add metadata to the top of your Markdown files:

```markdown
---
title: Getting Started
description: Learn how to get started
---

# Getting Started

Your content here...
```

### Editor Settings

For consistent formatting:
- Use **4 spaces** for indentation (not tabs)
- Use soft-wrapping to avoid carriage returns inside paragraphs

An `.editorconfig` file is included for automatic configuration in supported editors.

## Deployment

After building, deploy the `build/` directory to any static hosting service:

- GitHub Pages
- Netlify
- Vercel
- AWS S3
- Any web server

## Differences from Parent Project

This MVP simplifies the original OutSystems/docs-odc by:

- Removing complex build pipeline configurations
- Simplifying the YAML TOC structure
- Providing a basic HTML template instead of complex theming
- Including a simple local server for development
- Focusing on core Markdown rendering functionality

## License

MIT License - See LICENSE file for details

## Credits

Based on [OutSystems/docs-odc](https://github.com/OutSystems/docs-odc)
