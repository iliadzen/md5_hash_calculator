## Description
This service calculates MD5 file hashes using the following components:
- API: **FastAPI**
- Worker Manager: **Celery**
- Message Broker: **RabbitMQ**
- Backend: **Redis**
- ORM: **SQLAlchemy**

## How to Use
1. Run `docker-compose up -d`
2. Navigate to [http://localhost:8000/docs](http://localhost:8000/docs)
3. Upload a file
4. Retrieve the hash using the file ID

**To adjust the number of workers**, modify `docker-compose.yml`:
```yaml
    deploy:
        replicas: <number of workers>
