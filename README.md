**Employee APP**

## About the project:
Users should be able to:
- Create, read, update, and delete employees
- Search employee by first name, last name, email
- Receive form validations when trying to create/edit an employee
- Filter employees by: Year (date of birth), and skills
- State management 
- Unit tests
---

## Requirements

- Docker
- Docker-compose
- Makefile reader installed on device

---

## Installations guide

### Using Docker-compose

1. docker-compose up --build
2. docker-compose down

---

### Using Makefile

1. Clone the repository
2. Run `make build` to build the docker image
3. Run `make run` to run the docker container
4. Run `make stop` to stop the docker container
5. Run `make test` to stop run unit tests

---
