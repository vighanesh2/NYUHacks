#!/bin/bash

# Simple FastAPI startup script - uses system Python3

echo "🚀 Starting FastAPI Backend..."
echo ""

# Use python3 directly
PYTHON=python3

# Check if Python3 is available
if ! command -v $PYTHON &> /dev/null; then
    echo "❌ Error: python3 not found. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Using: $($PYTHON --version)"
echo ""

# Check if dependencies are installed
if ! $PYTHON -c "import fastapi" 2>/dev/null; then
    echo "📦 Installing dependencies..."
    $PYTHON -m pip install -r requirements.txt
    echo ""
fi

# Verify FastAPI is installed
if ! $PYTHON -c "import fastapi" 2>/dev/null; then
    echo "❌ Error: FastAPI installation failed."
    echo "   Please run manually: python3 -m pip install -r requirements.txt"
    exit 1
fi

echo "✅ Dependencies ready"
echo ""
echo "🌐 Starting server on http://localhost:8000"
echo "📚 API docs: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Run the server
cd "$(dirname "$0")"
$PYTHON src/main.py

