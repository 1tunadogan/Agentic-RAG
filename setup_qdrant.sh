#!/bin/bash

# Setup script for Qdrant vector database
echo "Setting up Qdrant vector database..."

# Check if Docker is available
if ! command -v docker &> /dev/null; then
    echo "Docker is not installed. Please install Docker to run Qdrant locally."
    echo "Alternatively, you can use Qdrant cloud service."
    exit 1
fi

# Stop existing Qdrant container if running
echo "Stopping existing Qdrant container..."
docker stop qdrant-rag 2>/dev/null || true
docker rm qdrant-rag 2>/dev/null || true

# Start Qdrant container
echo "Starting Qdrant container..."
docker run -d \
    --name qdrant-rag \
    -p 6333:6333 \
    -p 6334:6334 \
    -v $(pwd)/qdrant_storage:/qdrant/storage:z \
    qdrant/qdrant:latest

echo "Qdrant is starting up..."
echo "Web UI will be available at: http://localhost:6333/dashboard"
echo "API endpoint: http://localhost:6333"
echo ""
echo "To use Qdrant, set the following in your .env file:"
echo "VECTOR_DB=qdrant"
echo "QDRANT_URL=http://localhost:6333"
echo ""
echo "To stop Qdrant: docker stop qdrant-rag"