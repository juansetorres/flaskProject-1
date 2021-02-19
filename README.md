# Despliegue del back
Para desplegar el servidor, seguir los siguientes pasos: 
1. Iniciar el ambiente con el comando
    
        source Proyect/Scripts/activate

2. Instalar las siguientes dependencias.   

        pip3 install flask

        pip3 install flask-sqlalchemy

        pip3 install flask-restful

        pip3 install flask-marshmallow

        pip3 install flask_jwt_extended

        pip3 install python-dateutil

3. Ejecutar el archivo app.py
   
        python3 app.py

# Al hacer un cambio en el modelo de datos
Ejecutar las siguiente lineas:

        python3

        from app import db

        db.drop_all()

        db.create_all()

        exit()