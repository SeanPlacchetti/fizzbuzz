# fizzbuzz
Docker development environment for a Django REST Framework web application

###Playing with your application:

#####To run the app

`docker-compose up`

#####To run the tests

`docker-compose run web python manage.py test`

#####To auto-run the tests

Create a file called scent.py:

```
from subprocess import call
from sniffer.api import runnable

@runnable
def execute_tests(*args):
    fn = [ 'python', 'manage.py', 'test' ]
    fn += args[1:]
    return call(fn) == 0
```

#####Then you can run:

`docker-compose run web sniffer`

This will automatically run the tests each time you make changes to the code

###Generate a test coverage report

#####Generate coverage:

`docker-compose run web coverage run --source='.'  manage.py test`

#####Generate an html report

`docker-compose run web coverage html --directory=reports`

You will then find your coverage report in reports/index.html
