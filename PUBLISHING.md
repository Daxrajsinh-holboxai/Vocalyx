# Publishing Vocalyx to PyPI

This guide covers releasing `vocalyx` to TestPyPI (for testing) and then to PyPI (production).

## Prerequisites

1. **Create accounts** (if you don't have them):
   - [TestPyPI](https://test.pypi.org/account/register/)
   - [PyPI](https://pypi.org/account/register/)

2. **Install build tools**:
   ```bash
   pip install build twine
   ```

## Step 1: Test on TestPyPI

### Build the package

```bash
cd /path/to/Vocalyx
python -m build
```

This creates `dist/vocalyx-1.0.0.tar.gz` and `dist/vocalyx-1.0.0-py3-none-any.whl`.

### Upload to TestPyPI

```bash
twine upload --repository testpypi dist/*
```

When prompted:
- **Username**: your TestPyPI username (or use `__token__`)
- **Password**: your TestPyPI API token (create at https://test.pypi.org/manage/account/token/)

### Install from TestPyPI

```bash
pip install --index-url https://test.pypi.org/simple/ vocalyx
```

### Verify installation

```bash
vocalyx --help
vocalyx-tts --help
vocalyx-stt --help
```

## Step 2: Publish to PyPI (Production)

Once you've verified the package works on TestPyPI:

### Upload to PyPI

```bash
twine upload dist/*
```

- **Username**: `__token__`
- **Password**: your PyPI API token (create at https://pypi.org/manage/account/token/)

### Install from PyPI

```bash
pip install vocalyx
```

## Version Bumping

Before each release, update the version in:
1. `pyproject.toml` - `version = "X.Y.Z"`
2. `vocalyx/__init__.py` - `__version__ = "X.Y.Z"`

## Environment Variables (API Keys)

Users need to create a `.env` file with:
```
OPENAI_API_KEY=your_openai_api_key_here
```

The TTS server requires this for GPT streaming.
