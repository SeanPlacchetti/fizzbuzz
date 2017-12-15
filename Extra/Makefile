all:  install migrate load-test-data restart-apache

install:
	cp -R /fizzbuzz* /var/www/
	rm -rf /opt/fizzbuzz/*
	cp -R /fizzbuzz/* /opt/fizzbuzz/

update: install restart-apache

migrate:
	python manage.py migrate

migrations:
	python manage.py makemigrations

dump-test-data:
	python manage.py dumpdata > /fizzbuzz/testdata/db.json

load-test-data:
	python manage.py loaddata /fizzbuzz/testdata/db.json

restart-apache:
	sudo service apache2 restart

uninstall:
	rm -rf /opt/fizzbuzz/*

.PHONY: install restart-apache uninstall migrate migrations dump-test-data \
	load-test-data update
