django_metro
============
Delhi Metro DBMS project, with a web based frontend. Powered by Django Framework and Bootstrap.

Requirements:

Python 2.7
Django

Build instructions:

1. cd to django_metro (Project folder)

2. source bin/activate  //Only if virtualenv installed

3. cd mymtero

4. python manage.py runserver


==============

things that need to be done-

1.working with forms.

2.models.py not final yet(composite primary key issue,places table......)
(once final we'll do syncdb to add all the tables to our database!!)

3.Inserting values into Database.

3.Connecting the database.

4.queries for processing requests.

5.Remove lost and found

6.Add commenting feature

7.read south (if models are altered no need to drop tables and syncdb again,south can alter tables in the database directly.).