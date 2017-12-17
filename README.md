# fizzbuzz
Django REST Framework API with a browser based web-UI contained with Docker. 

The purpose of fizzbuzz is to be a starter project. I went searching for a project doing something along these lines and was unable to find something that fit all the criteria of being a good development environment using the tech I wanted to see in place.
 
* Single command container and application startup
* PostgreSQL, Python 3.5, Django, and django-rest-framework
* Functioning Web-UI for the API out of the box
* Application code mapped from host machine to container for faster development

Along these lines, the application has gone through *many* iterations, but it's finally in a place to be forked for specific use cases. w00t.

### Start up the development envionment
```
git clone https://github.com/SeanPlacchetti/fizzbuzz.git
cd fizzbuzz
docker-compose up
```
Pull up your favorite browser and go to `http://127.0.0.1:8000/`


### It's as easy as that, now you just start coding.