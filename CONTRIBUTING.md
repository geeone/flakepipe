
# Contributing to Flakepipe

Thanks for your interest in contributing!

## 🛠️ How to contribute

- Submit bug reports or feature requests as GitHub issues
- Fork the repo and submit pull requests
- Follow PEP8 and keep code modular
- Add test coverage where possible

## 📦 Install for development

```bash
pip install -r requirements.txt
pip install -e .
```

## 🎯 Running Tests \w CodeCov

This project uses `pytest` with `pytest-cov` to run unit tests and measure coverage.

### 1. Install development dependencies

```bash
pip install -r requirements-dev.txt
```

### 2. Run tests with coverage report

To run all tests and display a coverage summary in the terminal:

```bash
pytest --cov=flakepipe tests/
```

Moreover, you can generate a detailed HTML report:

```bash
pytest --cov=flakepipe --cov-report=term-missing --cov-report=html tests/
```

> 📁 The HTML report will be available in the `htmlcov/` directory.
