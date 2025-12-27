# Intelligent Document RAG

A Retrieval-Augmented Generation (RAG) system for intelligent document question-answering.

## Topics

This repository is tagged with the following topics for discoverability:

- `rag` - Retrieval-Augmented Generation
- `document-qa` - Document Question-Answering
- `ai` - Artificial Intelligence
- `fastapi` - FastAPI web framework
- `chatbot` - Conversational AI interface
- `natural-language-processing` - NLP techniques
- `pdf-parser` - PDF document processing
- `langchain` - LangChain framework
- `python` - Python programming language
- `machine-learning` - Machine Learning

## Managing Topics

### Automatic Updates

Topics are automatically applied when changes are pushed to `.github/topics.json` via the GitHub Actions workflow.

### Manual Updates

To manually apply topics to the repository:

```bash
# Ensure you have GitHub CLI installed and authenticated
gh auth login

# Run the apply-topics script
.github/scripts/apply-topics.sh
```

### Modifying Topics

To add or remove topics, edit `.github/topics.json` and either:
1. Push the changes to the main branch (triggers automatic update), or
2. Run the manual update script

## License

See [LICENSE](LICENSE) file for details.
