# Documentacion de las rutas endpoint de las API Rest

1) home:
    
        - GET: http://localhost:8000/

2) GET Method forms:

        - GET: http://localhost:8000/app/get/

3) GET REST endpoints:

        - GET: http://localhost:8000/api/v1/person/1/
        - GET: http://localhost:8000/api/v1/person/2/?first_name=&last_name=&age=
        - GET: http://localhost:8000/api/v1/person/id/?id=

<i>El parámetro query "id" admite el caracter "*" al comienzo, al final o ambos extremos, para obtener todos los resultados que coincidan luego de su posición.</i>

4) POST Method forms:

        - GET: http://localhost:8000/app/post/

5) POST REST endpoint:

        - POST: http://localhost:8000/api/v1/person/create/


6) PUT REST endpoint:

        - PUT: http://localhost:8000/api/v1/person/<id>/edit/


7) DELETE REST endpoint:

        - DELETE: http://localhost:8000/api/v1/person/<id>/delete/
