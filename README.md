## Getting started
```
vagrant up
vagrant ssh
cd /vagrant
sudo make
```
Visit http://127.0.0.1:8081/fizzbuzz from host machine to see a list of fizzbuzzes
Visit http://127.0.0.1:8081/fizzbuzz/1 from host machine to see the fizzbuzz with id equals 1

### Run this in the console to add an entry:
Though, I'd suggest just using the web api form
```
curl --include --request POST --header "Content-Type: application/json" --data-binary "{ 'message': 'hi'}" 'http://127.0.0.1:8081/fizzbuzz'
```

### Code changes
When you have code changes that you want to try out, run:
```
sudo make update
```
which will copy your code changes over and restart apache.

### Migrations and test data
When you have model changes you can create a migration via
```
make migrations
```
When you run
```
sudo make
```
It automatically loads test data.  You can update the data dump file to the
current app state by running
```
make dump-test-data
```
And then explicitly restore the data dump at any time via:
```
make load-test-data
```
Be sure to keep the data in sync with our migrations.