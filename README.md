
# Django CRUD API

This project is a Django CRUD API for managing `Office` and `Employees` data. It allows you to perform create, read, update, and delete operations on both models using MongoDB Atlas.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/wahid18-maqs/Django-CRUD-mongodb-.git
   cd djanocrud
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Run the server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints in Postman

### Offices

- **GET** `/api/offices/` - List all offices
- **POST** `/api/offices/` - Create a new office
- **GET** `/api/offices/{id}/` - Retrieve an office by ID
- **PUT** `/api/offices/{id}/` - Update an office by ID
- **DELETE** `/api/offices/{id}/` - Delete an office by ID

### Employees

- **GET** `/api/employees/` - List all employees
- **POST** `/api/employees/` - Create a new employee
- **GET** `/api/employees/{id}/` - Retrieve an employee by ID
- **PUT** `/api/employees/{id}/` - Update an employee by ID
- **DELETE** `/api/employees/{id}/` - Delete an employee by ID

## Postman Testing


### GET Offices

- **URL:** `http://127.0.0.1:8000/api/offices/`
- **Method:** GET

### POST Office

- **URL:** `http://127.0.0.1:8000/api/offices/`
- **Method:** POST
- **Body (JSON):**
   ```json
   {
     "name": "Office A",
     "location": "Location A"
   }
   ```

### GET Employees

- **URL:** `http://127.0.0.1:8000/api/employees/`
- **Method:** GET

### POST Employee

- **URL:** `http://127.0.0.1:8000/api/employees/`
- **Method:** POST
- **Body (JSON):**
   ```json
   {
     "employeeid": "E001",
     "name": "william",
     "dateofjoining": "2023-10-01",
     "department": "HR"
   }
   ```
