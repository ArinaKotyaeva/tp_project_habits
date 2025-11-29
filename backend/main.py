from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from datetime import datetime
from routers import habits, statistics
from database import init_db
import os

init_db()

app = FastAPI(title="Habits Tracker API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(habits.router, prefix="/api/habits", tags=["habits"])
app.include_router(statistics.router, prefix="/api/statistics", tags=["statistics"])

static_dir = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")


@app.get("/status")
async def status_page():
    html_path = os.path.join(os.path.dirname(__file__), "static", "index.html")
    if os.path.exists(html_path):
        return FileResponse(html_path)
    return {"message": "Status page not found"}


@app.get("/")
async def root():
    return {
        "message": "Habits Tracker API",
        "status": "running",
        "version": "1.0.0",
        "endpoints": {
            "habits": "/api/habits/",
            "statistics_day": "/api/statistics/day",
            "statistics_week": "/api/statistics/week",
            "docs": "/docs",
            "openapi": "/openapi.json"
        }
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "Habits Tracker API",
        "timestamp": datetime.now().isoformat()
    }

