from fastapi import FastAPI
from app.routes import blog, ctf, task_tracker, user

app = FastAPI(
    title="API Gateway",
    description="Gateway for routing requests to different microservices",
    version="1.0.0"
)

app.include_router(blog.router, prefix="/blog", tags=["Blog"])
app.include_router(ctf.router, prefix="/ctf", tags=["CTF"])
app.include_router(task_tracker.router, prefix="/task-tracker", tags=["Task Tracker"])
app.include_router(user.router, prefix="/user", tags=["User"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
