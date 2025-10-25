---
title: Markdown Extensions
---

# Markdown Extensions

This documentation generator uses Python-Markdown with several extensions enabled.

## Enabled Extensions

The following extensions match those used in the parent OutSystems/docs-odc project:

### 1. Extra Extension

`markdown.extensions.extra` is a meta-extension that enables:

- **Tables** - GitHub-flavored tables
- **Fenced Code Blocks** - Triple-backtick code blocks
- **Definition Lists** - Key-value term definitions
- **Footnotes** - Reference-style footnotes
- **Abbreviations** - Expandable abbreviations
- **Attribute Lists** - Add CSS classes to elements

### 2. Meta Extension

`markdown.extensions.meta` allows front-matter metadata:

```markdown
---
title: Page Title
author: John Doe
date: 2024-01-15
---

# Page Content
```

The metadata is parsed but not displayed in the output. It's used for the HTML `<title>` tag.

### 3. TOC Extension

`markdown.extensions.toc` generates:

- Automatic heading IDs for anchor links
- Bookmarkable URLs for each section

Example: A heading `## Installation` becomes `<h2 id="installation">Installation</h2>`

You can link directly: `page.html#installation`

### 4. Fenced Code Extension

`markdown.extensions.fenced_code` enables GitHub-style code blocks:

\`\`\`python
def example():
    return "Hello"
\`\`\`

### 5. CodeHilite Extension

`markdown.extensions.codehilite` adds syntax highlighting support.

## Tables Example

Tables are fully supported:

```markdown
| Feature | Supported | Notes |
|---------|-----------|-------|
| Tables  | ✓         | Via extra extension |
| Code    | ✓         | Syntax highlighting |
| Images  | ✓         | Standard Markdown |
```

Result:

| Feature | Supported | Notes |
|---------|-----------|-------|
| Tables  | ✓         | Via extra extension |
| Code    | ✓         | Syntax highlighting |
| Images  | ✓         | Standard Markdown |

## Definition Lists Example

```markdown
Markdown
:   A lightweight markup language for creating formatted text

Python-Markdown
:   A Python implementation of the Markdown parser
```

## Footnotes Example

```markdown
Here's a sentence with a footnote[^1].

[^1]: This is the footnote content.
```

## Adding More Extensions

To add more extensions, edit `build.py` and update the `MARKDOWN_EXTENSIONS` list:

```python
MARKDOWN_EXTENSIONS = [
    'markdown.extensions.extra',
    'markdown.extensions.meta',
    'markdown.extensions.toc',
    'markdown.extensions.fenced_code',
    'markdown.extensions.codehilite',
    # Add your extension here
    'markdown.extensions.sane_lists',
]
```

See the [Python-Markdown documentation](https://python-markdown.github.io/extensions/) for available extensions.
