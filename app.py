from flask import Flask, request
from datetime import datetime
import dateutil.parser

from flask_sqlalchemy import SQLAlchemy

from flask_marshmallow import Marshmallow

from flask_restful import Api, Resource


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    nombre = db.Column(db.String(50))

    apellido = db.Column(db.String(50))

    pssw = db.Column(db.String(50))


class Concurso(db.Model):

    id = db.Column(db.Integer, primary_key = True)

    nombre = db.Column( db.String(50) )

    url = db.Column( db.String(255) )

    fechaIni= db.Column(db.DateTime)

    fechaFin = db.Column(db.DateTime)

    value = db.Column(db.Integer)

    guion = db.Column( db.String(255) )

    recomendaciones = db.Column(db.String(255))


class Concurso_Schema(ma.Schema):
    class Meta:
        fields = ("id", "nombre", "url", "fechaIni", "fechaFin", "value", "guion", "recomendaciones")


post_schema = Concurso_Schema()

posts_schema = Concurso_Schema(many=True)

class Usuario_Schema(ma.Schema):
    class Meta:
        fields = ("id", "nombre", "apellido", "pssw")


post_schema = Usuario_Schema()

posts_schema = Usuario_Schema(many=True)

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