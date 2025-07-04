import os
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

# Configuration for vector database selection
VECTOR_DB = os.getenv("VECTOR_DB", "chroma").lower()  # chroma or qdrant

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")  

urls = [
    "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
    "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
]

docs = [WebBaseLoader(url).load() for url in urls]
docs_list = [item for sublist in docs for item in sublist]

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=250, chunk_overlap=0
)
doc_splits = text_splitter.split_documents(docs_list)

# Initialize vector store based on configuration
if VECTOR_DB == "qdrant":
    try:
        from langchain_qdrant import QdrantVectorStore
        from qdrant_client import QdrantClient
        from qdrant_client.http.models import Distance, VectorParams
        
        # Qdrant configuration
        QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
        QDRANT_API_KEY = os.getenv("QDRANT_API_KEY", None)
        COLLECTION_NAME = "rag-qdrant"
        
        # Initialize Qdrant client
        client = QdrantClient(
            url=QDRANT_URL,
            api_key=QDRANT_API_KEY,
        )
        
        vectorstore = QdrantVectorStore.from_documents(
            documents=doc_splits,
            embedding=embeddings,
            url=QDRANT_URL,
            api_key=QDRANT_API_KEY,
            collection_name=COLLECTION_NAME,
        )
        
        retriever = QdrantVectorStore(
            client=client,
            collection_name=COLLECTION_NAME,
            embeddings=embeddings,
        ).as_retriever()
        
        print(f"Initialized Qdrant vector store with collection: {COLLECTION_NAME}")
        
    except ImportError:
        print("Qdrant dependencies not installed. Falling back to Chroma.")
        VECTOR_DB = "chroma"

if VECTOR_DB == "chroma":
    vectorstore = Chroma.from_documents(
         documents=doc_splits,
         collection_name="rag-chroma",
         embedding=embeddings,
         persist_directory="./.chroma",
     )

    retriever = Chroma(
        collection_name="rag-chroma",
        persist_directory="./.chroma",
        embedding_function=embeddings,
    ).as_retriever()
    
    print("Initialized Chroma vector store with collection: rag-chroma")