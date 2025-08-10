<<<<<<< HEAD
# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.query import router as query_router

app = FastAPI(title="LLM Query System")

# Add CORS middleware for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(query_router, prefix="/api/v1/hackrx")
=======
# app/main.py
from fastapi import FastAPI
from app.routes.query import router as query_router

app = FastAPI(title="LLM Query System")

app.include_router(query_router, prefix="/api/v1/hackrx")
>>>>>>> 403fe5837f5e87f357ce88dcdd60c34961fed4eb
