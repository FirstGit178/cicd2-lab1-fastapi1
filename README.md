# CICD-2 FastAPI Lab Template

This repository contains a FastAPI lab for the CICD-2 module.  
Use this `README.md` as the standard structure for future labs.

---

## Lab Title

**Replace this with the lab title**

Example:

> Lab 1 — Creating a Basic FastAPI Application

---
## Repository Structure

Use the following structure for the labs:

```text
project-name/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   ├── services.py
│   └── models.py
│
├── tests/
│   ├── __init__.py
│   └── test_main.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Lab 5 — User API and Product Service

This project runs two FastAPI services:

- The **User API** runs on port 8000.
- The **Product Service** runs on port 8001.
- The User API contacts the Product Service to get product information.

### Start the services

Open two terminals in the project folder.

In Terminal 1, start the Product Service:

```bash
python -m uvicorn product_service.main:app --host 0.0.0.0 --port 8001 --reload