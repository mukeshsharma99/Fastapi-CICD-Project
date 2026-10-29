# 🚀 FastAPI Cloud-Native DevSecOps Platform

A backend application built with **FastAPI, PostgreSQL, Docker, Pytest, Git, GitHub, and GitHub Actions**.

The project demonstrates a basic production-style backend workflow from application development and database integration to containerization, automated testing, and Continuous Integration.

---

## 🛠️ Tech Stack

- **Python 3.12**
- **FastAPI**
- **Uvicorn**
- **PostgreSQL 16**
- **SQLAlchemy**
- **Pydantic**
- **Pytest**
- **HTTPX**
- **Docker**
- **Docker Compose**
- **Git**
- **GitHub**
- **GitHub Actions**

---

## 📌 Features

### FastAPI Backend

The application provides a REST API for managing users.

Implemented endpoints:

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Application health/message |
| POST | `/users` | Create a user |
| GET | `/users` | Get all users |
| GET | `/users/{user_id}` | Get user by ID |
| PUT | `/users/{user_id}` | Update user |
| DELETE | `/users/{user_id}` | Delete user |

---

## 🗄️ PostgreSQL Database

The application uses **PostgreSQL** as the database.

Implemented:

- SQLAlchemy ORM
- User database model
- Unique email constraint
- Database session management
- FastAPI database dependency
- PostgreSQL running through Docker Compose

### User Model

```text
User
├── id
├── name
└── email
```

---

## ✅ Validation & Error Handling

The API includes:

- Pydantic request validation
- Email validation
- Duplicate email protection
- `404` handling when a user does not exist
- Appropriate HTTP status codes

Example:

```text
POST /users
    ↓
Check existing email
    ↓
Create user
    ↓
Save to PostgreSQL
    ↓
Return created user
```

---

## 🐳 Docker

The application is containerized using Docker.

Docker Compose runs:

```text
FastAPI
   │
   ▼
PostgreSQL
```

### Services

```text
fastapi-container
fastapi-postgres
```

FastAPI runs on:

```text
http://localhost:8000
```

PostgreSQL is exposed locally on:

```text
localhost:5433
```

Inside the Docker Compose network, FastAPI connects to PostgreSQL using:

```text
postgres:5432
```

---

## 📦 Docker Compose

The project uses a persistent PostgreSQL Docker volume.

Start the application:

```bash
docker compose up -d --build
```

Check containers:

```bash
docker ps
```

Stop containers:

```bash
docker compose down
```

View FastAPI logs:

```bash
docker logs fastapi-container
```

---

## 📖 API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

```text
http://localhost:8000/docs
```

### ReDoc

```text
http://localhost:8000/redoc
```

---

## 🧪 Automated Testing

The project uses **Pytest** for API testing.

Current test coverage includes:

- Root endpoint
- Get users
- Create user
- Get user by ID
- User not found
- Update user
- Delete user
- Duplicate email validation

Run tests:

```bash
pytest
```

Current result:

```text
8 passed
```

---

## 🔄 GitHub Actions CI

The project includes a GitHub Actions workflow:

```text
.github/workflows/ci.yml
```

The CI workflow runs when code is:

- Pushed to `main`
- Submitted as a Pull Request to `main`

### Current CI Pipeline

```text
Git Push / Pull Request
          ↓
   GitHub Actions
          ↓
   Checkout Code
          ↓
   Setup Python 3.12
          ↓
 Install Dependencies
          ↓
       Pytest
          ↓
      Test Result
```

The purpose of the CI pipeline is to automatically run the test suite whenever changes are pushed to GitHub.

---

## 📁 Project Structure

```text
Fastapi-CICD-Project/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── dependencies.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
│
├── tests/
│   ├── __init__.py
│   └── test_main.py
│
├── .dockerignore
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── README.md
└── requirements.txt
```

---

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/mukeshsharma99/Fastapi-CICD-Project.git
```

```bash
cd Fastapi-CICD-Project
```

### 2. Create virtual environment

```bash
python -m venv .venv
```

### 3. Activate virtual environment

Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Start with Docker Compose

```bash
docker compose up -d --build
```

### 6. Open Swagger

```text
http://localhost:8000/docs
```

### 7. Run tests

```bash
pytest
```

---

## 🔐 Configuration

The application supports the `DATABASE_URL` environment variable.

### Local Development

```text
postgresql+psycopg://fastapi:fastapi_password@localhost:5433/fastapi_db
```

### Docker Compose

```text
postgresql+psycopg://fastapi:fastapi_password@postgres:5432/fastapi_db
```

This allows the same FastAPI application to work with different database connection settings depending on the environment.

---

## 📋 Current Project Status

### Completed

- [x] FastAPI application
- [x] PostgreSQL integration
- [x] SQLAlchemy ORM
- [x] User CRUD API
- [x] Pydantic validation
- [x] Error handling
- [x] Dockerfile
- [x] Docker Compose
- [x] PostgreSQL persistent volume
- [x] Pytest test suite
- [x] 8 automated tests passing
- [x] Git repository
- [x] GitHub repository
- [x] GitHub Actions CI
- [x] Automated testing through GitHub Actions

---

## 👨‍💻 Author

**Mukesh Sharma**

GitHub:

https://github.com/mukeshsharma99