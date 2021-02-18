# Despliegue del back
Para desplegar el servidor, seguir los siguientes pasos: 
1. Iniciar el ambiente con el comando
    
        source Proyect/Scripts/activate

2. Instalar las siguientes dependencias.   

        pip3 install flask

        pip3 install flask-sqlalchemy

        pip3 install flask-restful

        pip3 install flask-marshmallow

3. Ejecutar el archivo app.py
   
        python3 app.py