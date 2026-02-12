from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router
from services.search_service import search_youtube

app = FastAPI()

# Security for receiving queries
app.addMiddleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Registers API Router that are handled in routes.py
app.include_router(router)