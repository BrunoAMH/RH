from _ast import In
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, BLOB, CHAR, Float, ForeignKey, Date
from flask_login import UserMixin
from sqlalchemy.orm import relationship
db = SQLAlchemy()
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------EMPLEADOS---------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
class Empleados(UserMixin,db.Model):
    __tablename__ = 'empleados'
    idEmpleado = Column(Integer, primary_key=True)
    nombre = Column(String(60), nullable=False)
    apellidoPaterno = Column(String(60), nullable=False)
    apellidoMaterno = Column(String(60), nullable=False)
    sexo = Column(CHAR(1), nullable=False)
    fechaNacimiento = Column(Date, nullable=False)
    curp = Column(String(20), nullable=False)
    estadoCivil = Column(String(20), nullable=False)
    fechaContratacion = Column(Date, nullable=False)
    salarioDiario = Column(Float, nullable=False)
    nss = Column(String(11), nullable=False)
    diasVacaciones = Column(Integer, nullable=False)
    diasPermiso = Column(Integer, nullable=False)
    fotografia = Column(BLOB, nullable=False)
    direccion = Column(String(80), nullable=False)
    colonia = Column(String(50), nullable=False)
    codigoPostal = Column(String(5), nullable=False)
    escolaridad = Column(String(80), nullable=False)
    especialidad = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    contraseña = Column(String(20), nullable=False)
    tipo = Column(String(10), nullable=False)
    estatus = Column(CHAR(1), nullable=False)
    idDepartamento = Column(Integer, ForeignKey('departamentos.idDepartamento'))
    departamentos = relationship("Departamentos", backref="empleados", lazy='select')

    idPuesto = Column(Integer, ForeignKey('puestos.idPuesto'))
    puestos = relationship("Puestos", backref="empleados", lazy='select')

    idCiudad = Column(Integer, ForeignKey('ciudades.idCiudad'))
    ciudades = relationship("Ciudades", backref="empleados", lazy='select')

    idSucursal = Column(Integer, ForeignKey('sucursales.idSucursal'))
    sucursales= relationship("Sucursales", backref="empleados", lazy='select')

    idTurno = Column(Integer, ForeignKey('turnos.idTurno'))
    turnos = relationship("Turnos", backref="empleados", lazy='select')

    def consultarEmail(self, email):
        salida = {"estatus": "", "mensaje": ""}
        usuario = None
        usuario = self.query.filter(Empleados.email == email).first()
        if usuario != None:
            salida["estatus"] = "Error"
            salida["mensaje"] = "El correo " + email + " ya ha sido registrado. Intente con otro"
        else:
            salida["estatus"] = "Ok"
            salida["mensaje"] = "El correo " + email + " esta libre"
        return salida

    def consultarCurp(self, curp):
        salida = {"estatus": "", "mensaje": ""}
        usuario = None
        usuario = self.query.filter(Empleados.curp == curp).first()
        if usuario != None:
            salida["estatus"] = "Error"
            salida["mensaje"] = "La Curp " + curp + " ya ha sido registrado. Intente con otro"
        else:
            salida["estatus"] = "Ok"
            salida["mensaje"] = "La Curp " + curp + " esta libre"
        return salida

    def consultarNss(self, nss):
        salida = {"estatus": "", "mensaje": ""}
        usuario = None
        usuario = self.query.filter(Empleados.nss == nss).first()
        if usuario != None:
            salida["estatus"] = "Error"
            salida["mensaje"] = "El NSS " + nss + " ya ha sido registrado. Intente con otro"
        else:
            salida["estatus"] = "Ok"
            salida["mensaje"] = "El NSS " + nss + " esta libre"
        return salida


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

    def consultarImagen(self, id):
        return self.consultaIndividual(id).fotografia

    def consultarFoto(self, id):
        return self.consultaIndividual(id).fotografia

    def validar(self, correo, contrasena):
        empleado = None
        empleado = self.query.filter(Empleados.email == correo, Empleados.contraseña == contrasena, Empleados.estatus =='A').first()
        return empleado

    def is_authenticated(self):
        return True

    def is_active(self):
        return self.estatus

    def is_admin(self):
        if self.tipo == 'Admin':
            return True
        else:
            return False

    def is_staff(self):
        if self.tipo == 'Staff':
            return True
        else:
            return False

    def is_empleado(self):
        if self.tipo == 'Empleado':
            return True
        else:
            return False

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.idEmpleado
#-----------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------ESTADOS----------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

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
#-----------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------PUESTOS----------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------TURNOS-----------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
class Turnos(db.Model):
    __tablename__ = 'turnos'
    idTurno = Column(Integer, primary_key=True)
    nombre = Column(String(20), nullable=False)
    horaInicio = Column(Date, nullable=False)
    horaFin = Column(Date, nullable=False)
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
#-----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------PERCEPCIONES-------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
class Percepciones(db.Model):
    __tablename__ = 'percepciones'
    idPercepcion = Column(Integer, primary_key=True)
    nombre = Column(String(30), nullable=False)
    descripcion = Column(String(80), nullable=False)
    diasPagar = Column(Integer, nullable=False)

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
#-----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------DEDUCCIONES--------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
class Deducciones(db.Model):
    __tablename__ = 'deducciones'
    idDeduccion = Column(Integer, primary_key=True)
    nombre = Column(String(30), nullable=False)
    descripcion = Column(String(80), nullable=False)
    porcentaje = Column(Float, nullable=False)

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
#-----------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------PERIODOS---------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
class Periodos(db.Model):
    __tablename__ = 'periodos'
    idPeriodo = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    fechaInicio = Column(Date, nullable=False)
    fechaFin = Column(Date, nullable=False)
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
#-----------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------FORMAS DE PAGO------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
class FormasPago(db.Model):
    __tablename__ = 'formaspago'
    idFormaPago = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
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
#-----------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------CIUDADES---------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
class Ciudades(db.Model):
    __tablename__ = 'ciudades'
    idCiudad = Column(Integer, primary_key=True)
    nombre = Column(String(60), nullable=False)
    idEstado = Column(Integer, ForeignKey('estados.idEstado'))
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
#-----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------DEPARTAMENTOS------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
class Departamentos(db.Model):
    __tablename__ = 'departamentos'
    idDepartamento = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
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
#-----------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------SUCURSALES-------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
class Sucursales(db.Model):
    __tablename__ = 'sucursales'
    idSucursal = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    telefono = Column(String(10), nullable=False)
    direccion = Column(String(80), nullable=False)
    colonia = Column(String(50), nullable=False)
    codigopostal = Column(String(5), nullable=False)
    presupuesto = Column(Float, nullable=False)
    estatus = Column(CHAR(1), nullable=False)
    idCiudad = Column(Integer, ForeignKey('ciudades.idCiudad'))


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

#-----------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------DocumentacionEmpleado-------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
class DocumentacionEmpleado(db.Model):
    __tablename__ = 'documentacionempleado'
    idDocumento = Column(Integer, primary_key=True)
    nombre = Column(String(60), nullable=False)
    fechaEntrega = Column(Date, nullable=False)
    documento = Column(BLOB, nullable=False)
    idEmpleado = Column(Integer, ForeignKey('empleados.idEmpleado'))


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

    def consultarImagen(self, id):
        return self.consultaIndividual(id).documento

    def consultarFoto(self, id):
        return self.consultaIndividual(id).documento