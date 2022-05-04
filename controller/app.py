import datetime
from urllib import request
from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for, abort
from flask_bootstrap import Bootstrap
from flask_login import current_user, login_user, logout_user, login_manager, login_required, LoginManager
from model.DAO import db, Empleados, Puestos, Turnos, Ciudades, Percepciones, Deducciones, Periodos, FormasPago, \
    Sucursales, Departamentos, DocumentacionEmpleado, Estados
from estados import estados
from ciudades import ciudades
from puestos import puestos
from departamentos import departamentos
from turnos import turnos
from sucursales import sucursales
from periodos import periodos
from formasPago import formasPago
from percepciones import percepciones
from deducciones import deducciones
from documentacion import documentacion
import json
app = Flask(__name__, template_folder='../view', static_folder='../static')
#---------------------Conexion ARMANDO-----------------------------------------
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:Cocacola079*+@localhost/rh'
#---------------------Conexion BRUNO-------------------------------------------
#app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:Banano2805@127.0.0.1/rh'
#---------------------Conexion Espinoza-----------------------------------------
#app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/rh'

#------------------------------------------------------------------------------
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='cl4v3'
login_manager=LoginManager()

app.register_blueprint(estados)
app.register_blueprint(ciudades)
app.register_blueprint(puestos)
app.register_blueprint(departamentos)
app.register_blueprint(turnos)
app.register_blueprint(sucursales)
app.register_blueprint(periodos)
app.register_blueprint(formasPago)
app.register_blueprint(percepciones)
app.register_blueprint(deducciones)
app.register_blueprint(documentacion)
Bootstrap(app)

# ---------------------Conexion ARMANDO-----------------------------------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Cocacola079*+@localhost/rh'
# ---------------------Conexion BRUNO-------------------------------------------
# app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:Banano2805@127.0.0.1/rh'
# ---------------------Conexion Espinoza-----------------------------------------
# app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/rh'

# ------------------------------------------------------------------------------
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'cl4v3'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# ________________________________________________________________________________
# --------------------------------COMUNES-----------------------------------------
# ________________________________________________________________________________
@login_manager.user_loader
def load_user(id):
    return Empleados.query.get(int(id))


@app.route('/')
def login():
    return render_template('common/login.html')


@app.route('/index')
def inicio():
    return render_template('common/index.html')


# ________________________________________________________________________________
# --------------------------------EMPLEADOS---------------------------------------
# ________________________________________________________________________________
@app.route('/empleados/iniciandoSesion', methods=['post'])
def iniciandoSesion():
    correo = request.form['correo']
    contrasena = request.form['contrasena']
    empleado = Empleados()
    empleado = empleado.validar(correo, contrasena)
    if empleado != None:
        login_user(empleado)
        return redirect(url_for('inicio'))
    else:
        return render_template('common/login.html')


@app.route('/empleados/email/<string:email>', methods=['get'])
def consultarEmail(email):
    e = Empleados()
    return json.dumps(e.consultarEmail(email))


@app.route('/empleados/curp/<string:curp>', methods=['get'])
def consultarCurp(curp):
    e = Empleados()
    return json.dumps(e.consultarCurp(curp))


@app.route('/empleados/nss/<string:nss>', methods=['get'])
def consultarNss(nss):
    e = Empleados()
    return json.dumps(e.consultarNss(nss))


@app.route('/cerrarSesion')
@login_required
def cerrarSesion():
    logout_user()
    return redirect(url_for('login'))


@app.route('/empleados/consultarEmpleados')
@login_required
def consultarEmpleados():
    emplea = Empleados()
    departments = Departamentos()
    puesto = Puestos()
    ciuda = Ciudades()
    sucursa = Sucursales()
    turns = Turnos()
    return render_template('/empleados/consultar.html', emp=emplea.consultaGeneral(),
                           depa=departments.consultaGeneral(), pues=puesto.consultaGeneral(),
                           ciud=ciuda.consultaGeneral(), sucu=sucursa.consultaGeneral(), turn=turns.consultaGeneral())


@app.route('/empleados/consultarEmpleadosPersonal')
@login_required
def consultarEmpleadosPersonal():
    emplea = Empleados()
    return render_template('/empleados/consultarPersonal.html', emp=emplea.consultaGeneral())


@app.route('/empleados/consultarEmpleadosDiaspermiso')
@login_required
def consultarEmpleadosDiaspermiso():
    emplea = Empleados()
    departments = Departamentos()
    puesto = Puestos()
    ciuda = Ciudades()
    sucursa = Sucursales()
    turns = Turnos()
    return render_template('/empleados/consultarDiaspermiso.html', emp=emplea.consultaGeneral(),
                           depa=departments.consultaGeneral(), pues=puesto.consultaGeneral(),
                           ciud=ciuda.consultaGeneral(), sucu=sucursa.consultaGeneral(), turn=turns.consultaGeneral())


@app.route('/empleados/consultarEmpleadosDomicilio')
@login_required
def consultarEmpleadosDomicilio():
    emplea = Empleados()
    departments = Departamentos()
    puesto = Puestos()
    ciuda = Ciudades()
    sucursa = Sucursales()
    turns = Turnos()
    return render_template('/empleados/consultarDomicilio.html', emp=emplea.consultaGeneral(),
                           depa=departments.consultaGeneral(), pues=puesto.consultaGeneral(),
                           ciud=ciuda.consultaGeneral(), sucu=sucursa.consultaGeneral(), turn=turns.consultaGeneral())


@app.route('/empleados/consultarEmpleadosLaboral')
@login_required
def consultarEmpleadosLaboral():
    emplea = Empleados()
    departments = Departamentos()
    puesto = Puestos()
    ciuda = Ciudades()
    sucursa = Sucursales()
    turns = Turnos()
    return render_template('/empleados/consultarLaboral.html', emp=emplea.consultaGeneral(),
                           depa=departments.consultaGeneral(), pues=puesto.consultaGeneral(),
                           ciud=ciuda.consultaGeneral(), sucu=sucursa.consultaGeneral(), turn=turns.consultaGeneral())


@app.route('/empleados/consultarImagen/<int:id>')
def consultarImagenEmpleados(id):
    emplea = Empleados()
    return emplea.consultarImagen(id)


@app.route('/empleados/registrarEmpleados')
@login_required
def registrarEmpleados():
    department = Departamentos()
    puesto = Puestos()
    ciudad = Ciudades()
    sucursal = Sucursales()
    turno = Turnos()
    return render_template('/empleados/nuevo.html', depa=department.consultaGeneral(), pues=puesto.consultaGeneral(),
                           ciud=ciudad.consultaGeneral(), sucu=sucursal.consultaGeneral(), turn=turno.consultaGeneral())


@app.route('/empleados/guardandoEmpleados', methods=['post'])
@login_required
def guardandoEmpleados():
    emplea = Empleados()
    emplea.nombre = request.form['nombre']
    emplea.apellidoPaterno = request.form['apellidoPaterno']
    emplea.apellidoMaterno = request.form['apellidoMaterno']
    emplea.sexo = request.form['sexo']
    emplea.fechaNacimiento = request.form['fechaNacimiento']
    emplea.curp = request.form['curp']
    emplea.estadoCivil = request.form['estadoCivil']
    emplea.fechaContratacion = request.form['fechaContratacion']
    emplea.salarioDiario = request.form['salarioDiario']
    emplea.nss = request.form['nss']
    emplea.diasVacaciones = request.form['diasVacaciones']
    emplea.diasPermiso = request.form['diasPermiso']
    emplea.fotografia = request.files['fotografia'].stream.read()
    emplea.direccion = request.form['direccion']
    emplea.colonia = request.form['colonia']
    emplea.codigoPostal = request.form['codigoPostal']
    emplea.escolaridad = request.form['escolaridad']
    emplea.especialidad = request.form['especialidad']
    emplea.email = request.form['email']
    emplea.contraseña = request.form['contraseña']
    emplea.tipo = request.form['tipo']
    emplea.estatus = request.form['estatus']
    emplea.idDepartamento = request.form['idDepartament']
    emplea.idPuesto = request.form['idPuesto']
    emplea.idCiudad = request.form['idCiudad']
    emplea.idSucursal = request.form['idSucursal']
    emplea.idTurno = request.form['idTurno']
    emplea.insertar()
    flash('Empleado registrado exitosamente')
    return redirect(url_for('registrarEmpleados'))


@app.route('/empleados/ver/<int:id>')
@login_required
def editarEmpleados(id):
    emplea = Empleados()
    department = Departamentos()
    puesto = Puestos()
    ciudad = Ciudades()
    sucursal = Sucursales()
    turno = Turnos()
    return render_template('/empleados/editar.html', emp=emplea.consultaIndividual(id),
                           depa=department.consultaGeneral(), pues=puesto.consultaGeneral(),
                           ciud=ciudad.consultaGeneral(), sucu=sucursal.consultaGeneral(), turn=turno.consultaGeneral())


@app.route('/empleados/editandoEmpleados', methods=['post'])
@login_required
def editandoEmpleados():
    #try:
    emplea = Empleados()
    department = Departamentos()
    puesto = Puestos()
    ciudad = Ciudades()
    sucursal = Sucursales()
    return render_template('/sucursales/consultar.html', sucu=sucursal.consultaGeneral())

@app.route('/sucursales/nombre/<string:nombre>', methods=['get'])
def consultarNombreSucursales(nombre):
    e=Sucursales()
    return json.dumps(e.consultarNombreSucursales(nombre))

@app.route('/sucursales/registrarSucursales')
@login_required
def registrarSucursales():
    ciudad = Ciudades()
    return render_template('/sucursales/nuevo.html', ciud=ciudad.consultaGeneral())

@app.route('/sucursales/guardandoSucursales',methods=['post'])
@login_required
def guardandoSucursales():
    sucursal = Sucursales()
    sucursal.nombre = request.form['nombre']
    sucursal.telefono = request.form['telefono']
    sucursal.direccion = request.form['direccion']
    sucursal.colonia = request.form['colonia']
    sucursal.codigopostal = request.form['codigopostal']
    sucursal.presupuesto = request.form['presupuesto']
    sucursal.estatus = request.form['estatus']
    sucursal.idCiudad = request.form['idCiudad']
    sucursal.insertar()
    flash('Sucursal registrada exitosamente')
    return redirect(url_for('registrarSucursales'))

@app.route('/sucursales/ver/<int:id>')
@login_required
def editarSucursales(id):
    sucursal = Sucursales()
    ciudad = Ciudades()
    return render_template('/sucursales/editar.html', sucu=sucursal.consultaIndividual(id), ciud=ciudad.consultaGeneral())

@app.route('/sucursales/editandoSucursales',methods=['post'])
@login_required
def editandoSucursales():
    try:
        sucursal = Sucursales()
        sucursal.idSucursal = request.form['idSucursal']
        sucursal.nombre = request.form['nombre']
        sucursal.telefono = request.form['telefono']
        sucursal.direccion = request.form['direccion']
        sucursal.colonia = request.form['colonia']
        sucursal.codigopostal = request.form['codigopostal']
        sucursal.presupuesto = request.form['presupuesto']
        sucursal.estatus = request.form['estatus']
        sucursal.idCiudad = request.form['idCiudad']
        sucursal.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/sucursales/editar.html', sucu=sucursal)

@app.route('/sucursales/eliminarSucursales/<int:id>')
@login_required
def eliminarSucursales(id):
    sucursal = Sucursales()
    sucursal.eliminar(id)
    flash('Registro de Sucursales eliminado con exito')
    return redirect(url_for('consultarSucursales'))

#________________________________________________________________________________
#--------------------------------DocumentacionEmpleado----------------------------------------
#________________________________________________________________________________
@app.route('/documentacionEmpleado/consultarDocumentacionEmpleado')
@login_required
def consultarDocumentacionEmpleado():
    docemp = DocumentacionEmpleado()
    empleados = Empleados()
    if current_user.is_admin():
        return render_template('/documentacionEmpleado/consultarUsuarios.html', doc=docemp.consultaGeneral(),
                               emp=empleados.consultaGeneral())
    else:
        return render_template('/documentacionEmpleado/consultar.html', doc=docemp.consultaGeneral(),
                               emp=empleados.consultaGeneral())

@app.route('/documentacionEmpleado/registrarDocumentacionEmpleado')
@login_required
def registrarDocumentacionEmpleado():
    empl = Empleados()
    return render_template('/documentacionEmpleado/nuevo.html', emp=empl.consultaGeneral())


@app.route('/documentacionEmpleado/consultarImagen/<int:id>')
def consultarImagenDocumentacionEmpleado(id):
    docemp = DocumentacionEmpleado()
    return docemp.consultarImagen(id)


@app.route('/documentacionEmpleado/guardandoDocumentacionEmpleado', methods=['post'])
@login_required
def guardandoDocumentacionEmpleado():
    docemp = DocumentacionEmpleado()
    docemp.nombre = request.form['nombre']
    docemp.fechaEntrega = request.form['fechaEntrega']
    docemp.documento = request.files['documento'].stream.read()
    docemp.idEmpleado = request.form['idEmpleado']
    docemp.insertar()
    flash('Documentacion registrada exitosamente')
    return redirect(url_for('registrarDocumentacionEmpleado'))


@app.route('/documentacionEmpleado/ver/<int:id>')
@login_required
def editarDocumentacionEmpleado(id):
    docemp = DocumentacionEmpleado()
    empl = Empleados()
    return render_template('/documentacionEmpleado/editar.html', doc=docemp.consultaIndividual(id),
                           emp=empl.consultaGeneral())


@app.route('/documentacionEmpleado/editandoDocumentacionEmpleado', methods=['post'])
@login_required
def editandoDocumentacionEmpleado():
    try:
        docemp = DocumentacionEmpleado()
        docemp.idDocumento = request.form['idDocumento']
        docemp.nombre = request.form['nombre']
        docemp.fechaEntrega = request.form['fechaEntrega']
        docemp.documento = request.files['documento'].stream.read()
        docemp.idEmpleado = request.form['idEmpleado']
        docemp.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/documentacionEmpleado/editar.html', doc=docemp)


@app.route('/documentacionEmpleado/eliminarDocumentacionEmpleado/<int:id>')
@login_required
def eliminarDocumentacionEmpleado(id):
    docemp = DocumentacionEmpleado()
    docemp.eliminar(id)
    flash('Registro de Dcoumento eliminado con exito')
    return redirect(url_for('consultarSucursales'))


#________________________________________________________________________________
#--------------------------------Percepciones------------------------------------
#________________________________________________________________________________
@app.route('/percepciones/consultarPercepciones')
@login_required
def consultarPercepciones():
    perceps = Percepciones()
    return render_template('/percepciones/consultar.html', perce=perceps.consultaGeneral())

@app.route('/percepciones/registrarPercepciones')
@login_required
def registrarPercepciones():
    return render_template('/percepciones/nuevo.html')

@app.route('/percepciones/guardandoPercepciones',methods=['post'])
@login_required
def guardandoPercepciones():
    perce = Percepciones()
    perce.nombre = request.form['nombre']
    perce.descripcion = request.form['descripcion']
    perce.diasPagar = request.form['diasPagar']
    perce.insertar()
    flash('Percepciones registradas exitosamente')
    return redirect(url_for('registrarPercepciones'))

@app.route('/percepciones/ver/<int:id>')
@login_required
def editarPercepciones(id):
    perce = Percepciones()
    return render_template('/percepciones/editar.html', perceps=perce.consultaIndividual(id))

@app.route('/percepciones/editandoPercepciones',methods=['post'])
@login_required
def editandoPercepciones():
    try:
        perce = Percepciones()
        perce.idPercepcion = request.form['idPercepcion']
        perce.nombre = request.form['nombre']
        perce.descripcion = request.form['descripcion']
        perce.diasPagar = request.form['diasPagar']
        perce.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/percepciones/editar.html', perceps=perce)

@app.route('/percepciones/eliminarPerceociones/<int:id>')
@login_required
def eliminarPercepciones(id):
    perce = Percepciones()
    perce.eliminar(id)
    flash('Registro de Percepciones eliminado con exito')
    return redirect(url_for('consultarPercepciones'))
#________________________________________________________________________________
#--------------------------------Deducciones-------------------------------------
#________________________________________________________________________________
@app.route('/deducciones/consultarDeducciones')
@login_required
def consultarDeducciones():
    deductions = Deducciones()
    return render_template('/deducciones/consultar.html', deduc=deductions.consultaGeneral())

@app.route('/deducciones/registrarDeducciones')
@login_required
def registrarDeducciones():
    return render_template('/deducciones/nuevo.html')

@app.route('/deducciones/guardandoDeducciones',methods=['post'])
@login_required
def guardandoDeducciones():
    deduc = Deducciones()
    deduc.nombre = request.form['nombre']
    deduc.descripcion = request.form['descripcion']
    deduc.porcentaje = request.form['porcentaje']
    deduc.insertar()
    flash('Deducciones registradas exitosamente')
    return redirect(url_for('registrarDeducciones'))

@app.route('/deducciones/ver/<int:id>')
@login_required
def editarDeducciones(id):
    deduc = Deducciones()
    return render_template('/deducciones/editar.html', deductions=deduc.consultaIndividual(id))

@app.route('/deducciones/editandoDeducciones',methods=['post'])
@login_required
def editandoDeducciones():
    try:
        deduc = Deducciones()
        deduc.idDeduccion = request.form['idDeduccion']
        deduc.nombre = request.form['nombre']
        deduc.descripcion = request.form['descripcion']
        deduc.porcentaje = request.form['porcentaje']
        deduc.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/deducciones/editar.html', deductions=deduc)

@app.route('/deducciones/eliminarDeducciones/<int:id>')
@login_required
def eliminarDeducciones(id):
    deduc = Deducciones()
    deduc.eliminar(id)
    flash('Registro de Deducciones eliminado con exito')
    return redirect(url_for('consultarDeducciones'))
#________________________________________________________________________________
#--------------------------------Periodos----------------------------------------
#________________________________________________________________________________
@app.route('/periodos/consultarPeriodos')
@login_required
def consultarPeriodos():
    periodo = Periodos()
    return render_template('/periodos/consultar.html', peri=periodo.consultaGeneral())

@app.route('/periodos/registrarPeriodos')
@login_required
def registrarPeriodos():
    return render_template('/periodos/nuevo.html')

@app.route('/periodos/nombre/<string:nombre>', methods=['get'])
def consultarNombrePeriodos(nombre):
    e=Periodos()
    return json.dumps(e.consultarNombrePeriodos(nombre))

@app.route('/periodos/guardandoPeriodos',methods=['post'])
@login_required
def guardandoPeriodos():
    peri = Periodos()
    peri.nombre = request.form['nombre']
    peri.fechaInicio = request.form['fechaInicio']
    peri.fechaFin = request.form['fechaFin']
    peri.estatus = request.form['estatus']
    peri.insertar()
    flash('Periodo registrado exitosamente')
    return redirect(url_for('registrarPeriodos'))

@app.route('/periodos/ver/<int:id>')
@login_required
def editarPeriodos(id):
    peri = Periodos()
    return render_template('/periodos/editar.html', periodo=peri.consultaIndividual(id))

@app.route('/periodos/editandoPeriodos',methods=['post'])
@login_required
def editandoPeriodos():
    try:
        peri = Periodos()
        peri.idPeriodo = request.form['idPeriodo']
        peri.nombre = request.form['nombre']
        peri.fechaInicio = request.form['fechaInicio']
        peri.fechaFin = request.form['fechaFin']
        peri.estatus = request.form['estatus']
        peri.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/periodos/editar.html', periodo=peri)

@app.route('/periodos/eliminarPeriodos/<int:id>')
@login_required
def eliminarPeriodos(id):
    peri = Periodos()
    peri.eliminar(id)
    flash('Periodo eliminado con exito')
    return redirect(url_for('consultarPeriodos'))


#________________________________________________________________________________
#--------------------------------Formas Pago-------------------------------------
#________________________________________________________________________________

@app.route('/formaspago/consultarFormasPago')
@login_required
def consultarFormasPago():
    formaspa = FormasPago()
    return render_template('/formaspago/consultar.html', fop=formaspa.consultaGeneral())
    turno = Turnos()
    emplea.idEmpleado = request.form['idEmpleado']
    emplea.nombre = request.form['nombre']
    emplea.apellidoPaterno = request.form['apellidoPaterno']
    emplea.apellidoMaterno = request.form['apellidoMaterno']
    emplea.sexo = request.form['sexo']
    emplea.fechaNacimiento = request.form['fechaNacimiento']
    emplea.curp = request.form['curp']
    emplea.estadoCivil = request.form['estadoCivil']
    emplea.fechaContratacion = request.form['fechaContratacion']
    emplea.salarioDiario = request.form['salarioDiario']
    emplea.nss = request.form['nss']
    emplea.diasVacaciones = request.form['diasVacaciones']
    emplea.diasPermiso = request.form['diasPermiso']
    emplea.fotografia = request.files['fotografia'].stream.read()
    emplea.direccion = request.form['direccion']
    emplea.colonia = request.form['colonia']
    emplea.codigoPostal = request.form['codigoPostal']
    emplea.escolaridad = request.form['escolaridad']
    emplea.especialidad = request.form['especialidad']
    emplea.email = request.form['email']
    emplea.contraseña = request.form['contrasena']
    emplea.tipo = request.form['tipo']
    emplea.estatus = request.form['estatus']
    emplea.idDepartamento = request.form['idDepartament']
    emplea.idPuesto = request.form['idPuesto']
    emplea.idCiudad = request.form['idCiudad']
    emplea.idSucursal = request.form['idSucursal']
    emplea.idTurno = request.form['idTurno']
    emplea.actualizar()
    flash('Datos actualizados con exito')
    #except:
        #flash('!Error al actualizar!')
    return render_template('/empleados/editar.html', emp=emplea.consultaIndividual(id),
                           depa=department.consultaGeneral(), pues=puesto.consultaGeneral(),
                           ciud=ciudad.consultaGeneral(), sucu=sucursal.consultaGeneral(), turn=turno.consultaGeneral())


@app.route('/formaspago/nombre/<string:nombre>', methods=['get'])
def consultarNombreFormasPago(nombre):
    e=FormasPago()
    return json.dumps(e.consultarNombreFormasPago(nombre))

@app.route('/formaspago/guardandoFormasPago',methods=['post'])
@login_required
def guardandoFormasPago():
    fop = FormasPago()
    fop.nombre = request.form['nombre']
    fop.estatus = request.form['estatus']
    fop.insertar()
    flash('Forma de Pago registradas exitosamente')
    return redirect(url_for('registrarFormasPago'))

@app.route('/formaspago/ver/<int:id>')

@app.route('/empleados/eliminarEmpleados/<int:id>')

@login_required
def eliminarEmpleados(id):
    emplea = Empleados()
    emplea.eliminar(id)
    flash('Registro de empleado eliminado con exito')
    return redirect(url_for('consultarEmpleados'))


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
