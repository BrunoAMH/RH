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
    
    def consultarPagina(self, pagina):
      paginacion = self.query.order_by(Empleados.idEmpleado.asc()).paginate(pagina, per_page=10, error_out=False)
      return paginacion


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
    
    def consultarPagina(self, pagina):
        paginacion = self.query.order_by(Estados.idEstado.asc()).paginate(pagina, per_page=10, error_out=False)
        return paginacion


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
    
    def consultarPagina(self, pagina):
        paginacion = self.query.order_by(Puestos.idPuesto.asc()).paginate(pagina, per_page=10, error_out=False)
        return paginacion
    
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
   
    def consultarPagina(self, pagina):
        paginacion = self.query.order_by(Turnos.idTurno.asc()).paginate(pagina, per_page=10, error_out=False)
        return paginacion

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
    
    def consultarNombrePercepciones(self, nombre):
        salida = {"estatus": "", "mensaje": ""}
        usuario = None
        usuario = self.query.filter(Percepciones.nombre == nombre).first()
        if usuario != None:
            salida["estatus"] = "Error"
            salida["mensaje"] = "El nombre " + nombre + " ya ha sido registrado. Intente con otro"
        else:
            salida["estatus"] = "Ok"
            salida["mensaje"] = "El nombre " + nombre + " esta libre"
            
    def consultarPagina(self, pagina):
        paginacion = self.query.order_by(Percepciones.idPercepcion.asc()).paginate(pagina, per_page=10, error_out=False)
        return paginacion

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
    
    def consultarNombreDeducciones(self, nombre):
        salida = {"estatus": "", "mensaje": ""}
        usuario = None
        usuario = self.query.filter(Deducciones.nombre == nombre).first()
        if usuario != None:
            salida["estatus"] = "Error"
            salida["mensaje"] = "El nombre " + nombre + " ya ha sido registrado. Intente con otro"
        else:
            salida["estatus"] = "Ok"
            salida["mensaje"] = "El nombre " + nombre + " esta libre"
        return salida

    def consultarPagina(self, pagina):
        paginacion = self.query.order_by(Deducciones.idDeduccion.asc()).paginate(pagina, per_page=10, error_out=False)
        return paginacion
    
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

    def consultarNombrePeriodos(self, nombre):
        salida = {"estatus": "", "mensaje": ""}
        usuario = None
        usuario = self.query.filter(Periodos.nombre == nombre).first()
        if usuario != None:
            salida["estatus"] = "Error"
            salida["mensaje"] = "El nombre " + nombre + " ya ha sido registrado. Intente con otro"
        else:
            salida["estatus"] = "Ok"
            salida["mensaje"] = "El Nombre " + nombre + " esta libre"
        return salida
    
    def consultarPagina(self, pagina):
        paginacion = self.query.order_by(Periodos.idPeriodo.asc()).paginate(pagina, per_page=10, error_out=False)
        return paginacion

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

    def consultarNombreFormasPago(self, nombre):
        salida = {"estatus": "", "mensaje": ""}
        usuario = None
        usuario = self.query.filter(FormasPago.nombre == nombre).first()
        if usuario != None:
            salida["estatus"] = "Error"
            salida["mensaje"] = "El nombre " + nombre + " ya ha sido registrado. Intente con otro"
        else:
            salida["estatus"] = "Ok"
            salida["mensaje"] = "El Nombre " + nombre + " esta libre"
        return salida
    
    def consultarPagina(self, pagina):
        paginacion = self.query.order_by(FormasPago.idFormaPago.asc()).paginate(pagina, per_page=10, error_out=False)
        return paginacion

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
    
    def consultarPagina(self, pagina):
        paginacion = self.query.order_by(Ciudades.idCiudad.asc()).paginate(pagina, per_page=10, error_out=False)
        return paginacion

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
    
    def consultarPagina(self, pagina):
        paginacion = self.query.order_by(Departamentos.idDepartamento.asc()).paginate(pagina, per_page=10, error_out=False)
        return paginacion

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

    def consultarNombreSucursales(self, nombre):
        salida = {"estatus": "", "mensaje": ""}
        usuario = None
        usuario = self.query.filter(Sucursales.nombre == nombre).first()
        if usuario != None:
            salida["estatus"] = "Error"
            salida["mensaje"] = "El nombre " + nombre + " ya ha sido registrado. Intente con otro"
        else:
            salida["estatus"] = "Ok"
            salida["mensaje"] = "El Nombre " + nombre + " esta libre"
        return salida

    def consultarPagina(self, pagina):
        paginacion = self.query.order_by(Sucursales.idSucursal.asc()).paginate(pagina, per_page=10, error_out=False)
        return paginacion

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
#------------------------------------------------------DocumentacionEmpleado--------------------------------------------
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

#-----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------ASISTENCIAS EMPLEADO-----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
class Asistencias(db.Model):
    __tablename__ = 'asistencias'
    idAsistencia = Column(Integer, primary_key=True)
    idEmpleado = Column(Integer, ForeignKey('empleados.idEmpleado'))
    fecha = Column(String(60), nullable=False)
    horaEntrada = Column(Date, nullable=False)
    horaSalida = Column(Date, nullable=False)
    dia = Column(Date, nullable=False)

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

    def consultarFecha(self, fecha, idEmp):
        return self.query.filter(Asistencias.fecha == fecha, Asistencias.idEmpleado == idEmp).first()


#-----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------HISTORIAL DE PUESTOS-----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
class historial_de_puestos(db.Model):
    __tablename__ = 'historialpuestos'
    idEmpleado = Column(Integer, primary_key=True)
    idPuesto = Column(Integer, primary_key=True)
    idDepartamento = Column(Integer, primary_key=True)
    fechaInicio = Column(Date, primary_key=True)
    fechaFin = Column(Date, nullable=False)


    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self, idEmpleado, idPuesto, idDepartamento, fechaInicio ):
        return self.query.filter(historial_de_puestos.idEmpleado == idEmpleado, historial_de_puestos.idPuesto == idPuesto,
                                 historial_de_puestos.idDepartamento == idDepartamento, historial_de_puestos.fechaInicio == fechaInicio).first()

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
#-------------------------------------------------AusenciaJustificada---------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
class AusenciaJustificada(db.Model):
    __tablename__ = 'ausenciajustificada'
    idAusencia = Column(Integer, primary_key=True)
    fechaSolicitud = Column(Date, nullable=False)
    fechaInicio = Column(Date, nullable=False)
    fechaFin = Column(Date, nullable=False)
    tipo = Column(String(100), nullable=False)
    evidencia = Column(BLOB, nullable=False)
    estatus = Column(CHAR(1), nullable=False)
    motivo = Column(String(100), nullable=False)
    idEmpleadoSolicita = Column(Integer, ForeignKey('empleados.idEmpleado'))
    idEmpleadoAutoriza = Column(Integer, ForeignKey('empleados.idEmpleado'))

    def consultarPagina(self, pagina):
        paginacion = self.query.order_by(AusenciaJustificada.idAusencia.asc()).paginate(pagina, per_page=10, error_out=False)
        return paginacion
    
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
        return self.consultaIndividual(id).evidencia

    def consultarFoto(self, id):
        return self.consultaIndividual(id).evidencia


# -----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------NOMINAS--------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
class Nominas(db.Model):
    __tablename__ = 'nominas'
    idNomina = Column(Integer, primary_key=True)
    fechaElaboracion = Column(Date, nullable=True)
    fechaPago = Column(Date, nullable=True)
    subtotal = Column(Float, nullable=True)
    retenciones = Column(Float, nullable=True)
    total = Column(Float, nullable=True)
    diasTrabajados = Column(Integer, nullable=True)
    estatus = Column(CHAR(1), nullable=True)
    idEmpleado = Column(Integer, ForeignKey('empleados.idEmpleado'))
    empleados = relationship("Empleados", backref="empleados", lazy='select')
    idFormaPago = Column(Integer, ForeignKey('formaspago.idFormaPago'))
    formasPago = relationship("FormasPago", backref="formaspago", lazy='select')
    idPeriodo = Column(Integer, ForeignKey('periodos.idPeriodo'))
    periodos = relationship("Periodos", backref="periodos", lazy='select')

    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def consultarUltimo(self):
        return db.session.query(Nominas).order_by(Nominas.idNomina.desc()).first()

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


# -----------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------NOMINAS-PERCEPCIONES--------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
class NominasPercepciones(db.Model):
    __tablename__ = 'nominaspercepciones'
    idNomina = Column(Integer, primary_key=True)
    idPercepcion = Column(Integer, primary_key=True)
    importe = Column(Float, nullable=False)


    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def insertar(self):
        db.session.add(self)
        db.session.commit()


# -----------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------NOMINAS-DEDUCCIONES---------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
class NominasDeducciones(db.Model):
    __tablename__ = 'nominasdeducciones'
    idNomina = Column(Integer, primary_key=True)
    idDeduccion = Column(Integer, primary_key=True)
    importe = Column(Float, nullable=False)

    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

        
