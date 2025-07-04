# RAG-application-with-LangGraph

An advanced RAG (Retrieval-Augmented Generation) application built with LangGraph that supports multiple vector database backends.

## Features

- **Multiple Vector Databases**: Choose between Chroma (default) or Qdrant
- **Intelligent Routing**: Automatically routes queries to vector search or web search
- **Document Grading**: Evaluates document relevance and answer quality
- **Hallucination Detection**: Validates generated answers against retrieved facts
- **Web Search Fallback**: Uses Tavily for external knowledge when needed

## Vector Database Support

This application supports two vector database backends:

- **Chroma** (default): Simple, local file-based vector database
- **Qdrant**: High-performance vector database with cloud and self-hosted options

See [VECTOR_DB_SETUP.md](./VECTOR_DB_SETUP.md) for detailed configuration instructions.

## Quick Start

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and configure your API keys
4. (Optional) Set up Qdrant: `./setup_qdrant.sh`
5. Run the application: `python main.py`

## Configuration

Set your vector database preference in `.env`:

```bash
# Use Chroma (default)
VECTOR_DB=chroma

# Use Qdrant
VECTOR_DB=qdrant
QDRANT_URL=http://localhost:6333
```

See [VECTOR_DB_SETUP.md](./VECTOR_DB_SETUP.md) for complete configuration options.