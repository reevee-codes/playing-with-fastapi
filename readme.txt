# FastAPI Learning

Simple project created to learn FastAPI by building small API examples.

## Tech Stack

* Python 3.13
* FastAPI
* Uvicorn
* Pydantic
* Ruff

## Run

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload --host 127.0.0.1 --port 3000
```

API documentation:

* http://127.0.0.1:3000/docs
* http://127.0.0.1:3000/redoc

## Linting

```bash
ruff check . --fix
```

testy
pytest tests\test_main.py -v