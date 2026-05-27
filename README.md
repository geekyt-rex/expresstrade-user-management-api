# User Management API

A RESTful User Management API built using Flask and MySQL.

---

## Tech Stack

- Flask
- MySQL
- SQLAlchemy
- PyMySQL

---

## Features

- Create user
- Get all users
- Get user by ID
- Search users
- Pagination
- Validation
- Duplicate email handling
- JSON responses

---

## Project Structure

```text
routes/
models/
services/
database/
utils/
```

---

## Setup Instructions

### Clone Repository

```bash
git clone <repository-url>
cd user-management-api
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

---

### Activate Virtual Environment

#### Windows Git Bash

```bash
source venv/Scripts/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Database Setup

Create MySQL database:

```sql
CREATE DATABASE users;
```

Create `.env` file:

```env
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DB=users
```

---

## Run Application

```bash
python app.py
```

---

# API Endpoints

## Create User

```http
POST /users
```

Example Request:

```json
{
  "name": "Akshay",
  "email": "akshay@gmail.com",
  "role": "admin"
}
```

---

## Get All Users

```http
GET /users
```

---

## Get User By ID

```http
GET /users/1
```

---

## Search Users

```http
GET /users?search=akshay
```

---

## Pagination

```http
GET /users?page=1&limit=10
```

---

# Validation Rules

- name required
- email required
- role required
- email format validation
- duplicate email prevention

---

# Example Error Response

```json
{
  "success": false,
  "error": "User not found"
}
```

---

# Database Schema

| Column | Type |
|---|---|
| id | Integer |
| name | VARCHAR(100) |
| email | VARCHAR(100) UNIQUE |
| role | VARCHAR(50) |

---

# Assumptions

- MySQL server is running locally
- User has database creation privileges

---

# AI Usage Declaration

AI tools used:
- ChatGPT

AI-assisted sections:
- Project structure guidance
- Flask API implementation guidance
- Validation and pagination suggestions

Manual modifications:
- Integrated all modules manually
- Tested APIs manually
- Configured MySQL connection
- Debugged routes and validation

Assignment branch update