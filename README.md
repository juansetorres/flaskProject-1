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
1. Hacer build del front, para ello entrar al cliente. 

        cd client

   Seguido a ello, ejecutar los scripts de react en npm.

        npm run build

   Y regresar de nuevo a la raiz del proyecto

        cd ..
        
2. Asignar las siguientes variables de entorno.
   
        export FLASK_APP=app.py

        export FLASK_DEBUG=1

        export FLASK_ENV=development

3. Instalar el servidor de aplicaciones Gunicorn

        pip3 install wheel

        pip3 install gunicorn

4. Probar que el servidor de aplicaciones Gunicorn funciones correctamente. Pare esto, se debe especificar dirección IP y puerto de escucha.

        sudo ufw allow 4001

        gunicorn --bind 0.0.0.0:4001 wsgi:app

    De estanera debería poder ver en consola que está se ha ejecutado correctamene. 

5. Desactivar el entorno virtual.

        deactivate

6. Crear archivo con extención .service

        sudo nano /etc/systemd/system/app.service

7. Poner lo siguiente y remplazar las rutas que correspondan. 

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

8. El archivo de servicio de systemd está completo, guarde y cierre. Inicie el servicio Gunicorn creado y actívelo para que se cargue en el arranque:

        sudo systemctl start app
        
        sudo systemctl enable app
        

9.  Verifique que el servicio está funcionando/

        sudo systemctl status app

10. Ahora de ejecutar y comprobar el funcionamiento de Nginx

        $ sudo apt install nginx

   Verifique el firewall de Ubuntu y habilite el puerto de escucha de Nginx para solicitudes HTTP:

        sudo ufw app list

        sudo ufw allow 'Nginx HTTP'

        sudo systemctl status nginx

11. Cree un nuevo archivo de configuración en el directorio sites-available de Nginx, llamado app para que se adecue al resto de esta guía:

        sudo nano /etc/nginx/sites-available/app

    Ponga y remplace 'ip_servidor' por la ip de la maquina virtual. 

        server {

                listen 80;

                server_name ip_servidor;


                location / {

                include proxy_params;

                proxy_pass http://unix:/home/ubuntu/taller-api-flask-2/app.sock;

                }
        }

12. Efectuar las ultimas configuraciones

    Guarde y cierre el al finalizar. Habilite la configuración de Nginx que acaba de crear, vincule el archivo al directorio sites-enabled​​​:


        sudo ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled


    Con el archivo en ese directorio, puede realizar una verificación en busca de errores de sintaxis:


        sudo nginx -t


    Si no se indican problemas, reinicie el proceso de Nginx para que lea la nueva configuración:


        sudo systemctl restart nginx


    Ya no se requiere acceso a través del puerto 5000, por lo que debe eliminar esta regla. Luego, podemos permitir el acceso completo al servidor de Nginx:


        sudo ufw delete allow 4001

        sudo ufw allow 'Nginx Full'

