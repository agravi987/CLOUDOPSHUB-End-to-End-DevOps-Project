from sqlalchemy.orm import Session

from app.models.task import Task

def create_task(db: Session, title: str, description: str):

    task = Task(
        title=title,
        description=description
    )

    db.add(task)

    db.commit()

    db.refresh(task)

    return task