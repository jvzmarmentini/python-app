# Python App

This repository contains the code for a microservices-based application implemented. This application create and manage students and subjects.

## Contributors
- Lucas Antunes
- Gabriel Panho
- João Marmetini

## Installation

1. Clone the repository;

2. Make sure you have docker installed in your machine:

```bash
docker --version
```

If Docker is not installed, follow the official Docker installation guide for your operating system: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

## Core frameworks

In this project, we rely on two frameworks: Flask and SQLAlchemy. That's it (:

## Test

To run the tests, simply execute:

```bash
cd auth-service && pytest && cd .. &&\
cd student-service && pytest && cd .. &&\
cd enrollment-service && pytest && cd ..
```

It will find all microservices tests. If you need to see a specific one, move to the desired folder and run the same command.

For more verbose, use the `-v` flags

## Usage

Build and start the application using Docker Compose:

```bash
docker-compose up --build
```

This command will build the Docker images for each microservice and start the application containers.

If you need to reset or change the application

```bash
docker-compose down -v
```

Access the following endpoints (note that for most of them you need a session token, see the login route of the auth service to get one):


### Auth Controller

The auth service is mapped on port 5003

- `POST /register`: Register a new user.

```bash
curl -X POST -H "Content-Type: application/json" -d '{
    "email" : "johndoe@email.com",
    "password" : "123",
    "name" : "John Doe"
}' http://localhost:5003/register
```

- `POST /login`: Login and obtain a session token.

```bash
curl -X POST -H "Content-Type: application/json" -d '{
    "email" : "johndoe@email.com",
    "password" : "123"
}' http://localhost:5003/login
```

Use the following command to login and set token to `SESSION_TOKEN` env var in a single command.
```bash
SESSION_TOKEN=$(curl -X POST -H "Content-Type: application/json" -d '{
    "email" : "johndoe@email.com",
    "password" : "123"
}' http://localhost:5003/login | grep -Po '"sessionToken"\s*:\s*"\K[^"]+')
```

- `POST /logout`: Logout and invalidate the session token.

```bash
curl -X POST -H "session-token: $SESSION_TOKEN" http://localhost:5003/logout
```

- `POST /session`: Check if session token is valid.

```bash
curl -X POST -H "Content-Type: application/json" -d '{
    "sessionToken" : "e63e4b1e-2dc0-4ade-8ae7-8e9f97950db9",
}' http://localhost:5003/session
```

### Student Controller

The student is mapped on port 5000

- `GET`: Get a list of all students.

```bash
curl -X GET -H "session-token: $SESSION_TOKEN" http://localhost:5000/
```

- `GET /<int:id>`: Get details of a specific student.'

```bash
curl -X GET -H "session-token: $SESSION_TOKEN" http://localhost:5000/{id}
```

- `POST`: Create a new student.

```bash
curl -X POST -H "Content-Type: application/json" -H "session-token: $SESSION_TOKEN" -d '{"name": "John Doe", "document": 123456, "address": "123 Street"}' http://localhost:5000/
```

- `PUT /<int:id>`: Update an existing student.

```bash
curl -X PUT -H "Content-Type: application/json" -H "session-token: $SESSION_TOKEN" -d '{"name": "Updated Name", "document": 789012, "address": "456 Avenue"}' http://localhost:5000/{id}
```

- `DELETE /<int:id>`: Delete a student.

```bash
curl -X DELETE -H "session-token: $SESSION_TOKEN" http://localhost:5000/{id}
```

### Subject Controller

The subject is mapped on port 5001

- `GET`: Get a list of all subjects.

```bash
curl -X GET -H "session-token: $SESSION_TOKEN" http://localhost:5001/
```

- `GET /<int:id>`: Get details of a specific subject.'

```bash
curl -X GET -H "session-token: $SESSION_TOKEN" http://localhost:5001/{id}
```

- `POST`: Create a new subjects.

```bash
curl -X POST -H "session-token: $SESSION_TOKEN" -H "Content-Type: application/json" -d '{
    "class_num" : 4,
    "subject_num" : 4,
    "name" : "Biology",
    "schedule" : "D"}' http://localhost:5001/
```

- `PUT /<int:id>`: Update an existing subjects.

```bash
curl -X PUT -H "Content-Type: application/json" -H "session-token: $SESSION_TOKEN" -d '{"name": "Updated Name", "schedule": "E"}' http://localhost:5001/{id}
```

- `DELETE /<int:id>`: Delete a subjects.

```bash
curl -X DELETE -H "session-token: $SESSION_TOKEN" http://localhost:5001/{id}
```

### Enrollment Controller

The student is mapped on port 5002

- `POST`: Enroll a student in a class.

```bash
curl -X POST -H "Content-Type: application/json" -H "session-token: $SESSION_TOKEN" -d '{"studentId": 1, "subjectNum": 2, "classNum": 2}' http://localhost:5002
```

- `GET`: Get a list of enrollments with optional filters.

```bash
curl -X GET -H "session-token: $SESSION_TOKEN" http://localhost:5002/
```

## Architecture

The application follows a microservices-based architecture, with separate modules for students, subjects, enrollment and user authentication.

- The `student` module handles CRUD operations related to students.
- The `subject` module handles CRUD operations related to subjects.
- The `enrollment` module handles the enrollment of students in classes.
- The `auth` module handles user registration, login, and logout.

## Legacy code

The `app` directory contains the legacy code. It's totally function, and even has a swaggeer, but since we change the docker-compose, it won't work. 

## Contributing

Contributions are welcome! If you find any issues or want to add new features, feel free to open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
