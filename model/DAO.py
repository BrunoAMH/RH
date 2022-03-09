from _ast import In
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,String,Boolean,BLOB,CHAR,Float,ForeignKey,Date
from flask_login import UserMixin
from sqlalchemy.orm import relationship

db=SQLAlchemy()

class Estados(db.Model):
    __tablename__ = 'estados'
    idEstado = Column(Integer, primary_key=True)
    nombre = Column(String(60), nullable=False)
    siglas = Column(String(10), nullable=False)
    estatus = Column(CHAR(1), nullable=False)

    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self, id):
        obj = self.consultaIndividual(id)
        db.session.delete(obj)
        db.session.commit()

class Puestos(db.Model):
    __tablename__ = 'puestos'
    idPuesto = Column(Integer, primary_key=True)
    nombre = Column(String(60), nullable=False)
    salarioMinimo = Column(Float, nullable=False)
    salarioMaximo = Column(Float, nullable=False)
    estatus = Column(CHAR(1), nullable=False)

    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self, id):
        obj = self.consultaIndividual(id)
        db.session.delete(obj)
        db.session.commit()

class Turnos(db.Model):
    __tablename__ = 'turnos'
    idTurno = Column(Integer, primary_key=True)
    nombre = Column(String(20), nullable=False)
    horaInicio = Column(String(20), nullable=False)
    horaFin = Column(String(20), nullable=False)
    dias = Column(String(30), nullable=False)

    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self, id):
        obj = self.consultaIndividual(id)
        db.session.delete(obj)
        db.session.commit()