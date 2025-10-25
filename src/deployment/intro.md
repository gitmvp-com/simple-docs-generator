---
title: Deployment
---

# Deployment

Deploy your documentation to make it accessible online.

## What You're Deploying

After running `python build.py`, the `build/` directory contains:

- Static HTML files
- No server-side processing needed
- No database required
- Fast loading times

This makes deployment simple and hosting cheap (or free).

## Deployment Options

### GitHub Pages

1. **Create a `gh-pages` branch**:
   ```bash
   git checkout -b gh-pages
   ```

2. **Copy build files to root**:
   ```bash
   cp -r build/* .
   git add .
   git commit -m "Deploy documentation"
   git push origin gh-pages
   ```

3. **Enable GitHub Pages** in repository settings

Your docs will be at: `https://username.github.io/repo-name/`

### Netlify

1. **Create a `netlify.toml`** file:
   ```toml
   [build]
     command = "python build.py"
     publish = "build"
   ```

2. **Connect your repository** to Netlify
3. **Deploy** - Netlify will automatically build and deploy

### Vercel

1. **Install Vercel CLI**:
   ```bash
   npm i -g vercel
   ```

2. **Deploy**:
   ```bash
   python build.py
   vercel build/
   ```

### Traditional Web Hosting

1. **Build locally**:
   ```bash
   python build.py
   ```

2. **Upload via FTP/SFTP**:
   - Upload the contents of `build/` to your web server
   - Point your domain to the upload directory

### AWS S3

1. **Build locally**:
   ```bash
   python build.py
   ```

2. **Sync to S3**:
   ```bash
   aws s3 sync build/ s3://your-bucket-name/
   ```

3. **Enable static website hosting** in S3 bucket settings

## Custom Domain

Most hosting providers support custom domains:

- **GitHub Pages**: Add a `CNAME` file
- **Netlify**: Configure in dashboard
- **Vercel**: Configure in dashboard
- **S3**: Use Route 53 or CloudFront

## Continuous Deployment

Automate deployments when you push changes:

- **GitHub Actions**: Build and deploy on push
- **Netlify**: Auto-deploy on git push
- **Vercel**: Auto-deploy on git push

### Example GitHub Action

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy Documentation

on:
  push:
    branches: [main]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - run: pip install -r requirements.txt
      - run: python build.py
      - uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./build
```

## Performance Tips

- Use a CDN for faster global access
- Enable compression (gzip/brotli)
- Set proper cache headers
- Optimize images before adding to docs

## Next Steps

Your documentation is now live! Consider:

- Adding analytics to track usage
- Setting up redirects for old URLs
- Implementing search functionality
- Adding a feedback widget
