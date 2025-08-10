# LLM Query System

A powerful document analysis system that allows users to upload PDF documents and ask questions to get AI-powered answers using advanced natural language processing.

## 🌟 Features

- **PDF Document Upload**: Upload PDF files directly through the web interface
- **Multi-Question Support**: Ask multiple questions about the same document
- **AI-Powered Responses**: Get intelligent answers using Groq's LLM API
- **Vector Search**: Efficient document retrieval using FAISS vector similarity search
- **Real-time Processing**: Live updates on document processing stages
- **Modern UI**: Clean React-based frontend with TypeScript support

## 🏗️ System Architecture
Frontend (React/TypeScript) → FastAPI Backend → AI Services ↓ Document Processing Pipeline: 1. PDF Text Extraction 2. Text Chunking & Embedding 3. Vector Storage (FAISS) 4. Semantic Search 5. LLM Response Generation

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+**
- **Node.js 16+**
- **npm or yarn**

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd llm_query_system
   ```

2. Backend Setup
    - Creating environment
    ```bash
    python -m venv venv
    ```
    - Activation virtual environment
    ```bash
    # Windows:
    venv\Scripts\activate
    # macOS/Linux:
    source venv/bin/activate
    ```

    - Installing dependencies
    ```bash
    pip install -r requirements.txt
    ```

3. Frontend Setup
    ```bash
    cd frontend
    npm install
    ```

4. Environment Configuration
    Create a `.env` file in the root directory
    ```bash
    # API Keys
    GROQ_API_KEY=your_groq_api_key_here

    # FAISS Configuration (Optional - uses defaults if not set)
    FAISS_INDEX_FILE=vector_index.faiss
    FAISS_METADATA_FILE=metadata.pkl
    VECTOR_DIMENSION=384
    ```

### Running the application
1. Start the Backend Server:
    ```bash
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
    ```

2. Start the Frontend Development Server
    ```bash
    cd frontend
    npm start
    ```

3. Access the Application:
    - Frontend: `http://localhost:3000`
    - Backend API `http://localhost:8000`
    - API Documentation: `http://localhost:8000/docs`

### API Documentation
Endpoints
1. `POST /api/v1/hackrx/upload`
    Upload a PDF file and ask questions about its content.

    Request:
    - `file`: PDF file (multipart/form-data)
    - `questions`: JSON array of questions (form field)
    - `authorization`: Bearer token required

    Response:
    ```
    {
    "answers": ["Answer 1", "Answer 2", "..."]
    }
    ```

2. `POST /api/v1/hackrx/run`
    Process a PDF from URL with questions.
    Request:
    ```
    {
        "documents": "https://example.com/document.pdf",
        "questions": ["Question 1", "Question 2"]
    }
    ```

### Technical Stack:
1. Backend
    - FastAPI: Modern Python web framework
Groq API: LLM for generating responses (llama-3.1-70b-versatile)
    - Sentence Transformers: Text embedding generation
    - FAISS: Vector similarity search and storage
    - PDFPlumber: PDF text extraction
    - Pydantic: Data validation and settings management

2. Frontend
    - React 18: UI library with hooks
    - TypeScript: Type-safe JavaScript
    - CSS3: Modern styling with flexbox/grid
    - Fetch API: HTTP client for backend communication
    AI/ML Components
    - Embedding Model: all-MiniLM-L6-v2 (384-dimensional vectors)
    - Chunking Strategy: Intelligent text segmentation for optimal retrieval
    - Vector Store: FAISS index for fast similarity search
    - LLM: Groq's Llama 3.1 70B model for response generation

### Project Structure
    ```bash
    llm_query_system/
    ├── .env
    ├── requirements.txt
    ├── vector_index.faiss
    ├── metadata.pkl
    ├── app/
    │   ├── main.py
    │   ├── routes/
    │   │   └── query.py
    │   └── services/
    │       ├── decision_engine.py
    │       ├── document_parser.py
    │       ├── embedder.py
    │       ├── retriever.py
    │       └── vector_store.py
    └── frontend/
        ├── package.json
        ├── public/
        │   └── index.html
        └── src/
            ├── App.tsx
            ├── index.tsx
            └── components/
                ├── FileUpload.tsx
                ├── QueryForm.tsx
                └── ResponseDisplay.tsx
    ```

### Supported Models
Current LLM models available:

`llama-3.1-70b-versatile (default)`
`llama-3.1-8b-instant`
`mixtral-8x7b-32768`

### Performance Optimization
- Vector Store: Persisted in vector_index.faiss for faster subsequent queries
- Chunking Strategy: Optimized for 384-dimensional embeddings
- Response Time: Limited to 500 tokens for faster processing
- Context Limiting: Maximum 3 chunks per query for optimal performance

### Contributing to this repo:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Support
For support, please open an issue in the GitHub repository or contact the development team.

Built with ❤️ using FastAPI, React, and Groq AI