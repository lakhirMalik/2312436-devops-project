# 2312436-devops-project

**Name:** Haji Lakhir
**Registration Number:** 2312436
**Course:** DevOps Fundamentals — Final Project

---

## Project Overview

A production-ready containerised microservice built with FastAPI and PostgreSQL,
deployed on AWS EC2 with a fully automated CI/CD pipeline using GitHub Actions.

---

## Architecture
| Component     | Technology              |
|---------------|-------------------------|
| Web Service   | FastAPI + Uvicorn       |
| Database      | PostgreSQL 15           |
| CI Pipeline   | GitHub Actions (flake8 + pytest) |
| CD Pipeline   | GitHub Actions + SSH    |
| Cloud Server  | AWS EC2 t2.micro        |
| Container     | Docker + Docker Compose |

---

## API Endpoints

| Method | Endpoint            | Description                        |
|--------|---------------------|------------------------------------|
| GET    | /health             | Health check with DB status        |
| POST   | /students           | Create a new student record        |
| GET    | /students           | List all students                  |
| GET    | /students/{reg_no}  | Get a student by registration number |

---

## Local Setup Instructions

### Prerequisites
- Docker and Docker Compose installed
- Git installed

### Steps

1. **Clone the repository**
```bash
   git clone https://github.com/lakhirMalik/2312436-devops-project.git
   cd YOUR_REGNUM-devops-project
```

2. **Create your .env file**
```bash
   cp .env.example .env
   # Edit .env and fill in your values
```

3. **Start the application**
```bash
   docker compose up -d --build
```

4. **Verify it's running**
```bash
   curl http://localhost:8000/health
```

5. **Stop the application**
```bash
   docker compose down
```

---

## Running Tests Locally

```bash
pip install -r requirements.txt
cd app
pytest tests/ -v
```

---

## Live Deployment

**Live URL:** http://54.208.253.95:8000

The app auto-deploys to AWS EC2 on every push to the `main` branch via the CD pipeline.

---

## CI/CD Pipeline

- **CI** — triggers on every push and pull request: runs `flake8` lint and `pytest` tests
- **CD** — triggers on push to `main`: SSHs into EC2 and runs `docker compose up --build`

---

## Environment Variables

| Variable          | Description                  |
|-------------------|------------------------------|
| `DATABASE_URL`    | PostgreSQL connection string |
| `POSTGRES_USER`   | Database username            |
| `POSTGRES_PASSWORD` | Database password          |
| `POSTGRES_DB`     | Database name                |
| `STUDENT_REG_NO`  | Your registration number     |

> Never commit your `.env` file. Use `.env.example` as a template.
