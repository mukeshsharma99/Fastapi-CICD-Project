# 🚀 FastAPI CI/CD Project

A complete DevOps project demonstrating how to develop, test, containerize, and deploy a **FastAPI application** using **Docker, Docker Compose, GitHub Actions, and AWS EC2**.

The project starts with a FastAPI application, packages it into a Docker container, validates the application through GitHub Actions, and deploys the containerized application on an AWS EC2 Linux server.

---

## 📌 Project Overview

This project demonstrates the following workflow:

```text
                    Developer
                        │
                        ▼
                  GitHub Repository
                        │
                        ▼
                GitHub Actions (CI)
                        │
                 ┌──────┴──────┐
                 │             │
                 ▼             ▼
              Install        Run Tests
              Dependencies
                 │             │
                 └──────┬──────┘
                        ▼
                  CI Validation
                        │
                        ▼
                    AWS EC2
                        │
                        ▼
                     Docker
                        │
                        ▼
                 Docker Compose
                        │
                        ▼
                FastAPI Container
                        │
                        ▼
                    Uvicorn
                        │
                        ▼
                  FastAPI API
                        │
                        ▼
                  Port 8000
                        │
                        ▼
                    Internet
