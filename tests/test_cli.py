"""
Tests for RAGflow CLI module.
"""

import sys
from io import StringIO
from ragflow.cli import main


def test_cli_import():
    """Test that the CLI module can be imported."""
    from ragflow import cli
    assert cli is not None
    assert hasattr(cli, "main")


def test_cli_help(monkeypatch, capsys):
    """Test that the CLI help message works."""
    # Mock sys.argv to provide --help argument
    monkeypatch.setattr(sys, "argv", ["ragflow", "--help"])
    
    try:
        main()
    except SystemExit as e:
        # --help causes sys.exit(0)
        assert e.code == 0
    
    captured = capsys.readouterr()
    assert "RAGflow - Document Q&A CLI" in captured.out
    assert "index" in captured.out
    assert "query" in captured.out
    assert "batch" in captured.out


def test_cli_no_command(monkeypatch):
    """Test that the CLI exits when no command is provided."""
    # Mock sys.argv with no command
    monkeypatch.setattr(sys, "argv", ["ragflow"])
    
    try:
        main()
    except SystemExit as e:
        # No command should exit with code 1
        assert e.code == 1
