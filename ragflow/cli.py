"""
RAGflow CLI - Command line interface for RAGflow.

This module provides the CLI functionality for RAGflow.
"""

import argparse
import sys


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="RAGflow - Document Q&A CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Index documents
  ragflow index --input ./documents --output ./index
  
  # Query documents
  ragflow query --index ./index --question "What is the main topic?"
  
  # Batch processing
  ragflow batch --index ./index --input queries.txt --output results.json
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Index command
    index_parser = subparsers.add_parser("index", help="Index documents")
    index_parser.add_argument("--input", required=True, help="Input directory with documents")
    index_parser.add_argument("--output", required=True, help="Output directory for index")
    
    # Query command
    query_parser = subparsers.add_parser("query", help="Query indexed documents")
    query_parser.add_argument("--index", required=True, help="Index directory")
    query_parser.add_argument("--question", help="Question to ask")
    query_parser.add_argument("--interactive", action="store_true", help="Interactive mode")
    
    # Batch command
    batch_parser = subparsers.add_parser("batch", help="Batch process queries")
    batch_parser.add_argument("--index", required=True, help="Index directory")
    batch_parser.add_argument("--input", required=True, help="Input file with queries")
    batch_parser.add_argument("--output", required=True, help="Output file for results")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    # TODO: Implement actual functionality using ragflow package
    if args.command == "index":
        print(f"Indexing documents from {args.input} to {args.output}...")
        print("TODO: Implement indexing functionality")
    elif args.command == "query":
        if args.interactive:
            print("Interactive query mode...")
            print("TODO: Implement interactive query")
        else:
            print(f"Querying: {args.question}")
            print("TODO: Implement query functionality")
    elif args.command == "batch":
        print(f"Batch processing from {args.input} to {args.output}...")
        print("TODO: Implement batch processing")


if __name__ == "__main__":
    main()
