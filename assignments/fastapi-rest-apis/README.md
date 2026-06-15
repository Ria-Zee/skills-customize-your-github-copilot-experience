# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build modern REST APIs using the FastAPI framework. You will create endpoints to handle HTTP requests, work with request and response models, and implement basic data management operations.

## 📝 Tasks

### 🛠️ Create Basic API Endpoints

#### Description
Set up a FastAPI application with basic GET and POST endpoints for managing a simple todo item list.

#### Requirements
Completed program should:

- Initialize a FastAPI application
- Create a GET endpoint to retrieve all todo items
- Create a POST endpoint to add a new todo item to the list
- Return data in JSON format with appropriate HTTP status codes

### 🛠️ Implement Request and Response Models

#### Description
Define Pydantic models for request validation and structured responses.

#### Requirements
Completed program should:

- Create a Pydantic model for todo items with fields: `id`, `title`, `description`, and `completed`
- Use the model for request body validation on the POST endpoint
- Return responses using the same model structure
- Include automatic API documentation through FastAPI's built-in features

### 🛠️ Add CRUD Operations

#### Description
Expand the API to support updating and deleting todo items.

#### Requirements
Completed program should:

- Create a PUT endpoint to update an existing todo item by id
- Create a DELETE endpoint to remove a todo item by id
- Handle cases where an item is not found with appropriate error responses
- Maintain an in-memory list of todo items for the session
