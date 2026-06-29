from fastapi import FastAPI

from app.config.settings import APP_NAME

app = FastAPI(title=APP_NAME)

@app.get("/")
def root():
    return {
        "message":APP_NAME
    }