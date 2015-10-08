## Getting started
```
vagrant up
vagrant ssh
cd /vagrant
sudo make
```
Then visit http://127.0.0.1:8081/ from host machine to see barebones apache+django is running.

You can visit http://127.0.0.1:8081/admin to see the admin site.

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