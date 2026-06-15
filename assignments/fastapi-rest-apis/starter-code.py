"""
Starter code for Building REST APIs with FastAPI

This file contains the basic structure to get started with the assignment.
Add your implementation below each function definition.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

# Initialize the FastAPI application
app = FastAPI()

# Define Pydantic models for request/response validation
class TodoItem(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

# In-memory storage for todo items (for this exercise)
todos: List[TodoItem] = []

# Task 1: Create basic GET and POST endpoints
@app.get("/todos")
def get_todos():
    """Retrieve all todo items"""
    # TODO: Return all todo items
    pass

@app.post("/todos")
def create_todo(todo: TodoItem):
    """Create a new todo item"""
    # TODO: Add the todo item to the list and return it
    pass

# Task 2 & 3: Implement PUT and DELETE endpoints
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: TodoItem):
    """Update an existing todo item"""
    # TODO: Find the todo by id and update it
    pass

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    """Delete a todo item"""
    # TODO: Find and remove the todo item by id
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
