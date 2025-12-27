# Contributing to DocuChat

Thank you for your interest in contributing to DocuChat! We welcome contributions from the community and are excited to have you join us.

## 🤝 How to Contribute

### Reporting Bugs

If you find a bug, please create an issue on GitHub with:
- A clear, descriptive title
- Steps to reproduce the problem
- Expected behavior
- Actual behavior
- Your environment (OS, Python version, etc.)
- Screenshots if applicable

### Suggesting Features

We love new ideas! To suggest a feature:
- Check if the feature has already been suggested
- Create a new issue with a clear description
- Explain why this feature would be useful
- Provide examples of how it would work

### Code Contributions

1. **Fork the Repository**
   ```bash
   # Click the "Fork" button on GitHub
   git clone https://github.com/YOUR_USERNAME/DocuChat.git
   cd DocuChat
   ```

2. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes**
   - Write clear, readable code
   - Follow the existing code style
   - Add tests for new features
   - Update documentation as needed

4. **Test Your Changes**
   ```bash
   # Run tests
   pytest
   
   # Run linting
   ruff check .
   black --check .
   ```

5. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Add your descriptive commit message"
   ```

6. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request**
   - Go to the original DocuChat repository
   - Click "New Pull Request"
   - Select your fork and branch
   - Fill out the PR template with details

## 📝 Code Style

- Follow [PEP 8](https://pep8.org/) for Python code
- Use type hints where applicable
- Write docstrings for functions and classes
- Keep functions focused and concise
- Use meaningful variable names

## ✅ Pull Request Checklist

Before submitting a PR, ensure:
- [ ] Code follows the project's style guidelines
- [ ] Tests pass locally
- [ ] New tests added for new features
- [ ] Documentation updated
- [ ] Commit messages are clear and descriptive
- [ ] Branch is up to date with main

## 🧪 Testing

We use pytest for testing. To run tests:

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run all tests
pytest

# Run with coverage
pytest --cov=docuchat
```

## 📖 Documentation

When adding new features:
- Update the README.md if needed
- Add docstrings to new functions/classes
- Update or create relevant documentation files
- Include usage examples

## 💬 Communication

- **Issues** - For bug reports and feature requests
- **Discussions** - For questions and general discussion
- **Pull Requests** - For code contributions

## 🎯 Priority Areas

We're particularly interested in contributions for:
- Support for additional document formats
- Performance improvements
- UI/UX enhancements
- Documentation improvements
- Test coverage expansion

## 📜 Code of Conduct

Please note that this project follows a [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to uphold this code.

## ❓ Questions?

If you have questions about contributing:
- Check the [Wiki](https://github.com/anshuman-nanda/DocuChat/wiki)
- Ask in [Discussions](https://github.com/anshuman-nanda/DocuChat/discussions)
- Open an issue with the "question" label

## 🙏 Thank You!

Your contributions help make DocuChat better for everyone. We appreciate your time and effort!

---

Happy Contributing! 🚀
