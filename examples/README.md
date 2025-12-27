# RAGflow Examples

This directory contains example scripts and applications demonstrating RAGflow usage.

## Examples

### 1. Demo Server (`server.py`)

A FastAPI-based demo server showing how to use RAGflow in a web service.

**Run the server:**
```bash
python examples/server.py
# or
uvicorn examples.server:app --reload
```

**Access the API:**
- API Documentation: http://localhost:8000/docs
- Root endpoint: http://localhost:8000/
- Health check: http://localhost:8000/health

### 2. CLI Example (`cli.py`)

Command-line interface examples for RAGflow operations.

**Usage:**
```bash
# Index documents
python examples/cli.py index --input ./documents --output ./index

# Query documents (interactive)
python examples/cli.py query --index ./index --interactive

# Query documents (single question)
python examples/cli.py query --index ./index --question "What is the main topic?"

# Batch processing
python examples/cli.py batch --index ./index --input queries.txt --output results.json
```

## Adding Your Own Examples

Feel free to contribute additional examples! When adding examples:

1. Create a new Python file in this directory
2. Add clear documentation and usage instructions
3. Include error handling and helpful messages
4. Update this README with your example
5. Test thoroughly before submitting a PR

## Requirements

All examples require the RAGflow package to be installed:

```bash
pip install -e .
```

Or with all dependencies:

```bash
pip install -e ".[dev]"
```
