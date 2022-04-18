# fastapi-celery-sqlalchemy


### Description
Service for MD5 file hash calculation.  

API - **Fastapi**  
Worker manager - **Celery**  
Broker - **RabbitMQ**  
Backend - **Redis**  
ORM - **SQLAlchemy**

### API
http://localhost:8000/docs

### How to use
1) Run *docker-compose up -d*
2) Go to http://localhost:8000/docs
3) Upload a file
4) Get hash by file id

**The number of workers can be changed in** *docker-compose.yml:*
```
    deploy:
        replicas: <number of workers>
```