# Contributing to RAGflow

First off, thank you for considering contributing to RAGflow! 🎉 It's people like you that make this project such a great tool for the community.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Guidelines](#coding-guidelines)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)
- [Community](#community)

## Code of Conduct

This project and everyone participating in it is governed by our commitment to creating a welcoming and inclusive environment. By participating, you are expected to uphold this commitment.

### Our Standards

- **Be respectful** and considerate in your communication
- **Be collaborative** and open to feedback
- **Be patient** with newcomers and those learning
- **Focus on what is best** for the community and project

## Getting Started

### Prerequisites

Before you begin, ensure you have:

- Python 3.9 or higher installed
- Git for version control
- A GitHub account
- Familiarity with RAG systems and NLP (helpful but not required!)

### First-Time Contributors

If you're new to open source, welcome! Here are some resources:

- [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [Understanding the GitHub Flow](https://docs.github.com/en/get-started/quickstart/github-flow)

**Good First Issues**: Look for issues labeled `good-first-issue` or `beginner-friendly` to get started.

## How Can I Contribute?

### 🐛 Reporting Bugs

Before creating a bug report, please check existing issues to avoid duplicates.

**When submitting a bug report, include:**

- **Clear title and description** of the issue
- **Steps to reproduce** the problem
- **Expected behavior** vs. actual behavior
- **Screenshots** if applicable
- **Environment details** (OS, Python version, dependency versions)
- **Error messages or logs**

### ✨ Suggesting Enhancements

Enhancement suggestions are welcome! When suggesting an enhancement:

- **Use a clear and descriptive title**
- **Provide a detailed description** of the proposed feature
- **Explain why this enhancement would be useful** to most users
- **List any alternatives** you've considered
- **Include mockups or examples** if applicable

### 📝 Improving Documentation

Documentation improvements are always appreciated:

- Fix typos, grammar, or unclear explanations
- Add missing documentation for features
- Improve code examples
- Translate documentation (if applicable)

### 💻 Contributing Code

#### Types of Code Contributions

- **Bug fixes**: Squash those bugs! 🐛
- **New features**: Add exciting new capabilities
- **Performance improvements**: Make it faster!
- **Refactoring**: Clean up and improve code quality
- **Tests**: Improve test coverage

## Development Setup

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR-USERNAME/RAGflow.git
cd RAGflow

# Add upstream remote
git remote add upstream https://github.com/anshuman-nanda/RAGflow.git
```

### 2. Create Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Development dependencies
```

### 3. Create a Branch

```bash
# Update your local main branch
git checkout main
git pull upstream main

# Create a new feature branch
git checkout -b feature/your-feature-name
# or for bug fixes
git checkout -b fix/bug-description
```

### 4. Make Your Changes

Write your code, add tests, and update documentation as needed.

### 5. Run Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=ragflow tests/

# Run specific test file
pytest tests/test_document_processor.py
```

### 6. Lint Your Code

```bash
# Format code with Black
black ragflow/ tests/

# Check with flake8
flake8 ragflow/ tests/

# Type checking with mypy
mypy ragflow/
```

## Coding Guidelines

### Python Style Guide

We follow [PEP 8](https://peps.python.org/pep-0008/) with some modifications:

- **Line length**: Maximum 100 characters (not 79)
- **Imports**: Group and sort imports (use `isort`)
- **Docstrings**: Use Google-style docstrings
- **Type hints**: Use type hints for function signatures

### Example Code Style

```python
from typing import List, Dict, Optional

def process_document(
    file_path: str,
    chunk_size: int = 512,
    overlap: int = 50
) -> List[Dict[str, str]]:
    """
    Process a document and split it into chunks.

    Args:
        file_path: Path to the document file.
        chunk_size: Maximum size of each chunk in characters.
        overlap: Number of overlapping characters between chunks.

    Returns:
        A list of dictionaries containing chunk text and metadata.

    Raises:
        FileNotFoundError: If the file doesn't exist.
        ValueError: If chunk_size is less than overlap.
    """
    if chunk_size <= overlap:
        raise ValueError("chunk_size must be greater than overlap")
    
    # Implementation here
    chunks = []
    return chunks
```

### Testing Guidelines

- **Write tests** for all new features and bug fixes
- **Aim for high coverage**: Minimum 80% code coverage
- **Use descriptive test names**: `test_document_processor_handles_empty_file`
- **Follow AAA pattern**: Arrange, Act, Assert

```python
def test_chunk_document_with_overlap():
    # Arrange
    document = "This is a test document with some content."
    chunk_size = 10
    overlap = 2
    
    # Act
    chunks = chunk_document(document, chunk_size, overlap)
    
    # Assert
    assert len(chunks) > 1
    assert all(len(chunk) <= chunk_size for chunk in chunks)
```

## Commit Messages

Write clear, descriptive commit messages following these conventions:

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, no logic change)
- **refactor**: Code refactoring
- **test**: Adding or updating tests
- **chore**: Maintenance tasks

### Examples

```
feat(retriever): add hybrid search combining semantic and keyword search

Implemented a new hybrid search strategy that combines semantic 
similarity search with traditional keyword matching. This improves
retrieval accuracy by 15% on benchmark datasets.

Closes #123
```

```
fix(embeddings): handle empty document edge case

Fixed a bug where the embedding model would crash when processing
empty documents. Now returns an appropriate error message.

Fixes #456
```

## Pull Request Process

### Before Submitting

- [ ] Code follows project style guidelines
- [ ] Tests pass locally (`pytest`)
- [ ] New tests added for new features
- [ ] Documentation updated (README, docstrings, etc.)
- [ ] Commit messages follow conventions
- [ ] Branch is up to date with main

### Submitting

1. **Push your changes** to your fork
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a Pull Request** on GitHub
   - Use a clear title summarizing the changes
   - Fill out the PR template completely
   - Link related issues using keywords (Fixes #123, Closes #456)
   - Add screenshots for UI changes

3. **Address review feedback**
   - Be responsive to reviewer comments
   - Make requested changes promptly
   - Push updates to the same branch

### PR Review Process

- At least one maintainer review is required
- All CI checks must pass
- Code coverage should not decrease
- Documentation must be updated
- Maintainers may request changes or ask questions

### After Merge

- Delete your feature branch (optional but recommended)
- Update your local repository:
  ```bash
  git checkout main
  git pull upstream main
  ```

## Community

### Getting Help

- **GitHub Discussions**: Ask questions and share ideas
- **Issues**: Report bugs or request features
- **Email**: Contact maintainers directly for sensitive matters

### Recognition

All contributors are recognized in our README and release notes. Thank you for your contributions! 🙏

---

## Questions?

If you have questions about contributing, feel free to:

- Open an issue with the `question` label
- Start a discussion on GitHub Discussions
- Reach out to maintainers directly

---

**Thank you for contributing to RAGflow!** Every contribution, no matter how small, makes a difference. 🌟
