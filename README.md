# python-app
we like python and docker

## core frameworks
in this project, we rely on two frameworks: Quart and SQLAlchemy

### Quart
Quart is a web microframework. the microframework means that is does de bare minimum expected from a web framework. iow, it leaves to you the decision of which ORM you want to use. for example, Django is a web framework that includes an ORM, making it really difficult to use with SQLAlchemy, for example.

But why use Quart intead of Flask? tldr Quart is a reimplementation of Flask with asyncio. its and """updgrade""". since we're dealing with microservices, we really want to have the benefits of asynchronous.

### SQLAlchemy
Why? 'cause the name is cool
