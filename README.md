# CPSC334 Final Project: Todo App

Team Members: Maura Sweeney and Liwei Liu

### Our goal is to implement some of the CI/CD concepts learned in class in the creation of a full product including front end, back end, and a full test suite using GitHub Actions

## Project Description
A web-based Todo management application that allows users 
to add, view, delete, and mark tasks as complete.

## Tech Stack
- Backend: Python Flask
- Database: SQLite
- Frontend: HTML / CSS / JavaScript
- CI Tool: GitHub Actions
- Testing: pytest

## Features
- Add a new todo task
- View all todo tasks
- Delete a todo task
- Mark a task as complete/incomplete

## CI/CD Pipeline
This project uses GitHub Actions to implement an automated CI pipeline.
The pipeline is triggered automatically on every push and runs the following steps:

1. **Build**: Install project dependencies
2. **Unit Test**: Run unit tests on backend database functions
3. **Integration Test**: Run integration tests on Flask API endpoints

Every push must pass all three steps before the code is accepted.

## How to Contribute
1. Pull the latest code: git pull origin main
2. Make your changes
3. Stage your changes: git add .
4. Commit: git commit -m "describe what you did"
5. Push: git push origin main
6. Check GitHub Actions to confirm CI passed