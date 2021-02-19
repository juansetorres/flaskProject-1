# Desarrollo
A continuación se describen los pasos de como desplegar la aplicación en un ambiente de desarrollo. 
## Back-end
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

        pip3 install flask-cors

        pip3 install flask-sqlalchemy marshmallow-sqlalchemy

3. Ejecutar el archivo app.py
   
        python3 app.py

# Al hacer un cambio en el modelo de datos
Ejecutar las siguiente lineas:

        python3

        from app import db

        db.drop_all()

        db.create_all()

        exit()

# Producción 
Para desplegar la aplicación en producción, se deben seguir los siguientes pasos. 
1. Asignar las siguientes variables de entorno.
   
        export FLASK_APP=app.py

        export FLASK_DEBUG=1

        export FLASK_ENV=development

2. Instalar el servidor de aplicaciones Gunicorn

        pip3 install wheel

        pip3 install gunicorn

3. Probar que el servidor de aplicaciones Gunicorn funciones correctamente. Pare esto, se debe especificar dirección IP y puerto de escucha.

        sudo ufw allow 4001

        gunicorn --bind 0.0.0.0:4001 wsgi:app

    De estanera debería poder ver en consola que está se ha ejecutado correctamene. 

4. Desactivar el entorno virtual.

        deactivate

5. Crear archivo con extención .service

        sudo nano /etc/systemd/system/app.service

6. Poner lo siguiente y remplazar las rutas que correspondan. 

        [Unit]

        Description=Gunicorn instance to serve APP

        After=network.target


        [Service]

        User=ubuntu

        Group=www-data

        WorkingDirectory=/home/ubuntu/taller-api-flask-2

        Environment="PATH=/home/ubuntu/lab-flask/bin/"

        ExecStart=/home/ubuntu/lab-flask/bin/gunicorn --workers 1 --bind unix:app.sock -m 007 wsgi:app


        [Install]

        WantedBy=multi-user.target

7. El archivo de servicio de systemd está completo, guarde y cierre. Inicie el servicio Gunicorn creado y actívelo para que se cargue en el arranque:

        sudo systemctl start app
        
        sudo systemctl enable app
        

8. Verifique que el servicio está funcionando/

        sudo systemctl status app

9. Ahora de ejecutar y comprobar el funcionamiento de Nginx

        $ sudo apt install nginx


Verifique el firewall de Ubuntu y habilite el puerto de escucha de Nginx para solicitudes HTTP:

        sudo ufw app list

        sudo ufw allow 'Nginx HTTP'

        sudo systemctl status nginx

