##Enjoy reading 
## TODO API 
  
  ![image](https://github.com/mirafzal114/TodoApi/assets/136591233/4e7f29ae-6fee-4292-96cb-0d9d15f88960)

  ![image](https://github.com/mirafzal114/TodoApi/assets/136591233/40f8095f-1f1a-4d42-93eb-3f27e89dd779)

  ![image](https://github.com/mirafzal114/TodoApi/assets/136591233/75cbe66b-8579-41b1-8b66-1448976eeb39)

  ![image](https://github.com/mirafzal114/TodoApi/assets/136591233/438c8999-e91b-4044-bb02-ba068eab0299)

  # TodoApi Django Project

This project is a simple Django API for managing tasks (todos) with basic CRUD functionality.

## Features

- **Task Model**: 
    - Model: `TodoApp`
        - `title`: CharField for the task title.
        - `description`: TextField for the task description.
        - `time_create`: DateTimeField for task creation time.
        - `is_completed`: BooleanField to track task completion status.

- **API Endpoints**:
    - `GET /api/todos/`: Retrieve all tasks.
    - `POST /api/todos/`: Create a new task.
    - `GET /api/todos/<id>/`: Retrieve a specific task by ID.
    - `PUT /api/todos/<id>/`: Update a specific task by ID.
    - `DELETE /api/todos/<id>/`: Delete a specific task by ID.

## Usage

### Installation

#### Docker
To run the project using Docker:

1. Ensure Docker is installed on your system.
2. Build the Docker image:
    ```
    docker build -t todoapi .
    ```

3. Run the Docker container:
    ```
    docker run -p 8000:8000 todoapi
    ```

### Local Development

To run the project locally without Docker:

1. Install Python 3.11.

2. Clone the repository:
    ```
    git clone https://github.com/mirafzal114/TodoApi/
    ```

3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```
    python manage.py migrate
    ```

5. Start the server:
    ```
    python manage.py runserver
    ```

## API Examples

#### Create a Task

```http
POST /api/todos/
Content-Type: application/json

{
    "title": "Sample Task",
    "description": "This is a sample task description."
}


