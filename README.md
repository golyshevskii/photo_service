## User Manual (docker)

> Docker install required

1. Clone Github repository:

````
git clone https://github.com/golyshevskii/photo_service.git
````
2. Run docker containers 
``` 
docker-compose up -d
```

***
```http://0.0.0.0:8000/``` - main page

```http://0.0.0.0:8000/signin``` - sign in page

```http://0.0.0.0:8000/signup``` - sign up page

***

> 3.1. If there are no tables (SQL errors):
>> 1. Open new terminal
>> 2. Run command
```
docker exec -it django_app sh
```
>> 3. Run commands (separately):
```
python manage.py makemigrations
```
```
python manage.py migrate
```
***

4. Stop docker containers
```
docker-compose down
```