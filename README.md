--- cài đặt python ---
--- tạo môi trường ảo cho python ---
# windown : 
    + python -m venv backend
    + Set-ExecutionPolicy Unrestricted -Scope Process
    + ..\Scripts\activate
# cài đặt django 
    + pip install django
    + git clone <github.com>
# cài đặt postgresql 
    + https://www.youtube.com/watch?v=9enxgQes33s xem để cài đặt về windows
    + mở SQL shell(psql)
    + postgres=#  create database pos_web encoding='UTF-8';
        CREATE DATABASE
    + postgres=# create user pos_exuser with password '123456';
         CREATE ROLE 
    + postgres=# grant all privileges on database pos_web to pos_exuser;
        GRANT
# cài đặt khác 
    + pip install psycopg2-binary
    + pip install -U django-rest-knox  
    + pip install djangorestframework
    + python -m pip install Pillow
