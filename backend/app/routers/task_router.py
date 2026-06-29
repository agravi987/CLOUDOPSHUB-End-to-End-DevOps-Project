from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database.session import get_db
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskOut, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["tasks"])

# First, when a POST request is made to /tasks, this method will be called.
# It receives the task data in the request body, and sends the request to the database session.
# It creates a new task in the database and returns the created task.
@router.post("/", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(**task.model_dump() if hasattr(task, 'model_dump') else task.dict())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

# First, when a GET request is made to /tasks, this method will be called.
# It sends a request to the database to fetch all tasks and returns them as a list.
@router.get("/", response_model=List[TaskOut])
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks

# First, when a GET request is made to /tasks/{task_id}, this method will be called.
# It sends a request to the database to find the task by ID.
# If found, it returns the task; otherwise, it throws a 404 error.
@router.get("/{task_id}", response_model=TaskOut)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task

# First, when a PUT request is made to /tasks/{task_id}, this method will be called.
# It sends a request to find the task. If it exists, it updates the provided fields in the database.
@router.put("/{task_id}", response_model=TaskOut)
def update_task(task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db)):
    task_query = db.query(Task).filter(Task.id == task_id)
    existing_task = task_query.first()
    
    if not existing_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
        
    update_data = task_update.model_dump(exclude_unset=True) if hasattr(task_update, 'model_dump') else task_update.dict(exclude_unset=True)
    task_query.update(update_data, synchronize_session=False)
    db.commit()
    db.refresh(existing_task)
    return existing_task

# First, when a DELETE request is made to /tasks/{task_id}, this method will be called.
# It sends a request to the database to remove the task with that ID.
@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task_query = db.query(Task).filter(Task.id == task_id)
    task = task_query.first()
    
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
        
    task_query.delete(synchronize_session=False)
    db.commit()
    return None