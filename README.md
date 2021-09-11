# VirtualLibrary

#Requisitos Python 3.9.5
# Ejecución
1. Crear entorno virtual
   -python3 -m venv venv
   -cd venv/Scripts/activate.bat
2. Clonar repositorio (git clone https://github.com/ltvargas/VirtualLibrary.git)
   -Saltar a la rama ltvargas (git checkout ltvargas)
3. Backend
   - cd pydjango desde el ambiente
   - pip install -r requeriments.txt
   - python manage.py makemigrations
   - python manage.py migrate
   - python manage.py runserver
   - http://localhost:8000/admin/
4. fronend
   - cd virtuallibrary
   - Debes haber ejecutado python manege.py runserver
   - La ejecución se realiza en el main()
   - Descomentar la función load_previus_data() si se desea tener libros cargados previamente, se debe volver a comentar la linea luego de ejecutar el programa por primera vez
   - las credenciales se encuentrar en el file credentianls.csv

Nota: si al seguir todo los pasos tiene algun inconveniente pruebe instalando el contenido de requeriments por medio de pip install
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
- Al prestar un libro este se reserva y luego se hace el préstamo.
