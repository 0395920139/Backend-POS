<!-- build environment -->

python3 -m venv New-POS
mkdir repo
source ../bin/activate

<!-- build environment -->


<!-- build django -->

pip install django
<!-- django-admin startproject BackEndPOS
python manage.py runserver -->

<!-- build django -->

<!-- database -->


$ sudo su postgres
$ psql
postgres=# create database pos_web encoding='UTF-8';
CREATE DATABASE
postgres=# create user pos_exuser with password '123456';
CREATE ROLE
postgres=# grant all privileges on database pos_web to pos_exuser;
GRANT
postgres=# 
# \q


$ pip install psycopg2-binary

<!-- database -->

<!-- restfull apo -->
pip install djangorestframework
pip install -U django-rest-knox
<!-- restfull apo -->


