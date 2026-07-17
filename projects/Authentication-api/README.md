# Authentication API

A simple Authentication API built with FastAPI for learning backend engineering fundamentals.

## Features

- User Registration
- User Login
- Change Password
- Password Hashing with bcrypt
- Input Validation using Pydantic
- Proper HTTP Error Handling

## Tech Stack

- Python
- FastAPI
- Pydantic
- bcrypt

## API Endpoints

### Register

POST `/register`

Creates a new user with a securely hashed password.

---

### Login

POST `/login`

Verifies user credentials using bcrypt.

---

### Change Password

POST `/change-password`

Verifies the old password and securely stores the new hashed password.

## Concepts Practiced

- REST API Design
- Request Validation
- Password Hashing
- Authentication Flow
- Error Handling
- Backend Project Structure

## Future Improvements

- JWT Authentication
- Database Integration
- User Roles
- Email Verification
- Password Reset