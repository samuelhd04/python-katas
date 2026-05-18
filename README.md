Three Python katas solved and tested with pytest, containerized with Docker, and automated with GitHub Actions.

## Run locally

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
pytest tests/ -v
```

## Run with Docker

```bash
docker build -t python-katas .
docker run python-katas
```

Every push to `main` automatically builds the Docker image and runs all tests via GitHub Actions.
