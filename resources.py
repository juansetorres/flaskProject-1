from flask import request
from flask_restful import Resource
import models
from app import db
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    create_refresh_token
)
from werkzeug.security import generate_password_hash, check_password_hash

class RecursoListarConcursos(Resource):
    def get(self):

        concursos = models.Concurso.query.all()

        return posts_schema.dump(concursos)
        
    def post(self):
        nuevo_concurso = models.Concurso(

            nombre=request.json['nombre'],

            url=request.json['url'],

            fechaIni=dateutil.parser.parse(request.json['fechaIni'], ignoretz=True),

            fechaFin=dateutil.parser.parse(request.json['fechaFin'], ignoretz=True),

            value=request.json['value'],

            guion=request.json['guion'],

            recomendaciones=request.json['recomendaciones']

        )

        db.session.add(nuevo_concurso)
        db.session.commit()

        return models.post_schema.dump(nuevo_concurso)

class RecursoRegistro(Resource):
    def post(self):
        usuario = models.Usuario.query.filter_by(email = request.json["email"]).first()

        if usuario: 
            return 'Ya existe un usuario con el correo dado', 200

        try:
            password_encrypted = generate_password_hash(request.json["pssw"], method='sha256')
            nuevo_usuario = models.Usuario(nombre = request.json["nombre"],  
                                    apellido = request.json["nombre"],
                                    email = request.json["email"], 
                                    pssw = password_encrypted, 
                                    rol="normal")

            db.session.add(nuevo_usuario)
            db.session.commit()

            data = models.usuario_schema.dump(nuevo_usuario)
            access_token = create_access_token(identity=data)
        
            return {
                'message': f'User {request.json["email"]} was created',
                'access_token': access_token,
                'data': data
            }

        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}

class RecursoAutenticacion(Resource):
    def post(self):
        usuario = models.Usuario.query.filter_by(email = request.json["email"]).first()
        if usuario and check_password_hash(usuario.pssw, request.json["pssw"]):
            data = models.usuario_schema.dump(usuario)
            access_token = create_access_token(identity=data)
            return { "success": True, "msg": "Login exitoso", "access_token": access_token}
        else:
            return { "error": True, "msg": "La combinación usuario/contraseña no está dentro de nuestros registros"}


# Recurso para los usuarios
class RecursoUsuarios(Resource):

    def get(self):
        post_schema = models.Usuario_Schema()

        posts_schema = models.Usuario_Schema(many=True)

        usuarios = models.Usuario.query.all()

        return posts_schema.dump(usuarios)

    def post(self):
        post_schema = models.Usuario_Schema()

        posts_schema = models.Usuario_Schema(many=True)
        nuevo_usuario = models.Usuario(
            nombre=request.json['nombre'],
            apellido=request.json['apellido'],
            pssw=request.json['pssw'],
            rol=request.json['rol']
        )
        db.session.add(nuevo_usuario)

        db.session.commit()

        return models.post_schema.dump(nuevo_usuario)


# Para crear un Concurso se ocupa el id del usuario y ver los usuarios
class RecursoUsuarioConcurso(Resource):
    def get(self, id):
        posts_schema = models.Usuario_Schema()

        posts_schema = models.Usuario_Schema(many=False)

        usuarios = models.Usuario.query.get_or_404(id)

        return posts_schema.dump(usuarios)

    def post(self, id):
        posts_schema = models.Concurso_Schema()

        posts_schema = models.Concurso_Schema(many=False)
        nuevo_concurso = models.Concurso(

            nombre=request.json['nombre'],

            url=request.json['url'],

            fechaIni=dateutil.parser.parse(request.json['fechaIni'], ignoretz=True),

            fechaFin=dateutil.parser.parse(request.json['fechaFin'], ignoretz=True),

            value=request.json['value'],

            guion=request.json['guion'],

            recomendaciones=request.json['recomendaciones'],

            admin_id=id

        )

        db.session.add(nuevo_concurso)

        db.session.commit()

        return models.posts_schema.dump(nuevo_concurso)


# Recurso para ver todos los concursos
class RecursoListaConcursos(Resource):

    def get(self):
        post_schema = models.Concurso_Schema()

        posts_schema = models.Concurso_Schema(many=True)

        concursos = models.Concurso.query.all()

        return models.posts_schema.dump(concursos)


# Recurso para ver todos los concursos
class RecursoUnUsuario(Resource):
    def get(self, id):
        post_schema = models.Usuario_Schema()

        posts_schema = models.Usuario_Schema(many=True)
        usuario = models.Usuario.query.get_or_404(id)

        return models.post_schema.dump(usuario)

    def put(self, id):
        post_schema = models.Usuario_Schema()

        posts_schema = models.Usuario_Schema(many=True)

        usuario = models.Usuario.query.get_or_404(id)

        if 'pssw' in request.json:
            usuario.pssw = request.json['pssw']

        if 'rol' in request.json:
            usuario.rol = request.json['rol']

        db.session.commit()

        return models.post_schema.dump(usuario)

    def delete(self, id):
        post_schema = models.Usuario_Schema()

        posts_schema = models.Usuario_Schema(many=True)

        usuario = models.Usuario.query.get_or_404(id)

        db.session.delete(usuario)

        db.session.commit()

        return '', 204


# Recurso para ver un solo concurso
class RecursoUnConcurso(Resource):

    def get(self, id):
        post_schema = models.Concurso_Schema()

        posts_schema = models.Concurso_Schema(many=True)

        concurso = models.Concurso.query.get_or_404(id)

        return models.post_schema.dump(concurso)

    def put(self, id):
        post_schema = models.Concurso_Schema()

        posts_schema = models.Concurso_Schema(many=True)

        concurso = models.Concurso.query.get_or_404(id)

        if 'url' in request.json:
            concurso.url = request.json['url']

        if 'guion' in request.json:
            concurso.guion = request.json['guion']

        if 'value' in request.json:
            concurso.guion = request.json['value']

        if 'fechaIni' in request.json:
            concurso.guion = dateutil.parser.parse(request.json['fechaIni'], ignoretz=True)
        if 'fechaFin' in request.json:
            concurso.guion = dateutil.parser.parse(request.json['fechaFin'], ignoretz=True)

        db.session.commit()

        return models.post_schema.dump(concurso)

    def delete(self, id_publicacion):

        concurso = models.Concurso.query.get_or_404(id_publicacion)

        db.session.delete(concurso)

        db.session.commit()

        return '', 204


# Recurso para manejar las participaciones de un usuario en un concurso
class RecursoParticipacion(Resource):
    def get(self,id_usuario,id_concurso):
        posts_schema = models.Participacion_Schema()

        posts_schema = models.Participacion_Schema(many=True)
        patric = models.Participacion.query.all()

        return models.posts_schema.dump(patric)

    def post(self,id_usuario,id_concurso):
        models.post_schema = models.Participacion_Schema()

        posts_schema = models.Participacion_Schema(many=True)
        nueva_participacion = models.Participacion(

            id_usuario=id_usuario,

            id_concurso=id_concurso,
            urlRecord=request.json['urlRecord'],
            fechaPost=  dateutil.parser.parse(request.json['fechaPost'], ignoretz=True),
            estado="sin leer"

        )

        db.session.add(nueva_participacion)
        db.session.commit()
        return models.post_schema.dump(nueva_participacion)