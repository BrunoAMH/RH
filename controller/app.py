import datetime
from urllib import request

from flask import Flask,render_template,request,flash,redirect,url_for,abort
from flask_bootstrap import Bootstrap
from flask_login import current_user,login_user,logout_user,login_manager,login_required,LoginManager
from model.DAO import db, Empleados, Estados, Puestos, Turnos, Ciudades, Percepciones, Deducciones, Periodos, FormasPago, Sucursales, Departamentos, DocumentacionEmpleado
app=Flask(__name__, template_folder='../view', static_folder='../static')
Bootstrap(app)
#---------------------Conexion ARMANDO-----------------------------------------
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:Cocacola079*+@localhost/rh'
#---------------------Conexion BRUNO-------------------------------------------
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:Banano2805@127.0.0.1/rh'
#------------------------------------------------------------------------------
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='cl4v3'
login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'
#________________________________________________________________________________
#--------------------------------COMUNES-----------------------------------------
#________________________________________________________________________________
@login_manager.user_loader
def load_user(id):
    return Empleados.query.get(int(id))

@app.route('/')
def login():
    return render_template('common/login.html')

@app.route('/index')
@login_required
def inicio():
    return render_template('common/index.html')
#________________________________________________________________________________
#--------------------------------EMPLEADOS---------------------------------------
#________________________________________________________________________________
@app.route('/empleados/iniciandoSesion', methods=['post'])
def iniciandoSesion():
    correo = request.form['correo']
    contrasena = request.form['contrasena']
    empleado = Empleados()
    empleado = empleado.validar(correo, contrasena)
    if empleado!= None:
        login_user(empleado)
        return render_template('common/index.html')
    else:
        return render_template('common/login.html')

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
    return render_template('/empleados/consultar.html', emp=emplea.consultaGeneral(),depa=departments.consultaGeneral(), pues=puesto.consultaGeneral(), ciud=ciuda.consultaGeneral(),sucu=sucursa.consultaGeneral(), turn = turns.consultaGeneral())

@app.route('/empleados/consultarImagen/<int:id>')
def consultarImagenEmpleados(id):
    emplea= Empleados()
    return emplea.consultarImagen(id)

@app.route('/empleados/registrarEmpleados')
@login_required
def registrarEmpleados():
    department = Departamentos()
    puesto = Puestos()
    ciudad = Ciudades()
    sucursal = Sucursales()
    turno = Turnos()
    return render_template('/empleados/nuevo.html', depa=department.consultaGeneral(), pues=puesto.consultaGeneral(), ciud=ciudad.consultaGeneral(), sucu=sucursal.consultaGeneral(), turn=turno.consultaGeneral())

@app.route('/empleados/guardandoEmpleados',methods=['post'])
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
    emplea.idDepartamento = request.form['idDepartamento']
    emplea.idPuesto = request.form['idPuesto']
    emplea.idCiudad = request.form['idCiudad']
    emplea.idSucursal = request.form['idSucursal']
    emplea.idTurno = request.form['idTurno']
    emplea.insertar()
    flash('Ciudad registrado exitosamente')
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
    return render_template('/empleados/editar.html',emp=emplea.consultaIndividual(id), depa=department.consultaGeneral(), pues=puesto.consultaGeneral(), ciud=ciudad.consultaGeneral(), sucu=sucursal.consultaGeneral(), turn=turno.consultaGeneral())

@app.route('/empleados/editandoEmpleados',methods=['post'])
@login_required
def editandoEmpleados():
    try:
        emplea = Empleados()
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
        emplea.contraseña = request.form['contraseña']
        emplea.tipo = request.form['tipo']
        emplea.estatus = request.form['estatus']
        emplea.idDepartamento = request.form['idDepartamento']
        emplea.idPuesto = request.form['idPuesto']
        emplea.idCiudad = request.form['idCiudad']
        emplea.idSucursal = request.form['idSucursal']
        emplea.idTurno = request.form['idTurno']
        emplea.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/empleados/editar.html', emp=emplea)

@app.route('/empleados/eliminarEmpleados/<int:id>')
@login_required
def eliminarEmpleados(id):
    emplea = Empleados()
    emplea.eliminar(id)
    flash('Registro del ciudades eliminado con exito')
    return redirect(url_for('consultarEmpleados'))



#________________________________________________________________________________
#--------------------------------ESTADOS-----------------------------------------
#________________________________________________________________________________
@app.route('/estados/consultarEstados')
@login_required
def consultarEstados():
    estates = Estados()
    return render_template('/estados/consultar.html', est=estates.consultaGeneral())

@app.route('/estados/registrarEstados')
@login_required
def registrarEstados():
    return render_template('/estados/nuevo.html')

@app.route('/estados/guardandoEstado',methods=['post'])
@login_required
def guardandoEstado():
    est = Estados()
    est.nombre = request.form['nombre']
    est.siglas = request.form['siglas']
    est.estatus = request.form['estatus']
    est.insertar()
    flash('Estado registrado exitosamente')
    return redirect(url_for('registrarEstados'))

@app.route('/estados/ver/<int:id>')
@login_required
def editarEstado(id):
    est = Estados()
    return render_template('/estados/editar.html', estates=est.consultaIndividual(id))

@app.route('/estados/editandoEstado',methods=['post'])
@login_required
def editandoEstado():
    try:
        est = Estados()
        est.idEstado = request.form['idEstado']
        est.nombre = request.form['nombreEstado']
        est.siglas = request.form['siglas']
        est.estatus = request.form['estatus']
        est.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/estados/editar.html', estates=est)

@app.route('/estados/eliminarEstado/<int:id>')
@login_required
def eliminarEstado(id):
    est = Estados()
    est.eliminar(id)
    flash('Registro del estado eliminado con exito')
    return redirect(url_for('consultarEstados'))

#________________________________________________________________________________
#--------------------------------DEPARTAMENTOS-----------------------------------------
#________________________________________________________________________________
@app.route('/departamentos/consultarDepartamentos')
@login_required
def consultarDepartamentos():
    departments = Departamentos()
    return render_template('/departamentos/consultar.html', depa=departments.consultaGeneral())

@app.route('/departamentos/registrarDepartamentos')
@login_required
def registrarDepartamentos():
    return render_template('/departamentos/nuevo.html')

@app.route('/departamentos/guardandoDepartamentos',methods=['post'])
@login_required
def guardandoDepartamentos():
    depa = Departamentos()
    depa.nombre = request.form['nombre']
    depa.estatus = request.form['estatus']
    depa.insertar()
    flash('Departamento registrado exitosamente')
    return redirect(url_for('registrarDepartamentos'))

@app.route('/departamentos/ver/<int:id>')
@login_required
def editarDepartamentos(id):
    depa = Departamentos()
    return render_template('/departamentos/editar.html', departments=depa.consultaIndividual(id))

@app.route('/departamentos/editandoDepartamentos',methods=['post'])
@login_required
def editandoDepartamentos():
    try:
        depa = Departamentos()
        depa.idDepartamento = request.form['idDepartamento']
        depa.nombre = request.form['nombre']
        depa.estatus = request.form['estatus']
        depa.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/departamentos/editar.html', departments=depa)

@app.route('/departamentos/eliminarDepartamentos/<int:id>')
@login_required
def eliminarDepartamentos(id):
    depa = Departamentos()
    depa.eliminar(id)
    flash('Registro de departamentos eliminado con exito')
    return redirect(url_for('consultarDepartamentos'))

#________________________________________________________________________________
#--------------------------------PUESTOS-----------------------------------------
#________________________________________________________________________________
@app.route('/puestos/consultarPuestos')
@login_required
def consultarPuestos():
    puesto = Puestos()
    return render_template('/puestos/consultar.html', pues=puesto.consultaGeneral())

@app.route('/puestos/registrarPuestos')
@login_required
def registrarPuestos():
    return render_template('/puestos/nuevo.html')

@app.route('/puestos/guardandoPuestos',methods=['post'])
@login_required
def guardandoPuestos():
    pues = Puestos()
    pues.nombre = request.form['nombre']
    pues.salarioMinimo = request.form['salarioMinimo']
    pues.salarioMaximo = request.form['salarioMaximo']
    pues.estatus = request.form['estatus']
    pues.insertar()
    flash('Puesto registrado exitosamente')
    return redirect(url_for('registrarPuestos'))

@app.route('/puestos/ver/<int:id>')
@login_required
def editarPuestos(id):
    pues = Puestos()
    return render_template('/puestos/editar.html', puesto=pues.consultaIndividual(id))

@app.route('/puestos/editandoPuestos',methods=['post'])
@login_required
def editandoPuestos():
    try:
        pues = Puestos()
        pues.idPuesto = request.form['idPuesto']
        pues.nombre = request.form['nombrePuesto']
        pues.salarioMinimo = request.form['salarioMinimo']
        pues.salarioMaximo = request.form['salarioMaximo']
        pues.estatus = request.form['estatus']
        pues.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/puestos/editar.html', puesto=pues)


@app.route('/puestos/eliminarPuestos/<int:id>')
@login_required
def eliminarPuestos(id):
    pues = Puestos()
    pues.eliminar(id)
    flash('Registro del puesto eliminado con exito')
    return redirect(url_for('consultarPuestos'))

#________________________________________________________________________________
#--------------------------------Turnos-----------------------------------------
#________________________________________________________________________________
@app.route('/turnos/consultarTurnos')
@login_required
def consultarTurnos():
    turns = Turnos()
    return render_template('/turnos/consultar.html', turn=turns.consultaGeneral())

@app.route('/turnos/registrarTurnos')
@login_required
def registrarTurnos():
    return render_template('/turnos/nuevo.html')

@app.route('/turnos/guardandoTurnos',methods=['post'])
@login_required
def guardandoTurnos():
    turn = Turnos()
    turn.nombre = request.form['nombre']
    turn.horaInicio = request.form['horaInicio']
    turn.horaFin = request.form['horaFin']
    turn.dias = request.form['dias']
    turn.insertar()
    flash('Turnos registrado exitosamente')
    return redirect(url_for('registrarTurnos'))

@app.route('/turnos/ver/<int:id>')
@login_required
def editarTurnos(id):
    turn = Turnos()
    return render_template('/turnos/editar.html', turns=turn.consultaIndividual(id))

@app.route('/turnos/editandoTurnos',methods=['post'])
@login_required
def editandoTurnos():
    try:
        turn = Turnos()
        turn.idTurno = request.form['idTurno']
        turn.nombre = request.form['nombre']
        turn.horaInicio = request.form['horaInicio']
        turn.horaFin = request.form['horaFin']
        turn.dias = request.form['dias']
        turn.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/turnos/editar.html', turns=turn)

@app.route('/turnos/eliminarTurnos/<int:id>')
@login_required
def eliminarTurnos(id):
    turn = Turnos()
    turn.eliminar(id)
    flash('Registro del turno eliminado con exito')
    return redirect(url_for('consultarTurnos'))
#________________________________________________________________________________
#--------------------------------Ciudades----------------------------------------
#________________________________________________________________________________
@app.route('/ciudades/consultarCiudades')
@login_required
def consultarCiudades():
    ciudad = Ciudades()
    estates = Estados()
    return render_template('/ciudades/consultar.html', ciud=ciudad.consultaGeneral(), est=estates.consultaGeneral())

@app.route('/ciudades/registrarCiudades')
@login_required
def registrarCiudades():
    estates = Estados()
    return render_template('/ciudades/nuevo.html', est=estates.consultaGeneral())

@app.route('/ciudades/guardandoCiudades',methods=['post'])
@login_required
def guardandoCiudades():
    ciudad = Ciudades()
    ciudad.nombre = request.form['nombre']
    ciudad.idEstado = request.form['idEstado']
    ciudad.estatus = request.form['estatus']
    ciudad.insertar()
    flash('Ciudad registrado exitosamente')
    return redirect(url_for('registrarCiudades'))

@app.route('/ciudades/ver/<int:id>')
@login_required
def editarCiudades(id):
    ciudad = Ciudades()
    estates = Estados()
    return render_template('/ciudades/editar.html', ciud=ciudad.consultaIndividual(id), est=estates.consultaGeneral())

@app.route('/ciudades/editandoCiudades',methods=['post'])
@login_required
def editandoCiudades():
    try:
        ciudad = Ciudades()
        ciudad.idCiudad = request.form['idCiudad']
        ciudad.nombre = request.form['nombre']
        ciudad.idEstado = request.form['idEstado']
        ciudad.estatus = request.form['estatus']
        ciudad.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/ciudades/editar.html', ciud=ciudad)

@app.route('/ciudades/eliminarCiudades/<int:id>')
@login_required
def eliminarCiudades(id):
    ciudad = Ciudades()
    ciudad.eliminar(id)
    flash('Registro del ciudades eliminado con exito')
    return redirect(url_for('consultarCiudades'))
#________________________________________________________________________________
#--------------------------------Sucursales----------------------------------------
#________________________________________________________________________________
@app.route('/sucursales/consultarSucursales')
@login_required
def consultarSucursales():
    sucursal = Sucursales()
    return render_template('/sucursales/consultar.html', sucu=sucursal.consultaGeneral())

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
    empl = Empleados()
    return render_template('/documentacionEmpleado/consultar.html', doc=docemp.consultaGeneral(), emp=empl.consultaGeneral())

@app.route('/documentacionEmpleado/registrarDocumentacionEmpleado')
@login_required
def registrarDocumentacionEmpleado():
    empl = Empleados()
    return render_template('/documentacionEmpleado/nuevo.html', emp=empl.consultaGeneral())




@app.route('/documentacionEmpleado/consultarImagen/<int:id>')
def consultarImagenDocumentacionEmpleado(id):
    docemp= DocumentacionEmpleado()
    return docemp.consultarImagen(id)


@app.route('/documentacionEmpleado/guardandoDocumentacionEmpleado',methods=['post'])
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
    return render_template('/documentacionEmpleado/editar.html', doc=docemp.consultaIndividual(id), emp=empl.consultaGeneral())

@app.route('/documentacionEmpleado/editandoDocumentacionEmpleado',methods=['post'])
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

@app.route('/formaspago/registrarFormasPago')
@login_required
def registrarFormasPago():
    return render_template('/formaspago/nuevo.html')

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
@login_required
def editarFormasPago(id):
    fop = FormasPago()
    return render_template('/formaspago/editar.html', formaspa=fop.consultaIndividual(id))

@app.route('/formaspago/editandoFormasPago',methods=['post'])
@login_required
def editandoFormasPago():
    try:
        fop = FormasPago()
        fop.idFormaPago = request.form['idFormaPago']
        fop.nombre = request.form['nombre']
        fop.estatus = request.form['estatus']
        fop.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/formaspago/editar.html', formaspa=fop)

@app.route('/formaspago/eliminarFormasPago/<int:id>')
@login_required
def eliminarFormasPago(id):
    peri = FormasPago()
    peri.eliminar(id)
    flash('forma de pago eliminada con exito')
    return redirect(url_for('consultarFormasPago'))

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
