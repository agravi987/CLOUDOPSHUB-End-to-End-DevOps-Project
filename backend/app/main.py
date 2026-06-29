from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message":"CloudOpsHub"}

@app.get("/health")
def health():
    return {
        "status":"healthy"
    }