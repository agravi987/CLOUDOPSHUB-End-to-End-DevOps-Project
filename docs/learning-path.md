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

4.

Mini Summary (Current Chat)
✅ What We Learned
Understood the difference between a Database and a DBMS.
Learned why PostgreSQL is chosen for production applications.
Installed:
sqlalchemy
psycopg2-binary
Updated the .env configuration with database details.
Created the database connection layer (database.py).
Learned the purpose of:
create_engine()
SessionLocal
Base
Built our first ORM model: Task.

5.

Why database schema changes should be handled with migrations (later using Alembic).
Why each request gets its own database session.
Introduced the complete request flow:
Router → Schema → Service → Database
Created the first request schema (TaskCreate).
Built the first business logic function (create_task).
Started the router layer.
Learned the purpose of:
db.add()
db.commit()
db.refresh()
Introduced the Single Responsibility Principle (SRP).

6. Completed Backend CRUD Operations for Task

- Updated `schemas/task.py` to include comprehensive Pydantic models: `TaskBase`, `TaskCreate`, `TaskUpdate`, and `TaskOut`.
- Implemented full CRUD logic in `routers/task_router.py` (GET all, GET by ID, POST, PUT, DELETE).
- Included the `task_router` into the main application via `app.include_router()`.
- Added step-by-step explanatory comments in the router detailing the flow of each HTTP request, from parameter extraction to database session handling, execution, and returning the result.

7.

What We Learned
Why Docker was created ("Works on My Machine" problem).
Difference between Virtual Machines and Containers.
Docker architecture:
Docker Hub
Docker Engine
Image
Container
Difference between an Image (blueprint) and a Container (running instance).
The Docker lifecycle:

8.  Reviewed Image vs Container with interview-quality explanations.
    Learned what a Dockerfile is.
    Understood every instruction:
    FROM
    WORKDIR
    COPY
    RUN
    CMD
    Learned the concept of Docker Layers.
    Understood Docker Layer Caching and why instruction order matters.
    Built our first Docker image using:

9.

Reviewed Docker layer caching with interview-quality explanations.
Understood what docker run actually does internally.
Learned Port Mapping (HOST_PORT:CONTAINER_PORT).
Understood why Uvicorn must listen on 0.0.0.0.
Learned:
docker ps
docker ps -a
docker logs
docker exec
docker stop
docker start
docker rm
Learned the complete Docker container lifecycle.
Introduced the purpose of .dockerignore.


