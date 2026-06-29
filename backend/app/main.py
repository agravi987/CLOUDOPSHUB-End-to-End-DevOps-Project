from fastapi import FastAPI

from app.config.settings import APP_NAME
from app.routers import task_router
from app.database.database import engine, Base

# First, this will be called to ensure database tables are created.
Base.metadata.create_all(bind=engine)

app = FastAPI(title=APP_NAME)

# First, this method will be called to include the task router endpoints in the app.
app.include_router(task_router.router)

@app.get("/")
def root():
    return {
        "message": APP_NAME
    }