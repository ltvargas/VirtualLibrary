# VirtualLibrary

#Requisitos Python 3.9.5
1. Crear entorno virtual
2. Clonar repositorio
3. Saltar a la rama ltvargas
4. En el directorio pip install -r requirements.txt
5. python manage.py makemigrations
6. python manage.py migrate
7. python manege.py runserver

# Ejecución
1. Debes haber ejecutado python manege.py runserver
2. La ejecución se realiza en el main()
3. Descomentar la función load_previus_data() si se desea tener libros cargados previamente, se debe volver a comentar la linea luego de ejecutar el programa por primera vez

# Descripción 
Biblioteca virtual

1.Administrador

- Puede agregar nuevos libros al sistema.
- Puede buscar la información de un libro por el código.

2.Estudiante

- Puede ver los libros que están disponibles
- hacer préstamo de libros.
- Puede ver la información de los libros que ha prestado
- devolver un libro antes de los 30 días limites

Condiciones:
- La fecha de devolución de un libro es hasta 30 días de haberlo prestado.
- El estudiante no puede prestar más de un ejemplar del mismo título de ser el caso se sumará el stock
- Al prestar un libro este se reserva y luego se hace espréstamo.
