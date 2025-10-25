---
title: Markdown Syntax Reference
---

# Markdown Syntax Reference

A comprehensive reference for Markdown syntax supported by this generator.

## Headings

```markdown
# H1 Heading
## H2 Heading
### H3 Heading
#### H4 Heading
##### H5 Heading
###### H6 Heading
```

## Emphasis

```markdown
*italic* or _italic_
**bold** or __bold__
***bold and italic***
~~strikethrough~~
```

## Lists

### Unordered Lists

```markdown
- Item 1
- Item 2
    - Nested item 2.1
    - Nested item 2.2
- Item 3
```

### Ordered Lists

```markdown
1. First item
2. Second item
3. Third item
```

## Links

```markdown
[Link text](https://example.com)
[Link with title](https://example.com "Link title")
```

## Images

```markdown
![Alt text](image.png)
![Alt text](image.png "Image title")
```

## Code

### Inline Code

```markdown
Use `inline code` for short snippets.
```

### Code Blocks

With syntax highlighting:

\`\`\`python
def hello_world():
    print("Hello, world!")
\`\`\`

\`\`\`javascript
const greeting = "Hello, world!";
console.log(greeting);
\`\`\`

## Tables

```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |
```

Result:

| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |

## Blockquotes

```markdown
> This is a blockquote.
> It can span multiple lines.
>
> > Nested blockquotes are also possible.
```

## Horizontal Rules

```markdown
---
***
___
```

## HTML

You can use inline HTML when needed:

```html
<div class="custom-class">
    <p>HTML content</p>
</div>
```

## Definition Lists

(Available through `markdown.extensions.extra`)

```markdown
Term 1
:   Definition 1

Term 2
:   Definition 2a
:   Definition 2b
```
