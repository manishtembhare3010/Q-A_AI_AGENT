# Knowledge-Based AI Agent

A FastAPI-based backend for a Retrieval-Augmented Generation (RAG) agent that uses documents, Excel, emails, and CRM data for intelligent information retrieval and question answering.

## Overview

This project implements a knowledge agent that can ingest various document types, index their content, and respond to natural language questions by retrieving relevant information from the indexed documents.

## Features

- **LLM-based answer generation** - Uses LLaMA 3 for generating accurate, context-aware responses
- **Document & data ingestion pipeline** - Supports multiple file formats
- **API for real-time querying** - FastAPI endpoints for question answering
- **Automatic document processing** - Indexes documents with appropriate chunking
- **Local LLM support** - Uses Ollama for local inference with fallback mechanisms

## Supported File Formats

- PDF documents (`.pdf`)
- Word documents (`.docx`, `.doc`)
- Excel spreadsheets (`.xlsx`, `.xls`, `.csv`) 
- Text files (`.txt`, `.md`, `.markdown`)
- Email files (`.eml`, `.msg`)

## Installation

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Ensure you have Ollama installed (optional, for local LLM support)
4. Place documents in the `data/` directory

## Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The API will be available at http://127.0.0.1:8000.

## API Endpoints

### `/ask` (POST)

Ask a question to the knowledge base.

**Request:**
```json
{
  "question": "Your question here"
}
```

**Response:**
```json
{
  "question": "Your question here",
  "answer": "The answer based on the knowledge base"
}
```

### `/reload` (POST)

Reload the knowledge base to include newly added documents.

**Response:**
```json
{
  "success": true,
  "message": "Knowledge base reloaded successfully",
  "document_count": 42
}
```

## How It Works

1. Documents are loaded from the `data/` directory and processed based on their file type
2. Text is extracted, chunked, and indexed for efficient retrieval
3. When a question is asked, the system:
   - Retrieves the most relevant document sections
   - Uses LLM (via Ollama) to generate a contextual answer
   - Falls back to keyword matching when needed

## Development

The project is structured as follows:

- `app/api/` - FastAPI routes and models
- `app/retrieval/` - Document processing and retrieval logic
- `data/` - Storage for documents to be indexed