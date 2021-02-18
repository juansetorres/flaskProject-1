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

class Participacion(db.Model):
    id_usuario = db.Column(db.Integer, ForeignKey('usuario.id'),primary_key = True)

    id_concurso= db.Column(db.Integer, ForeignKey('concurso.id'),primary_key = True)

    urlRecord=db.Column(db.String(255))

    fechaPost = db.Column(db.DateTime)

    estado = db.Column(db.String(50))

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    nombre = db.Column(db.String(50))

    apellido = db.Column(db.String(50))

    pssw = db.Column(db.String(50))

    rol = db.Column(db.String(50))

    children = relationship("Concurso")


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


class Concurso_Schema(ma.Schema):
    class Meta:
        fields = ("id", "nombre", "url", "fechaIni", "fechaFin", "value", "guion", "recomendaciones")


post_schema = Concurso_Schema()

posts_schema = Concurso_Schema(many=True)

class Usuario_Schema(ma.Schema):
    class Meta:
        fields = ("id", "nombre", "apellido", "pssw", "rol")

post_schema = Usuario_Schema()

posts_schema = Usuario_Schema(many=True)

class Participacion_Schema(ma.Schema):
    class Meta:
        fields = ("urlRecord", "fechaPost", "estado")


post_schema = Participacion_Schema()

posts_schema = Participacion_Schema(many=True)

api = Api(app)

class RecursoListarConcursos(Resource):

    def get(self):

        concursos = Concurso.query.all()

        return posts_schema.dump(concursos)
    def post(self):
        nuevo_concurso = Concurso(

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

        return post_schema.dump(nuevo_concurso)


api.add_resource(RecursoListarConcursos, '/concursos')




if __name__ == '__main__':

    app.run(debug=True)