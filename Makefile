all:  install migrate load-test-data restart-apache

install:
	cp -R /vagrant/src/static* /var/www/
	rm -rf /opt/fizzbuzz/*
	cp -R /vagrant/src/* /opt/fizzbuzz/

update: install restart-apache

migrate:
	python /vagrant/src/manage.py migrate

migrations:
	python /vagrant/src/manage.py makemigrations

dump-test-data:
	python /vagrant/src/manage.py dumpdata > /vagrant/testdata/db.json

load-test-data:
	python /vagrant/src/manage.py loaddata /vagrant/testdata/db.json

restart-apache:
	/etc/init.d/apache2 restart

uninstall:
	rm -rf /opt/fizzbuzz/*

.PHONY: install restart-apache uninstall migrate migrations dump-test-data \
	load-test-data update
