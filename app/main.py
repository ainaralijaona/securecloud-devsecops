
from fastapi import FastAPI, HTTPException, status
from app.models import Task, TaskCreate

app = FastAPI(
    title="SecureCloud API",
    description="DevSecOps Security Platform",
    version="1.0.0"
)

tasks: dict[int, Task] = {}
next_id = 1


@app.get("/")
def root():
    return {"message": "Welcome to SecureCloud API"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task: TaskCreate):
    global next_id

    new_task = Task(id=next_id, **task.model_dump())
    tasks[next_id] = new_task
    next_id += 1

    return new_task


@app.get("/tasks", response_model=list[Task])
def get_tasks():
    return list(tasks.values())


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return tasks[task_id]


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: TaskCreate):
    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    updated_task = Task(id=task_id, **task.model_dump())
    tasks[task_id] = updated_task

    return updated_task


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    del tasks[task_id]
    return None
