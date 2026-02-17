# ML Service Operation Manual (RUNBOOK)

MLOps Course Module 3 Milestone 2 - Containerized ML Service Operation Manual

**Version**: v1.0.0

**Maintainer**: <jing han/jane872>

**Update Time**: <2.17.2026>

## 1. Dependency Fixing Strategy (Reproducibility)

### 1.1 Core Principles

- All Python dependencies **have a fixed specific version** (no `>=` or `<`) to avoid version compatibility issues;

- Separate **runtime dependencies** (app/requirements.txt) and **development/test dependencies** (manually installed locally, without entering the runtime image);

- All dependencies are installed from the official PyPI repository to ensure integrity.

### 1.2 Dependency Update Process

```bash

# After updating dependency versions locally, regenerate requirements.txt

pip freeze > app/requirements.txt

# Test dependency compatibility locally

pytest tests/test_app.py

# Rebuild the image and test

docker build -t ml-service:test . && docker run --rm ml-service:test