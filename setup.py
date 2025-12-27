"""
Setup script for RAGflow package.
"""

from setuptools import setup, find_packages
import os

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

# Read dev requirements
with open("requirements-dev.txt", "r", encoding="utf-8") as fh:
    dev_requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="ragflow",
    version="0.1.0",
    author="Anshuman Nanda",
    author_email="anshuman.nanda@gmail.com",
    description="A Python package for Retrieval-Augmented Generation over documents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anshuman-nanda/RAGflow",
    project_urls={
        "Bug Reports": "https://github.com/anshuman-nanda/RAGflow/issues",
        "Source": "https://github.com/anshuman-nanda/RAGflow",
        "Documentation": "https://github.com/anshuman-nanda/RAGflow/blob/main/README.md",
    },
    packages=find_packages(exclude=["tests", "tests.*", "examples", "examples.*", "docs"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    extras_require={
        "dev": dev_requirements,
        "gpu": [
            "faiss-gpu>=1.7.4",
        ],
    },
    entry_points={
        "console_scripts": [
            "ragflow=ragflow.cli:main",
        ],
    },
    keywords=[
        "rag",
        "retrieval-augmented-generation",
        "document-qa",
        "semantic-search",
        "nlp",
        "ai",
        "llm",
        "embeddings",
        "vector-database",
    ],
    include_package_data=True,
)
