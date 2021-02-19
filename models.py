from app import db, ma
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import relationship

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

    email = db.Column(db.String(50))

    nombre = db.Column(db.String(50))

    apellido = db.Column(db.String(50))

    email = db.Column(db.String(50))

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

    admin_id = db.Column(Integer, ForeignKey('usuario.id',ondelete='CASCADE'))

#Concurso Schema
class Concurso_Schema(ma.SQLAlchemyAutoSchema):
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

    # Usuario Schema


class Usuario_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario

    id = ma.auto_field()
    email = ma.auto_field()
    nombre = ma.auto_field()
    apellido = ma.auto_field()
    email = ma.auto_field()
    pssw = ma.auto_field()
    rol = ma.auto_field()
    concursos = ma.auto_field()

    # Participacion Schema


class Participacion_Schema(ma.Schema):
    class Meta:
        fields = ("id_usuario", "id_concurso", "urlRecord", "fechaPost", "estado")


usuario_schema = Usuario_Schema()
usuarios_schema = Usuario_Schema(many=True)