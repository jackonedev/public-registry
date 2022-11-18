# Documentacion de las rutas endpoint de las API Rest



1) Para mostrar todos los registros de personas de la base de datos:

`localhost:8000/api/all/`


2) Para filtrar determinados registros de personas, por nombre, o apellido o edad

`localhost:8000/api/get?first_name=&last_name=&age=`


3) Para filtrar registros de personas por id

`localhost:8000/api/id?id=`

Este endpoint tiene la particularidad que si uno agrega "*" al comienzo, al final o ambas, usara esa expresion para buscar todas las alternativas que coincidan luego de dicho caracter.

