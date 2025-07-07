
# Flakepipe

[![PyPI](https://img.shields.io/pypi/v/flakepipe)](https://pypi.org/project/flakepipe/)
[![Python](https://img.shields.io/badge/Python-3.8%20|%203.9%20|%203.10%20|%203.11-blue)](https://pypi.org/project/flakepipe/)
[![License](https://img.shields.io/github/license/geeone/flakepipe)](LICENSE)
[![Build Status](https://github.com/geeone/flakepipe/actions/workflows/build.yml/badge.svg)](https://github.com/geeone/flakepipe/actions/workflows/build.yml)
[![Codecov](https://codecov.io/gh/geeone/flakepipe/branch/main/graph/badge.svg)](https://codecov.io/gh/geeone/flakepipe)

**Flakepipe** is a lightweight, reusable Python module for uploading datasets to **Snowflake** via secure staging.

It automates table creation, column normalization, and data ingestion using Snowflake’s `PUT` and `COPY INTO` commands – making it ideal for ETL pipelines, scraping workflows, and reproducible data transfers.

---

## 📦 Features

- Upload CSV files to Snowflake via `PUT` and `COPY INTO`
- Automatically create or truncate target tables
- Normalize column names to be Snowflake-compatible
- Support for prefix/postfix-based table naming
- Modular, testable, and production-friendly design

---

## ⚙️ Installation

### Supported Python Versions

Flakepipe supports **Python ≥ 3.8**, and **< 3.12**.

### Installing Flakepipe

To install globally via PyPI (recommended):

```bash
pip install flakepipe
```

To install locally from source (for development), use editable mode:

```bash
git clone https://github.com/geeone/flakepipe.git
cd flakepipe
pip install -e .
```

Alternatively, you can install only the dependencies (without installing the package itself):

```bash
pip install -r requirements.txt
```

> 💡 See the [Dependencies](#-dependencies) section for version details.

---

## 🧩 Configuration

You must provide a config dictionary with Snowflake connection parameters:

```python
config = {
    'SF_USER': 'your_user',
    'SF_PASSWORD': 'your_password',
    'SF_ACCOUNT': 'your_account',
    'SF_ROLE': 'your_role',
    'SF_DATABASE': 'your_database',
    'SF_WAREHOUSE': 'your_warehouse',
}
```

---

## 🚀 Usage

### Upload a CSV file

```python
from flakepipe.uploader import upload_csv_to_snowflake
from your_project.config import config

upload_csv_to_snowflake(
    config=config,
    file_path='output.csv',
    schema='MY_SCHEMA',
    table_name='my_table',
    truncate=True,
    overwrite=False,
    prefix='daily',
    postfix='20250705'
)
```

### Truncate a table manually

```python
from flakepipe.uploader import truncate_table
from flakepipe.connection import get_engine

engine = get_engine(config, schema='MY_SCHEMA')
truncate_table(engine, 'MY_TABLE')
engine.dispose()
```

---

## 🛠 Dependencies

Listed in `requirements.txt`, including:

- SQLAlchemy >= 1.4.15
- snowflake-connector-python >= 2.8.1
- snowflake-sqlalchemy >= 1.2.4
- pandas >= 1.4.0, < 2.1
- numpy>=1.21.0, <1.26.0

> ✅ Tested with pandas 1.4.x to 1.5.x  
> ⚠️ Compatibility with pandas 2.x is expected but not officially guaranteed

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions, suggestions, and issues are welcome!  
Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 🌍 Why Flakepipe?

Flakepipe was born from repeated use in real-world data workflows, especially in scraping and ETL projects.  
Instead of rewriting boilerplate Snowflake ingestion code, this tool wraps best practices into a portable, documented, and open solution – freely available under an MIT license.

Whether you’re building one-off scripts or production pipelines – Flakepipe helps you do it right.
