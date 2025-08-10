<<<<<<< HEAD
# app/services/retriever.py
import numpy as np
from typing import List
from app.services.embedder import get_embedding
from app.services.vector_store import vector_store
from sklearn.metrics.pairwise import cosine_similarity

def find_top_chunks(query: str, chunks: List[str] = None, chunk_embeddings: np.ndarray = None, top_k: int = 3) -> List[str]:
    """
    Find top matching chunks using FAISS vector store or fallback to direct similarity
    Optimized for faster search performance.
    
    Args:
        query: The search query
        chunks: List of text chunks (used for fallback)
        chunk_embeddings: Embeddings array (used for fallback)
        top_k: Number of results to return (limited to 5 for speed)
        
    Returns:
        List of top matching text chunks
    """
    # Limit top_k to improve performance
    top_k = min(top_k, 5)
    
    query_embedding = get_embedding(query)
    
    # Try to use FAISS vector store first
    if vector_store.get_stats()['total_vectors'] > 0:
        results = vector_store.search(query_embedding, k=top_k)
        return [result['metadata'].get('text', '') for result in results if result['metadata'].get('text')]
    
    # Fallback to direct similarity search if FAISS store is empty
    elif chunks is not None and chunk_embeddings is not None:
        # Limit chunks processed for speed
        max_chunks = min(len(chunks), 100)
        limited_embeddings = chunk_embeddings[:max_chunks]
        limited_chunks = chunks[:max_chunks]
        
        similarities = cosine_similarity([query_embedding], limited_embeddings)[0]
        top_indices = np.argsort(similarities)[::-1][:top_k]
        return [limited_chunks[i] for i in top_indices]
    
    else:
        return []

def add_chunks_to_vector_store(chunks: List[str], embeddings: np.ndarray) -> None:
    """
    Add text chunks and their embeddings to the FAISS vector store
    
    Args:
        chunks: List of text chunks
        embeddings: Corresponding embeddings
    """
    metadata = [{'text': chunk} for chunk in chunks]
    vector_store.add_vectors(embeddings, metadata)
=======
# app/services/retriever.py
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from app.services.embedder import get_embedding

def find_top_chunks(query, chunks, chunk_embeddings, top_k=3):
    query_embedding = get_embedding(query)
    similarities = cosine_similarity([query_embedding], chunk_embeddings)[0]
    top_indices = np.argsort(similarities)[::-1][:top_k]
    return [chunks[i] for i in top_indices]
>>>>>>> 403fe5837f5e87f357ce88dcdd60c34961fed4eb
