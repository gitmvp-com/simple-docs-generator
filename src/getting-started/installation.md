---
title: Installation
---

# Installation

Follow these steps to install and set up the Simple Documentation Generator.

## Prerequisites

You need Python 3.7 or later installed on your system.

Check your Python version:

```bash
python --version
```

or

```bash
python3 --version
```

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/gitmvp-com/simple-docs-generator.git
cd simple-docs-generator
```

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Or using pip3:

```bash
pip3 install -r requirements.txt
```

### 3. Verify Installation

Run the build script to verify everything is working:

```bash
python build.py
```

You should see output indicating that the documentation was built successfully.

## What's Installed?

The `requirements.txt` includes:

- **Markdown** - The core Markdown parser (version 3.4.0+)
- **PyYAML** - For parsing the table of contents (version 6.0+)

These match the dependencies used in the parent OutSystems/docs-odc project.

## Next Steps

Now that you have the tool installed, proceed to the [Quick Start](quickstart.md) guide to create your first documentation.
