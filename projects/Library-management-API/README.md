# 📚 Library Management API

A simple Library Management REST API built with **FastAPI**.

This project allows users to add books, borrow books, return books, and view all users and books. While building this project, I focused on learning backend business logic, request validation, and API development using FastAPI.

---

# 📖 Overview

The API simulates a basic library system.

When a user borrows a book, the system checks several business rules before allowing the request. It verifies whether the book exists, whether it is available, whether the user has reached the borrowing limit, and updates both the user and book records accordingly.

The project stores data using Python dictionaries, making it a good practice project for understanding backend logic before moving to a real database.

---

# ✨ Features

- Add new books
- View all books
- Borrow books
- Return borrowed books
- Automatically create a new user on the first borrow request
- Prevent borrowing unavailable books
- Limit each user to borrowing a maximum of 3 books
- Track borrowed books for each user
- View all users

---

# 🛠 Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn
- Python Dictionaries (In-memory storage)

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone <repository-url>
```

## 2. Move into the project folder

```bash
cd fastapi-basics
```

## 3. Create a virtual environment

```bash
python -m venv .venv
```

## 4. Activate the virtual environment

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

## 5. Install dependencies

```bash
pip install -r requirements.txt
```

## 6. Run the API

```bash
uvicorn Library_management_API:app --reload
```

## 7. Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# 🔗 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/book` | Add a new book |
| GET | `/books` | View all books |
| GET | `/borrow/{user_id}/{book_id}` | Borrow a book |
| POST | `/return/{user_id}/{book_id}` | Return a borrowed book |
| GET | `/users` | View all users |

---

# 📜 Business Rules

## Book Validation

- Book ID cannot be empty.
- Book title must contain at least 2 characters.
- Author name must contain at least 2 characters.
- Empty or whitespace-only values are rejected.
- Duplicate book IDs are not allowed.

## Borrow Rules

- The requested book must exist.
- If the user does not exist, a new user is created automatically.
- A book can only be borrowed if it is available.
- A user can borrow a maximum of 3 books.
- If the borrowing limit is exceeded, a violation is recorded.

## Return Rules

- The user must exist.
- The book must exist.
- The user must have borrowed that book before returning it.

---

# 📚 What I Learned

While building this project, I learned:

- How to build REST APIs using FastAPI.
- How to organize backend logic into small helper functions.
- How to use Pydantic models for request validation.
- How `Field()` validates input data.
- How `field_validator()` can reject invalid input such as empty strings or whitespace.
- How business rules are different from API endpoints.
- How dictionaries can simulate a simple database.
- How writing a README helps organize my thoughts and understand my own project better.

---

# 🚀 Future Improvements

In the future, I would like to improve this project by:

- Replacing dictionaries with SQLite or PostgreSQL.
- Adding user authentication.
- Adding due dates for borrowed books.
- Adding search functionality.
- Improving error handling.
- Adding logging.
- Writing automated tests.
- Deploying the API to the cloud.

---

# 👨‍💻 Author

**Madhusudan Yemmewar**

Backend & AI Engineering (Learning in Public)