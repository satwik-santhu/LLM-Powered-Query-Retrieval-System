<<<<<<< HEAD
# app/services/embedder.py
from sentence_transformers import SentenceTransformer
import textwrap
import numpy as np

# Load model once at startup (faster than reloading each time)
model = SentenceTransformer("all-MiniLM-L6-v2")

def chunk_text(text: str, max_length: int = 300):
    """
    Splits long text into smaller chunks for embedding.
    Reduced chunk size for faster processing.
    
    Args:
        text (str): The full text to split.
        max_length (int): Max characters per chunk.

    Returns:
        list[str]: List of text chunks.
    """
    # Remove extra whitespace before splitting
    cleaned_text = " ".join(text.split())
    # Split into smaller chunks for faster embedding
    chunks = textwrap.wrap(cleaned_text, width=max_length)
    # Limit total chunks to prevent excessive processing time
    return chunks[:50]  # Max 50 chunks to limit processing time

def chunk_and_embed(text: str):
    """
    Splits text into chunks and returns both the chunks and their embeddings.
    Optimized for faster processing with batch size limits.
    
    Args:
        text (str): Input text.

    Returns:
        tuple: (chunks list, embeddings ndarray)
    """
    chunks = chunk_text(text)
    if not chunks:
        return [], np.array([])
    
    # Process in smaller batches for better performance
    batch_size = 10
    all_embeddings = []
    
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i+batch_size]
        batch_embeddings = model.encode(batch, convert_to_numpy=True, batch_size=batch_size)
        all_embeddings.append(batch_embeddings)
    
    embeddings = np.vstack(all_embeddings) if all_embeddings else np.array([])
    return chunks, embeddings

def get_embedding(text: str):
    """
    Generates an embedding for a single text string.
    
    Args:
        text (str): Input text.

    Returns:
        ndarray: Embedding vector.
    """
    return model.encode([text], convert_to_numpy=True)[0]
=======
# app/services/embedder.py
from sentence_transformers import SentenceTransformer
import textwrap
import numpy as np

# Load model once at startup (faster than reloading each time)
model = SentenceTransformer("all-MiniLM-L6-v2")

def chunk_text(text: str, max_length: int = 500):
    """
    Splits long text into smaller chunks for embedding.
    
    Args:
        text (str): The full text to split.
        max_length (int): Max characters per chunk.

    Returns:
        list[str]: List of text chunks.
    """
    # Remove extra whitespace before splitting
    cleaned_text = " ".join(text.split())
    return textwrap.wrap(cleaned_text, width=max_length)

def chunk_and_embed(text: str):
    """
    Splits text into chunks and returns both the chunks and their embeddings.
    
    Args:
        text (str): Input text.

    Returns:
        tuple: (chunks list, embeddings ndarray)
    """
    chunks = chunk_text(text)
    embeddings = model.encode(chunks, convert_to_numpy=True)
    return chunks, embeddings

def get_embedding(text: str):
    """
    Generates an embedding for a single text string.
    
    Args:
        text (str): Input text.

    Returns:
        ndarray: Embedding vector.
    """
    return model.encode([text], convert_to_numpy=True)[0]
>>>>>>> 403fe5837f5e87f357ce88dcdd60c34961fed4eb
