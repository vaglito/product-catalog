# Product Catalog API

A modern and efficient API for managing product catalogs, built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**.

## 🚀 Technologies

- **Python:** >= 3.14
- **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (Standard)
- **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/) 2.0
- **Database:** PostgreSQL (via `psycopg2`)
- **Configuration Management:** `python-decouple`
- **Dependency Manager:** Poetry

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.14 or higher.
- Poetry.
- An active PostgreSQL instance.

## 🛠️ Installation and Configuration

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd product-catalog
   ```

2. **Install dependencies with Poetry:**
   ```bash
   poetry install
   ```

3. **Configure environment variables:**
   Create a `.env` file in the root of the project based on the following:
   ```env
   DATABASE_URL=postgresql://user:password@localhost:5432/db_name
   ```

## 🏃 Execution

To start the development server, use the standard FastAPI command:

```bash
poetry run fastapi dev
```

The API will be available at `http://127.0.0.1:8000` and you can access the interactive documentation in `/docs`.

## 📝 License
This project is authored by Cesar Gonzalez.