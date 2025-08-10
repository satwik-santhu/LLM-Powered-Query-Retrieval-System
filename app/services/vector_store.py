<<<<<<< HEAD
import faiss
import numpy as np
import pickle
import os
from typing import List, Tuple, Any

class FAISSVectorStore:
    def __init__(self, dimension: int = 384, index_file: str = "vector_index.faiss", metadata_file: str = "metadata.pkl"):
        """
        Initialize FAISS vector store
        
        Args:
            dimension: Vector dimension (384 for all-MiniLM-L6-v2)
            index_file: Path to save/load FAISS index
            metadata_file: Path to save/load metadata
        """
        self.dimension = dimension
        self.index_file = index_file
        self.metadata_file = metadata_file
        self.index = faiss.IndexFlatIP(dimension)  # Inner product (cosine similarity)
        self.metadata = []
        self.id_counter = 0
        
        # Load existing index if it exists
        self.load_index()
    
    def add_vectors(self, vectors: np.ndarray, metadata: List[dict]) -> None:
        """
        Add vectors to the FAISS index
        
        Args:
            vectors: numpy array of shape (n_vectors, dimension)
            metadata: list of metadata dictionaries for each vector
        """
        # Normalize vectors for cosine similarity
        faiss.normalize_L2(vectors)
        
        # Add to index
        self.index.add(vectors)
        
        # Add metadata with IDs
        for meta in metadata:
            meta_with_id = {**meta, 'id': self.id_counter}
            self.metadata.append(meta_with_id)
            self.id_counter += 1
        
        # Save to disk
        self.save_index()
    
    def search(self, query_vector: np.ndarray, k: int = 5) -> List[dict]:
        """
        Search for similar vectors
        
        Args:
            query_vector: Query vector of shape (dimension,)
            k: Number of results to return
            
        Returns:
            List of results with scores and metadata
        """
        # Reshape and normalize query vector
        query_vector = query_vector.reshape(1, -1).astype(np.float32)
        faiss.normalize_L2(query_vector)
        
        # Search
        scores, indices = self.index.search(query_vector, k)
        
        # Format results
        results = []
        for i, (score, idx) in enumerate(zip(scores[0], indices[0])):
            if idx >= 0:  # Valid index
                result = {
                    'score': float(score),
                    'metadata': self.metadata[idx] if idx < len(self.metadata) else {},
                    'index': int(idx)
                }
                results.append(result)
        
        return results
    
    def save_index(self) -> None:
        """Save FAISS index and metadata to disk"""
        try:
            faiss.write_index(self.index, self.index_file)
            with open(self.metadata_file, 'wb') as f:
                pickle.dump(self.metadata, f)
        except Exception as e:
            print(f"Error saving index: {e}")
    
    def load_index(self) -> None:
        """Load FAISS index and metadata from disk"""
        try:
            if os.path.exists(self.index_file):
                self.index = faiss.read_index(self.index_file)
                print(f"Loaded FAISS index with {self.index.ntotal} vectors")
            
            if os.path.exists(self.metadata_file):
                with open(self.metadata_file, 'rb') as f:
                    self.metadata = pickle.load(f)
                    if self.metadata:
                        self.id_counter = max(meta.get('id', 0) for meta in self.metadata) + 1
                print(f"Loaded {len(self.metadata)} metadata entries")
                
        except Exception as e:
            print(f"Error loading index: {e}")
            # Create new index if loading fails
            self.index = faiss.IndexFlatIP(self.dimension)
            self.metadata = []
            self.id_counter = 0
    
    def clear(self) -> None:
        """Clear the index and metadata"""
        self.index = faiss.IndexFlatIP(self.dimension)
        self.metadata = []
        self.id_counter = 0
        
        # Remove files
        if os.path.exists(self.index_file):
            os.remove(self.index_file)
        if os.path.exists(self.metadata_file):
            os.remove(self.metadata_file)
    
    def get_stats(self) -> dict:
        """Get statistics about the vector store"""
        return {
            'total_vectors': self.index.ntotal,
            'dimension': self.dimension,
            'metadata_count': len(self.metadata)
        }

# Global instance
vector_store = FAISSVectorStore()
=======
import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

# Load .env variables
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV")  # Example: "us-east-1"

if not PINECONE_API_KEY or not PINECONE_ENV:
    raise ValueError("Missing Pinecone API key or environment in .env file")

# Create Pinecone client instance
pc = Pinecone(api_key=PINECONE_API_KEY)

# Example index name
index_name = "hackrx-index"

# Create index if not exists
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=1536,  # match your embedding model
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region=PINECONE_ENV)
    )

# Connect to the index
index = pc.Index(index_name)

def upsert_vectors(vectors):
    """Upsert vectors into Pinecone"""
    index.upsert(vectors=vectors)

def query_vectors(vector, top_k=5):
    """Query vectors from Pinecone"""
    results = index.query(vector=vector, top_k=top_k, include_metadata=True)
    return results
>>>>>>> 403fe5837f5e87f357ce88dcdd60c34961fed4eb
