import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import analysis

app = FastAPI(title="CP Tracker API")

default_origins = "http://localhost:5173"
allowed_origins = os.getenv("ALLOWED_ORIGINS", default_origins).split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analysis.router)

@app.get("/")
def root():
    return {"status": "CP Tracker API running"}
