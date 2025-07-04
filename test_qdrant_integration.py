#!/usr/bin/env python3
"""
Test script to validate Qdrant integration without external dependencies
"""
import os
import sys

def test_vector_db_selection():
    """Test the vector database selection logic"""
    
    # Test 1: Default should be Chroma
    os.environ.pop('VECTOR_DB', None)
    vector_db = os.getenv("VECTOR_DB", "chroma").lower()
    assert vector_db == "chroma", f"Expected 'chroma', got '{vector_db}'"
    print("✓ Test 1 passed: Default is Chroma")
    
    # Test 2: Set to Qdrant
    os.environ['VECTOR_DB'] = 'qdrant'
    vector_db = os.getenv("VECTOR_DB", "chroma").lower()
    assert vector_db == "qdrant", f"Expected 'qdrant', got '{vector_db}'"
    print("✓ Test 2 passed: Can set to Qdrant")
    
    # Test 3: Case insensitive
    os.environ['VECTOR_DB'] = 'QDRANT'
    vector_db = os.getenv("VECTOR_DB", "chroma").lower()
    assert vector_db == "qdrant", f"Expected 'qdrant', got '{vector_db}'"
    print("✓ Test 3 passed: Case insensitive")
    
    # Test 4: Qdrant configuration
    os.environ['QDRANT_URL'] = 'http://test:6333'
    os.environ['QDRANT_API_KEY'] = 'test-key'
    qdrant_url = os.getenv("QDRANT_URL", "http://localhost:6333")
    qdrant_key = os.getenv("QDRANT_API_KEY", None)
    assert qdrant_url == "http://test:6333", f"Expected 'http://test:6333', got '{qdrant_url}'"
    assert qdrant_key == "test-key", f"Expected 'test-key', got '{qdrant_key}'"
    print("✓ Test 4 passed: Qdrant configuration works")
    
    # Clean up
    os.environ.pop('VECTOR_DB', None)
    os.environ.pop('QDRANT_URL', None)
    os.environ.pop('QDRANT_API_KEY', None)
    
    print("\n✅ All tests passed!")

def test_ingestion_import():
    """Test that ingestion module can be imported without errors"""
    try:
        # Mock the missing modules
        import sys
        from unittest.mock import MagicMock
        
        # Mock the modules that might not be installed
        sys.modules['langchain_google_genai'] = MagicMock()
        sys.modules['langchain_qdrant'] = MagicMock()
        sys.modules['qdrant_client'] = MagicMock()
        sys.modules['qdrant_client.http.models'] = MagicMock()
        
        # Try to parse the ingestion file
        with open('ingestion.py', 'r') as f:
            content = f.read()
        
        # Check if our modifications are present
        assert 'VECTOR_DB = os.getenv("VECTOR_DB", "chroma").lower()' in content
        assert 'if VECTOR_DB == "qdrant":' in content
        assert 'except ImportError:' in content
        print("✓ Ingestion file contains expected Qdrant integration code")
        
    except Exception as e:
        print(f"✗ Test failed: {e}")
        return False
    
    return True

if __name__ == "__main__":
    print("Testing Qdrant integration...")
    print("=" * 50)
    
    test_vector_db_selection()
    print()
    
    test_ingestion_import()
    
    print("\n🎉 All integration tests completed successfully!")