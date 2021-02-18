from flask import Flask, request
from datetime import datetime
import dateutil.parser

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from flask_marshmallow import Marshmallow

from flask_restful import Api, Resource


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)
ma = Marshmallow(app)
Base = declarative_base()
#Participacion model
class Participacion(db.Model):
    id_usuario = db.Column(db.Integer, ForeignKey('usuario.id'),primary_key = True)

    id_concurso= db.Column(db.Integer, ForeignKey('concurso.id'),primary_key = True)

    urlRecord=db.Column(db.String(255))

    fechaPost = db.Column(db.DateTime)

    estado = db.Column(db.String(50))
#Usuario model
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    nombre = db.Column(db.String(50))

    apellido = db.Column(db.String(50))

    pssw = db.Column(db.String(50))

    rol = db.Column(db.String(50))

    concursos = db.relationship('Concurso', backref='usuario', lazy=True)

#concurso model
class Concurso(db.Model):

    id = db.Column(db.Integer, primary_key = True)

    nombre = db.Column( db.String(50) )

    url = db.Column( db.String(255) )

    fechaIni= db.Column(db.DateTime)

    fechaFin = db.Column(db.DateTime)

    value = db.Column(db.Integer)

    guion = db.Column( db.String(255) )

    recomendaciones = db.Column(db.String(255))

    admin_id = Column(Integer, ForeignKey('usuario.id'))

#Concurso Schema
class Concurso_Schema(ma.Schema):
    class Meta:
        model = Concurso

        include_fk = True

    id = ma.auto_field()
    nombre = ma.auto_field()
    url = ma.auto_field()
    fechaIni = ma.auto_field()
    fechaFin = ma.auto_field()
    value = ma.auto_field()
    guion = ma.auto_field()
    recomendaciones = ma.auto_field()


#Usuario Schema
class Usuario_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario

    id = ma.auto_field()
    nombre = ma.auto_field()
    apellido = ma.auto_field()
    pssw = ma.auto_field()
    rol = ma.auto_field()
    concursos = ma.auto_field()




#Participacion Schema
class Participacion_Schema(ma.Schema):
    class Meta:
        fields = ("id_usuario","id_concurso","urlRecord", "fechaPost", "estado")


api = Api(app)
#Recurso para los usuarios
class RecursoUsuarios(Resource):

    def get(self):
        post_schema = Usuario_Schema()

        posts_schema = Usuario_Schema(many=True)


        usuarios = Usuario.query.all()

        return posts_schema.dump(usuarios)
#Para crear un Concurso se ocupa el id del usuario y ver los usuarios
class RecursoUsuarioConcurso(Resource):
    post_schema = Usuario_Schema()

    post_schema = Usuario_Schema(many=True)

    def get(self,id):
        post_schema = Usuario_Schema()

        posts_schema = Usuario_Schema(many=True)

        usuarios = Usuario.query.get_or_404(id)

        return posts_schema.dump(usuarios)
    def post(self,id):
        post_schema = Concurso_Schema()

        posts_schema = Concurso_Schema(many=True)
        nuevo_concurso = Concurso(

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



        return post_schema.dump(nuevo_concurso)
#Recurso para ver todos los concursos
class RecursoListaConcursos(Resource):


    def get(self):
        post_schema = Concurso_Schema()

        posts_schema = Concurso_Schema(many=True)


        concursos = Concurso.query.all()

        return posts_schema.dump(concursos)




#URLS
api.add_resource(RecursoListaConcursos, '/concursos')
api.add_resource(RecursoUsuarios, '/usuarios')
api.add_resource(RecursoUsuarioConcurso, '/usuarios/<int:id>/concursos')





if __name__ == '__main__':

    app.run(debug=True)