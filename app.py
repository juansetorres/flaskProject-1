from datetime import datetime
import dateutil.parser

from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ThisIsHardestThing'
app.config['JWT_SECRET_KEY'] = '!9m@S-dThyIlW[pHQbN^'

db = SQLAlchemy(app)
ma = Marshmallow(app)
Base = declarative_base()
jwt = JWTManager(app)
api = Api(app)

# Generating tables before first request is fetched
@app.before_first_request
def create_tables():
    db.create_all()

# Importing models and resources
import models
import resources

# Api Endpoints
api.add_resource(resources.RecursoListarConcursos, '/concursos')
api.add_resource(resources.RecursoRegistro, '/registro')
api.add_resource(resources.RecursoAutenticacion, '/login')

if __name__ == '__main__':

    app.run(debug=True)