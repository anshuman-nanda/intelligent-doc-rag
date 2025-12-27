"""
Basic tests for RAGflow package structure.
"""

import ragflow


def test_package_import():
    """Test that the package can be imported."""
    assert ragflow is not None


def test_version_exists():
    """Test that version is defined."""
    assert hasattr(ragflow, "__version__")
    assert isinstance(ragflow.__version__, str)
    assert ragflow.__version__ == "0.1.0"


def test_author_metadata():
    """Test that author metadata is defined."""
    assert hasattr(ragflow, "__author__")
    assert hasattr(ragflow, "__email__")
