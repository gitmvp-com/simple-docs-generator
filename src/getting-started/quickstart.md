---
title: Quick Start Guide
---

# Quick Start Guide

Get your documentation site up and running in minutes!

## Step 1: Create Your First Page

Create a new Markdown file in the `src/` directory:

```bash
mkdir -p src/my-docs
touch src/my-docs/hello.md
```

Add some content to `src/my-docs/hello.md`:

```markdown
---
title: Hello World
---

# Hello World

This is my first documentation page!

## Features

- Easy to write
- Clean HTML output
- Fast builds
```

## Step 2: Update the Table of Contents

Edit `toc.yml` to include your new page:

```yaml
# Getting Started
- href: getting-started/intro.md
- topics:
    - href: getting-started/installation.md
    - href: getting-started/quickstart.md

# My Docs
- href: my-docs/hello.md
```

## Step 3: Build the Documentation

Run the build script:

```bash
python build.py
```

You'll see output like:

```
Starting documentation build...
Found 4 files in table of contents
✓ Built: getting-started/intro.md -> build/getting-started/intro.html
✓ Built: my-docs/hello.md -> build/my-docs/hello.html
✓ Created index.html

✅ Build complete! 4 files generated in build/
```

## Step 4: Preview Locally

Start the local web server:

```bash
python serve.py
```

Open your browser to:

```
http://localhost:8000
```

You should see your documentation with a table of contents!

## Step 5: Deploy (Optional)

The `build/` directory contains static HTML files that can be deployed anywhere:

- **GitHub Pages**: Push the build folder to a `gh-pages` branch
- **Netlify**: Drag and drop the build folder
- **Vercel**: Deploy with `vercel build/`
- **Traditional hosting**: Upload via FTP/SFTP

## Next Steps

Learn more about:

- [Writing Documentation](writing-docs.md) - Markdown syntax and best practices
- [Markdown Extensions](../building/extensions.md) - Advanced features
