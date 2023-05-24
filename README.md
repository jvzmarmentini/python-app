# python-app

This repository contains the code for a microservices-based application implemented. This application create and manage students and subjects.

## Installation

1. Clone the repository;

2. Make sure you have docker installed in your machine:

```bash
docker --version
```

If Docker is not installed, follow the official Docker installation guide for your operating system: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

## Usage

Build and start the application using Docker Compose:

```bash
docker-compose up --build
```

This command will build the Docker images for each microservice and start the application containers.

The application will be accessible at `http://localhost:80`.

Access the following endpoints:

### Swagger API Documentation

- `GET /swagger`: Swagger UI for interactive API documentation. Browse and test the available endpoints.

### Health Endpoint

- `GET /health`: Health endpoint to check the status of the application. Returns a JSON response with the status information.

### Student Controller

- `GET /students`: Get a list of all students.
- `GET /students/<int:id>`: Get details of a specific student.
- `POST /students`: Create a new student.
- `PUT /students/<int:id>`: Update an existing student.
- `DELETE /students/<int:id>`: Delete a student.

### Subject Controller

- `GET /students/<int:student_id>/subjects`: Get a list of subjects for a specific student.
- `POST /students/<int:student_id>/subjects`: Create a new subject for a specific student.
- `PUT /students/<int:student_id>/subjects/<int:id>`: Update an existing subject for a specific student.
- `DELETE /students/<int:student_id>/subjects/<int:id>`: Delete a subject for a specific student.

### Enrollment Controller

- `POST /enrollments`: Enroll a student in a class.
- `GET /enrollments`: Get a list of enrollments with optional filters.

### User Controller

- `POST /register`: Register a new user.
- `POST /login`: Login and obtain a session token.
- `GET /logout`: Logout and invalidate the session token.

Refer to the API documentation for detailed information about each endpoint.

## Architecture

The application follows a microservices-based architecture, with separate modules for students, subjects, and user authentication.

- The `student` module handles CRUD operations related to students.
- The `subject` module handles CRUD operations related to subjects.
- The `enrollment` module handles the enrollment of students in classes.
- The `auth` module handles user registration, login, and logout.

## Contributing

Contributions are welcome! If you find any issues or want to add new features, feel free to open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## core frameworks

in this project, we rely on two frameworks: Quart and SQLAlchemy

## TODO

- [x] mover CRUD de student para StudentRepository
- [x] mover CRUD de subject para SubjectRepository
- [x] mover CRUD de user para UserRepository (tem que criar, modulo auth)
- [x] esperar container do banco inicializar antes de rodar o server
- [x] documentar todas nossas rotas e como funcina o processo de autenticacao
- [ ] talvez criar um AuthService no modulo common, que por sua vez chama o auth.AuthService, para deixar bem desacoplado (microservicos vao mudar a implementacao do common.AuthService para fazer chamada http para o servico de autenticacao)

## Functionalities

- [x] Registra o estudante: nome, número do documento, endereço. Ao 
cadastrar o estudante (evitando duplicações) cria-se um número de 
matrícula para o estudante. 

- [x] Consulta um estudante pelo número de matrícula;
- [x] Consulta um estudante por um pedaço de seu nome. Se houver mais
de um "match", retorna uma lista;

- [x] Consulta a lista de todos os estudantes;

- [x] cadastrar disciplinas, com os dados: codigo da disciplina, nome da 
disciplina, horário da disciplina (por códigos: A, B, C, D ...., G), turma 
da disciplina (código numérico). Lembre-se que uma mesma 
disciplina (mesmo código e nome) pode ocorrer mais de uma vez
(turmas diferentes);

```
POST /enrollments
{
    "subjectId": "",
    "classId": "",
    "studentId": ""
}
```

- [x] Matricular estudante na disciplina: informa número de matrúcula do 
estudante, código e turma da disciplina.

- [x] Consultar as disciplinas/turmas em que um estudante está 
matriculado;

- [x] Consultar os estudantes matriculados em uma disciplina/turma

- [x] Registra usuário do sistema, com seu email, nome e senha;

- [x] Efetua login e logout. Obs: você pode implementar uma funcionalidade simples, com controles codificados por você, ou necessário utilizar as funções do framework de autenticação/autorização.
