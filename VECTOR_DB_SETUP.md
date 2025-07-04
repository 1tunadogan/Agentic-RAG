# Vector Database Configuration

This RAG application supports two vector database backends:

1. **Chroma** (default) - Local, file-based vector database
2. **Qdrant** - High-performance vector database with cloud and self-hosted options

## Configuration

Use the `VECTOR_DB` environment variable to choose your vector database:

```bash
# Use Chroma (default)
VECTOR_DB=chroma

# Use Qdrant
VECTOR_DB=qdrant
```

## Chroma Setup (Default)

Chroma is the default vector database and requires no additional setup. Data is stored locally in the `./.chroma` directory.

### Environment Variables
```bash
VECTOR_DB=chroma  # or omit this line for default
```

## Qdrant Setup

### Option 1: Local Qdrant with Docker

1. Run the setup script:
   ```bash
   ./setup_qdrant.sh
   ```

2. Configure environment variables:
   ```bash
   VECTOR_DB=qdrant
   QDRANT_URL=http://localhost:6333
   QDRANT_API_KEY=  # leave empty for local setup
   ```

### Option 2: Qdrant Cloud

1. Sign up at [Qdrant Cloud](https://cloud.qdrant.io/)
2. Create a cluster and get your API key
3. Configure environment variables:
   ```bash
   VECTOR_DB=qdrant
   QDRANT_URL=https://your-cluster-url.qdrant.cloud
   QDRANT_API_KEY=your-api-key-here
   ```

### Option 3: Self-hosted Qdrant

1. Install and run Qdrant on your server
2. Configure environment variables:
   ```bash
   VECTOR_DB=qdrant
   QDRANT_URL=http://your-server:6333
   QDRANT_API_KEY=your-api-key  # if authentication is enabled
   ```

## Environment Variables

Create a `.env` file (see `.env.example` for template):

```bash
# Vector Database Selection
VECTOR_DB=chroma  # or "qdrant"

# Qdrant Configuration (only needed if VECTOR_DB=qdrant)
QDRANT_URL=http://localhost:6333
QDRANT_API_KEY=

# Required API Keys
GOOGLE_API_KEY=your_google_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

## Dependencies

### Chroma Dependencies
Already included in requirements.txt:
- `langchain-chroma==0.1.2`

### Qdrant Dependencies
Added to requirements.txt:
- `qdrant-client==1.12.1`
- `langchain-qdrant==0.1.3`

## Collection Names

- **Chroma**: `rag-chroma`
- **Qdrant**: `rag-qdrant`

## Fallback Behavior

If Qdrant is selected but the dependencies are not installed, the application will automatically fall back to Chroma with a warning message.

## Performance Considerations

### Chroma
- **Pros**: Simple setup, no external dependencies, good for development
- **Cons**: Limited scalability, single-machine only

### Qdrant
- **Pros**: High performance, scalable, cloud-ready, advanced filtering
- **Cons**: Requires additional setup, external dependency

## Switching Between Databases

To switch from Chroma to Qdrant:
1. Set `VECTOR_DB=qdrant` in your `.env` file
2. Configure Qdrant connection settings
3. Restart the application - it will automatically recreate the vector store

To switch back to Chroma:
1. Set `VECTOR_DB=chroma` in your `.env` file (or remove the line)
2. Restart the application

**Note**: Switching databases will require re-ingestion of documents as the vector stores are separate.