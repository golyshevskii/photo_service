## User Manual (docker)

> Docker install required

1. Clone Github repository:

````
git clone https://github.com/golyshevskii/photo_service.git
````
2. Run docker containers 
``` 
docker-compose up
```

***
> admin auth: admin/admin ```http://0.0.0.0:8000/admin```

```http://0.0.0.0:8000/``` - main page

```http://0.0.0.0:8000/auth/login``` - login page

```http://0.0.0.0:8000/auth/signup``` - signup page

```http://0.0.0.0:8000/yourposts``` - posts by user

```http://0.0.0.0:8000/post``` - post new photo

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