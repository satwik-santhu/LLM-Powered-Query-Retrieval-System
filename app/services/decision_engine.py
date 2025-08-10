<<<<<<< HEAD
# app/services/decision_engine.py
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize Groq client with correct parameters
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

def get_llm_response(question: str, context_chunks: list):
    """
    Get LLM response for a question using provided context chunks
    Optimized for faster response times.
    
    Args:
        question: The question to answer
        context_chunks: Context chunks to use for answering
        
    Returns:
        LLM generated answer
    """
    # Limit context to prevent excessive token usage and improve speed
    max_chunks = 3
    limited_chunks = context_chunks[:max_chunks]
    
    # Prepare context for Groq with length limits
    context = "\n\n".join(limited_chunks)
    # Limit context length to improve response time
    max_context_length = 2000
    if len(context) > max_context_length:
        context = context[:max_context_length] + "..."
    
    prompt = f"""You are an expert document analyst.
Given the following context:\n\n{context}\n\nAnswer this question: "{question}"

Provide a clear, concise answer based only on the information in the context. If the context doesn't contain enough information to answer the question, say so."""

    # Call Groq API with current supported model
    response = client.chat.completions.create(
        model="gemma2-9b-it",  # Updated to current supported model
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,  # Limit response length for faster processing
        temperature=0.3  # Lower temperature for faster, more focused responses
    )

    return response.choices[0].message.content
=======
# from openai import OpenAI



# def get_llm_response(question, clauses):
#     context = "\n\n".join(clauses)
#     prompt = f"""You are an insurance policy expert.
# Given the following clauses:\n\n{context}\n\nAnswer this question: "{question}"
# Return only the answer with reasoning from the text."""

#     response = client.chat.completions.create(
#         model="llama3-70b-8192",  # Required Groq-supported model
#         messages=[{"role": "user", "content": prompt}]
#     )

#     return response.choices[0].message.content





# app/services/decision_engine.py
from openai import OpenAI
import os
from dotenv import load_dotenv
from app.services.vector_store import query_vectors
from app.services.embedder import get_embedding  # You’ll need to make this

load_dotenv()

# Initialize Groq client
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),  # Put your Groq key in .env
    base_url="https://api.groq.com/openai/v1"
)

def get_llm_response(question):
    # Step 1: Convert question to embedding
    query_embedding = get_embedding(question)

    # Step 2: Search Pinecone for top chunks
    results = query_vectors(query_embedding, top_k=5)
    clauses = [match["metadata"]["text"] for match in results["matches"]]

    # Step 3: Prepare context for Groq
    context = "\n\n".join(clauses)
    prompt = f"""You are an insurance policy expert.
Given the following clauses:\n\n{context}\n\nAnswer this question: "{question}"
Return only the answer with reasoning from the text."""

    # Step 4: Call Groq API
    response = client.chat.completions.create(
        model="llama3-70b-8192",  # Groq model
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
>>>>>>> 403fe5837f5e87f357ce88dcdd60c34961fed4eb
