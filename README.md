# URL Extras Package

This package demonstrates how to use file URLs as extras dependencies in a Python package.

## Installation

Basic installation:

```bash
pip install .
```

With extras:

```bash
# Install with standard extras (regular packages)
pip install ".[standard]"

# Install with JSON data from URL
pip install ".[json_data]"

# Install with Git repository component
pip install ".[git_component]"

# Install with component from a monorepo
pip install ".[monorepo_component]"

# Install all extras
pip install ".[complete]"
```

```sh
pip uninstall -y json_data url_extras_package
```

## Usage

```python
from url_extras_package import core, utils

# Check what extras are installed
print(utils.list_installed_extras())

# Use JSON data (if the json_data extra is installed)
json_data = core.load_json_data()
print(json_data)

# Use Git component (if the git_component extra is installed)
result = core.use_git_component()
print(result)

# Use monorepo component (if installed)
result = core.use_monorepo_component()
print(result)
```

## Creating JSON Data Package

For the `json_data` extra to work, you need to create a simple Python package with your JSON data:

1. Create a directory structure:
```
json_data/
├── setup.py
└── json_data/
    └── data.json
```

2. Add this to setup.py:
```python
from setuptools import setup

setup(
    name="json_data",
    version="0.1.0",
    package_data={"json_data": ["*.json"]},
    packages=["json_data"]
)
```

3. Package it:
```bash
cd json_data
python -m build
```

4. Host the resulting .zip or .tar.gz file somewhere accessible via HTTP

## Extras Formats Supported

Pip supports several URL formats for dependencies:

- Wheel files (.whl)
- Source distributions (.tar.gz, .tgz)
- Zip archives (.zip)
- Other compressed tarballs (.tar.bz2, .tar.xz)
- Git repositories (git+https://...)
- Other VCS: Mercurial (hg+), Subversion (svn+), Bazaar (bzr+)
