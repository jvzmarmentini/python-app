# python-app
we like python and docker

## core frameworks
in this project, we rely on two frameworks: Quart and SQLAlchemy

### Quart
Quart is a web microframework. the microframework means that is does de bare minimum expected from a web framework. iow, it leaves to you the decision of which ORM you want to use. for example, Django is a web framework that includes an ORM, making it really difficult to use with SQLAlchemy, for example.

But why use Quart intead of Flask? tldr Quart is a reimplementation of Flask with asyncio. its and """updgrade""". since we're dealing with microservices, we really want to have the benefits of asynchronous.

### SQLAlchemy
Why? 'cause the name is cool


## Functionalities

- [x] Registra o estudante: nome, número do documento, endereço. Ao 
cadastrar o estudante (evitando duplicações) cria-se um número de 
matrícula para o estudante. 

- [x] Consulta um estudante pelo número de matrícula;
- [ ] Consulta um estudante por um pedaço de seu nome. Se houver mais
de um "match", retorna uma lista;

- [x] Consulta a lista de todos os estudantes;

- [x] cadastrar disciplinas, com os dados: codigo da disciplina, nome da 
disciplina, horário da disciplina (por códigos: A, B, C, D ...., G), turma 
da disciplina (código numérico). Lembre-se que uma mesma 
disciplina (mesmo código e nome) pode ocorrer mais de uma vez
(turmas diferentes);

- [ ] Matricular estudante na disciplina: informa número de matrúcula do 
estudante, código e turma da disciplina.

- [ ] Consultar as disciplinas/turmas em que um estudante está 
matriculado;

- [ ] Consultar os estudantes matriculados em uma disciplina/turma

- [ ] Registra usuário do sistema, com seu email, nome e senha;

- [ ] Efetua login e logout. Obs: você pode implementar uma funcionalidade simples, com controles codificados por você, ou necessário utilizar as funções do framework de autenticação/autorização.

