# FastAPI School System

A backend API built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL** to model a simple school management system.

This project is part of my journey transitioning into **Python backend development**. It focuses on learning and applying backend concepts such as relational database modeling, REST API design, and clean architecture patterns.

---

## Current Features

The API currently supports a basic school domain with the following entities:

* **Students**
* **Profiles**
* **Teachers**
* **Subjects**
* **Enrollments**

Key capabilities implemented so far:

* RESTful API built with **FastAPI**
* Database modeling with **SQLAlchemy ORM**
* PostgreSQL integration
* One-to-one, one-to-many, and many-to-many relationships
* Nested Pydantic schemas
* Partial updates using `PATCH`
* Automatic OpenAPI documentation with Swagger UI
* Basic CRUD operations for the main entities

Example student routes currently implemented:

```
POST   /students
GET    /students
GET    /students/{id}
PATCH  /students/{id}
DELETE /students/{id}
```

---

## Tech Stack

* **Python**
* **FastAPI**
* **SQLAlchemy**
* **Pydantic**
* **PostgreSQL**
* **Uvicorn**

---

## Database Model

The system models a typical academic environment:

```
Student ─── Profile
   │
   │ enrollment
   ▼
Enrollment
   ▲
   │
Subject ─── Teacher
```

Relationships include:

* Student → Profile (one-to-one)
* Student → Subjects (many-to-many through enrollments)
* Teacher → Subjects (one-to-many)

---

## Project Goal

This repository is designed as an **evolving backend project**. The goal is not just to build an API, but to progressively improve the architecture following best practices used in real-world backend systems.

Future improvements will include:

* Separation of **routers**
* Introduction of **service layer**
* Introduction of **repository layer**
* Modular project structure
* Improved dependency management
* Better error handling
* Database migrations
* Automated testing

---

## Planned Architecture

The project will gradually evolve toward a more scalable backend structure:

```
app/
      main.py
      core/
      database/
      models/
      schemas/
      repositories/
      services/
      routers/
```

Architecture flow:

```
HTTP Request
      ↓
Router
      ↓
Service Layer
      ↓
Repository Layer
      ↓
Database
```

This structure improves:

* code organization
* testability
* maintainability
* separation of concerns

---

## Running the Project

Create a virtual environment:

```
python -m venv venv
```

Activate it:

```
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the server:

```
uvicorn app.main:app --reload
```

Open the API documentation:

```
http://127.0.0.1:8000/docs
```

---

## Learning Goals

This project helps me deepen my understanding of:

* REST API design
* SQLAlchemy relationships
* Pydantic schema modeling
* backend architecture patterns
* Python backend best practices

---

## Author

**Jaderson Rodrigues Ilidio**

Backend developer focused on Python and API development.
