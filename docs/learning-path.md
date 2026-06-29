1. Python setup and minimal app

Initialized the project and Git repository.
Planned the project folder structure.
Set up a Python virtual environment.
Installed FastAPI and Uvicorn.
Created requirements.txt.
Built the first FastAPI application.
Learned how uvicorn app.main:app --reload works.
Used FastAPI's automatic Swagger documentation.
Started documenting our learning in docs/03-python.md.

2.  Improved interview-quality explanations for:
    FastAPI() application instance
    requirements.txt
    --reload
    Introduced the Separation of Concerns principle.
    Designed a production-ready FastAPI folder structure.
    Learned the purpose of:
    routers/
    services/
    schemas/
    database/
    config/
    utils/
    Understood why **init**.py exists.
    Added a professional /health endpoint.
    Connected the idea of /health with Kubernetes self-healing.

3.

Correct separation of responsibilities:
.env stores secrets and environment-specific values.
config/settings.py loads and exposes configuration to the application.
Installed python-dotenv.
Created the first .env file.
Built a configuration layer (settings.py).
Updated main.py to use configuration instead of hardcoded values.
Created a proper .gitignore.
Learned why committing secrets to Git is dangerous.
Introduced the best practice of using .env.example.
