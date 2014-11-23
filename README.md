Django-Delhi_Metro
============

Delhi Metro Management system website powered by the Django framwork and MySQL as the database. 


## Requirements

Python 2.7

Django

MySQL

MySQLDB


## Build instructions:

1. cd to django_metro (Project folder)

2. source bin/activate  //Only if virtualenv installed

3. cd mymtero

4. python manage.py runserver


Note
====

Virtualenv has been used for this project.

The project is running on Django version 1.6.5 !!

The data has been loaded into the tables using the following query -

mysql>load data local infile 'absolutepath' into table table_name;


Tables
======

-> metro_stationinfo corresponds to stationinfo.txt.

-> metro_station corresponds to station.txt.

-> metro_places corresponds to places.txt.

-> metro_path corresponds to path.txt.

-> metro_review handled by the admin side.














