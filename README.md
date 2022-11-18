# Documentacion de las rutas endpoint de las API Rest

1) home:
    
        - GET: http://localhost:8000/

2) GET Method forms:

        - GET: http://localhost:8000/api/get/

3) GET endpoints:

        - GET: http://localhost:8000/api/v1/person/
        - GET: http://localhost:8000/api/v1/get/person/?first_name=&last_name=&age=
        - GET: http://localhost:8000/api/v1/get/person/id/?id=

<i>El parámetro query "id" admite el caracter "*" al comienzo, al final o ambos extremos, para obtener todos los resultados que coincidan luego de su posición.</i>

4) POST Method forms:

        - POST: http://localhost:8000/api/post/

