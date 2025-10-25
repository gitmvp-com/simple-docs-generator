---
title: Writing Documentation
---

# Writing Documentation

Learn how to write effective documentation using Markdown.

## Basic Markdown Syntax

### Headings

Use `#` for headings:

```markdown
# Heading 1
## Heading 2
### Heading 3
```

### Text Formatting

```markdown
**Bold text**
*Italic text*
~~Strikethrough~~
```

### Lists

Unordered lists:

```markdown
- Item 1
- Item 2
    - Nested item
```

Ordered lists:

```markdown
1. First item
2. Second item
3. Third item
```

### Links and Images

```markdown
[Link text](https://example.com)
![Image alt text](image.png)
```

### Code

Inline code: \`code here\`

Code blocks:

\`\`\`python
def hello():
    print("Hello, world!")
\`\`\`

## Front Matter

Add metadata to your pages:

```markdown
---
title: Page Title
description: Page description
---

# Page content starts here
```

The `title` field is used in the HTML `<title>` tag.

## Editor Settings

For consistent formatting, configure your editor:

- **Indentation**: 4 spaces (not tabs)
- **Line endings**: Unix (LF)
- **Encoding**: UTF-8

The included `.editorconfig` file will configure this automatically in supported editors like VS Code, Sublime Text, and others.

## Best Practices

1. **Use descriptive headings** - Help readers scan content
2. **Keep paragraphs short** - Easier to read
3. **Add code examples** - Show, don't just tell
4. **Link related topics** - Help readers navigate
5. **Use lists** - Break down complex information

## Advanced Features

For advanced Markdown features, see [Markdown Extensions](../building/extensions.md).
