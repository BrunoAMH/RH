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


@app.route('/empleados/eliminarEmpleados/<int:id>')
@login_required
def eliminarEmpleados(id):
    emplea = Empleados()
    emplea.eliminar(id)
    flash('Registro del ciudades eliminado con exito')
    return redirect(url_for('consultarEmpleados'))


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
