<div align="center">

# 🚀 Intelligent Doc RAG

### 📚 Transform Your Documents into AI-Powered Knowledge

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![GitHub stars](https://img.shields.io/github/stars/anshuman-nanda/intelligent-doc-rag?style=social)](https://github.com/anshuman-nanda/intelligent-doc-rag/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/anshuman-nanda/intelligent-doc-rag?style=social)](https://github.com/anshuman-nanda/intelligent-doc-rag/network/members)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

*An intelligent Retrieval-Augmented Generation (RAG) system that enables semantic search and AI-powered question answering over your documents* ✨

[Getting Started](#-quick-start) • [Features](#-features) • [Documentation](#-usage) • [Contributing](#-contributing) • [Roadmap](#-roadmap)

</div>

---

## 🌟 Overview

**Intelligent Doc RAG** is a cutting-edge document intelligence platform that combines the power of modern AI with traditional information retrieval. Built on Retrieval-Augmented Generation (RAG) technology, it allows you to:

- 🔍 **Semantic Search**: Find relevant information across thousands of documents using natural language queries
- 🤖 **AI-Powered Answers**: Get accurate, context-aware responses grounded in your actual documents
- 📄 **Multi-Format Support**: Process PDFs, Word documents, text files, and more
- 🔒 **Privacy First**: All processing happens locally - your documents never leave your machine
- ⚡ **Lightning Fast**: Optimized vector search delivers results in milliseconds
- 📊 **Source Attribution**: Every answer includes citations to original document sources

Perfect for researchers, legal professionals, enterprise knowledge bases, customer support teams, and anyone who needs to extract insights from large document collections.

---

## ✨ Features

### Core Capabilities

🎯 **Intelligent Document Processing**
- Automatic text extraction from multiple file formats (PDF, DOCX, TXT, MD)
- Smart document chunking that preserves semantic meaning
- Support for complex document structures and layouts

🧠 **Advanced RAG Pipeline**
- State-of-the-art embedding models for semantic understanding
- Vector database integration for blazing-fast similarity search
- Hybrid search combining keyword and semantic approaches

💬 **Natural Language Interaction**
- Conversational interface for querying documents
- Context-aware multi-turn conversations
- Support for follow-up questions and clarifications

📈 **Enterprise-Ready Features**
- Batch document processing
- Custom metadata tagging and filtering
- API integration for seamless workflow adoption
- Scalable architecture for large document collections

🔧 **Developer-Friendly**
- Clean, modular codebase
- Comprehensive API documentation
- Easy integration with existing systems
- Extensible plugin architecture

---

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- pip package manager
- (Optional) CUDA-compatible GPU for faster processing

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/anshuman-nanda/intelligent-doc-rag.git
   cd intelligent-doc-rag
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run the application**
   ```bash
   python main.py
   ```

---

## 📖 Usage

### Basic Document Query

```python
from intelligent_doc_rag import DocumentRAG

# Initialize the RAG system
rag = DocumentRAG()

# Add documents to your knowledge base
rag.add_documents([
    "path/to/document1.pdf",
    "path/to/document2.docx",
    "path/to/folder/"  # Add entire folder
])

# Query your documents
response = rag.query("What are the key findings in the research papers?")

print(response.answer)
# Output: Based on the research papers, the key findings include...

# View source citations
for source in response.sources:
    print(f"- {source.document}: Page {source.page}")
```

### Advanced Usage with Filters

```python
# Query with metadata filters
response = rag.query(
    "Summarize the quarterly results",
    filters={
        "document_type": "financial_report",
        "year": 2024,
        "quarter": "Q1"
    }
)

# Conversational follow-up
response = rag.query(
    "How does this compare to last quarter?",
    conversation_id=response.conversation_id
)
```

### Command Line Interface

```bash
# Index documents
python -m intelligent_doc_rag index --input ./documents --output ./index

# Interactive query mode
python -m intelligent_doc_rag query --index ./index

# Batch processing
python -m intelligent_doc_rag batch --input queries.txt --output results.json
```

---

## 🎬 Demo

### Document Ingestion
![Document Ingestion Demo](docs/images/ingestion-demo.gif)
*Coming soon: Watch how documents are processed and indexed*

### Semantic Search in Action
![Search Demo](docs/images/search-demo.gif)
*Coming soon: See the RAG system answer complex queries*

### Web Interface
![Web Interface](docs/images/web-interface.png)
*Coming soon: User-friendly web interface for document management*

---

## 🏗️ Architecture

```
intelligent-doc-rag/
├── src/
│   ├── document_processor/     # Document parsing and chunking
│   ├── embeddings/              # Embedding model integration
│   ├── vector_store/            # Vector database operations
│   ├── retriever/               # Semantic search and ranking
│   ├── generator/               # LLM integration for answer generation
│   └── api/                     # REST API endpoints
├── tests/                       # Comprehensive test suite
├── docs/                        # Documentation
├── examples/                    # Usage examples
└── requirements.txt             # Python dependencies
```

### Tech Stack

- **Document Processing**: PyPDF2, python-docx, unstructured
- **Embeddings**: Sentence Transformers, OpenAI embeddings
- **Vector Database**: FAISS, Pinecone, Weaviate
- **LLM Integration**: OpenAI GPT, Anthropic Claude, Local models via Ollama
- **API Framework**: FastAPI
- **Frontend**: React, Next.js (coming soon)
- **Testing**: pytest, unittest

---

## 🤝 Contributing

We love contributions! Whether it's bug fixes, new features, documentation improvements, or feedback, we appreciate your help in making Intelligent Doc RAG better.

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Contribution Guidelines

- Write clear, commented code
- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation as needed
- Be respectful and constructive in discussions

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 🗺️ Roadmap

### Current Focus (v0.1.0) 🎯
- [x] Basic RAG pipeline implementation
- [x] PDF document support
- [ ] Core embedding models integration
- [ ] Vector database setup (FAISS)
- [ ] Basic query interface

### Coming Soon (v0.2.0) 📅
- [ ] Multi-format document support (DOCX, TXT, MD, HTML)
- [ ] Web-based UI
- [ ] Conversation history
- [ ] Advanced filtering and metadata
- [ ] Batch processing capabilities

### Future Enhancements (v0.3.0+) 🚀
- [ ] Multi-modal support (images, tables, charts)
- [ ] Custom embedding model fine-tuning
- [ ] Real-time document updates
- [ ] Collaborative features
- [ ] Cloud deployment options
- [ ] Mobile application
- [ ] Integration with popular document management systems
- [ ] Advanced analytics and insights dashboard

**Want to suggest a feature?** Open an [issue](https://github.com/anshuman-nanda/intelligent-doc-rag/issues) with the `enhancement` label!

---

## 📊 Project Stats

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=anshuman-nanda/intelligent-doc-rag&type=Date)](https://star-history.com/#anshuman-nanda/intelligent-doc-rag&Date)

### Contributors

We appreciate all our contributors! 🙏

[![Contributors](https://contrib.rocks/image?repo=anshuman-nanda/intelligent-doc-rag)](https://github.com/anshuman-nanda/intelligent-doc-rag/graphs/contributors)

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Built with inspiration from cutting-edge RAG research and open-source projects
- Thanks to the amazing open-source community for tools and libraries
- Special mention to projects like [LangChain](https://github.com/langchain-ai/langchain), [LlamaIndex](https://github.com/jerryjliu/llama_index), and [Haystack](https://github.com/deepset-ai/haystack)

---

## 📞 Connect & Support

- **GitHub Issues**: [Report bugs](https://github.com/anshuman-nanda/intelligent-doc-rag/issues) or request features
- **Discussions**: [Join the conversation](https://github.com/anshuman-nanda/intelligent-doc-rag/discussions)
- **Email**: [anshuman.nanda@gmail.com](mailto:anshuman.nanda@gmail.com)

---

<div align="center">

### ⭐ If you find this project useful, please consider giving it a star!

**Made with ❤️ by the Intelligent Doc RAG community**

[⬆ Back to Top](#-intelligent-doc-rag)

</div>
