# python-app
we like python and docker

## core frameworks

in this project, we rely on two frameworks: Quart and SQLAlchemy

## TODO

- [x] mover CRUD de student para StudentRepository
- [x] mover CRUD de subject para SubjectRepository
- [ ] mover CRUD de user para UserRepository (tem que criar, modulo auth)
- [x] esperar container do banco inicializar antes de rodar o server
- [ ] documentar todas nossas rotas e como funcina o processo de autenticacao
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
