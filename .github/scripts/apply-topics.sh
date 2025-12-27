#!/bin/bash

# Script to manually apply GitHub topics to the repository
# This script reads topics from .github/topics.json and applies them using GitHub CLI

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TOPICS_FILE="$SCRIPT_DIR/../topics.json"

if [ ! -f "$TOPICS_FILE" ]; then
    echo "Error: topics.json not found at $TOPICS_FILE"
    exit 1
fi

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo "Error: GitHub CLI (gh) is not installed."
    echo "Please install it from: https://cli.github.com/"
    exit 1
fi

# Check if gh is authenticated
if ! gh auth status &> /dev/null; then
    echo "Error: GitHub CLI is not authenticated."
    echo "Please run: gh auth login"
    exit 1
fi

# Check if jq is installed
if ! command -v jq &> /dev/null; then
    echo "Error: jq is not installed."
    echo "Please install it: sudo apt-get install jq (Ubuntu/Debian) or brew install jq (macOS)"
    exit 1
fi

# Get repository name
REPO=$(gh repo view --json nameWithOwner -q .nameWithOwner)

if [ -z "$REPO" ]; then
    echo "Error: Could not determine repository name. Are you in a git repository?"
    exit 1
fi

echo "Repository: $REPO"
echo "Reading topics from: $TOPICS_FILE"

# Read topics from JSON file
TOPICS=$(jq -r '.names[]' "$TOPICS_FILE")

echo ""
echo "Topics to add:"
echo "$TOPICS" | sed 's/^/  - /'
echo ""

# Build the gh command
CMD="gh repo edit $REPO"
while IFS= read -r topic; do
    CMD="$CMD --add-topic $topic"
done <<< "$TOPICS"

# Execute the command
echo "Applying topics..."
eval "$CMD"

echo ""
echo "✓ Topics updated successfully!"
echo ""
echo "You can verify the topics at: https://github.com/$REPO"
