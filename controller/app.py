import datetime
from urllib import request

from flask import Flask,render_template,request,flash,redirect,url_for,abort
from flask_bootstrap import Bootstrap
from flask_login import current_user,login_user,logout_user,login_manager,login_required,LoginManager
from model.DAO import db, Estados, Puestos, Turnos, Ciudades, Percepciones, Deducciones, Periodos, FormasPago
app=Flask(__name__, template_folder='../view', static_folder='../static')
Bootstrap(app)
#---------------------Conexion ARMANDO-----------------------------------------
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:Cocacola079*+@localhost/rh'
#---------------------Conexion BRUNO-------------------------------------------
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:Banano2805@127.0.0.1/rh'
#------------------------------------------------------------------------------
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='cl4v3'
#________________________________________________________________________________
#--------------------------------COMUNES-----------------------------------------
#________________________________________________________________________________

@app.route('/')
def login():
    return render_template('common/login.html')

@app.route('/index')
def inicio():
    return render_template('common/index.html')
#________________________________________________________________________________
#--------------------------------ESTADOS-----------------------------------------
#________________________________________________________________________________
@app.route('/estados/consultarEstados')
def consultarEstados():
    estates = Estados()
    return render_template('/estados/consultar.html', est=estates.consultaGeneral())

@app.route('/estados/registrarEstados')
def registrarEstados():
    return render_template('/estados/nuevo.html')

@app.route('/estados/guardandoEstado',methods=['post'])
def guardandoEstado():
    est = Estados()
    est.nombre = request.form['nombre']
    est.siglas = request.form['siglas']
    est.estatus = request.form['estatus']
    est.insertar()
    flash('Estado registrado exitosamente')
    return redirect(url_for('registrarEstados'))

@app.route('/estados/ver/<int:id>')
def editarEstado(id):
    est = Estados()
    return render_template('/estados/editar.html', estates=est.consultaIndividual(id))

@app.route('/estados/editandoEstado',methods=['post'])
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
def eliminarEstado(id):
    est = Estados()
    est.eliminar(id)
    flash('Registro del estado eliminado con exito')
    return redirect(url_for('consultarEstados'))

#________________________________________________________________________________
#--------------------------------PUESTOS-----------------------------------------
#__
@app.route('/puestos/consultarPuestos')
def consultarPuestos():
    puesto = Puestos()
    return render_template('/puestos/consultar.html', pues=puesto.consultaGeneral())

@app.route('/puestos/registrarPuestos')
def registrarPuestos():
    return render_template('/puestos/nuevo.html')

@app.route('/puestos/guardandoPuestos',methods=['post'])
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
def editarPuestos(id):
    pues = Puestos()
    return render_template('/puestos/editar.html', puesto=pues.consultaIndividual(id))

@app.route('/puestos/editandoPuestos',methods=['post'])
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
def eliminarPuestos(id):
    pues = Puestos()
    pues.eliminar(id)
    flash('Registro del puesto eliminado con exito')
    return redirect(url_for('consultarPuestos'))

#________________________________________________________________________________
#--------------------------------Turnos-----------------------------------------
#__
@app.route('/turnos/consultarTurnos')
def consultarTurnos():
    turns = Turnos()
    return render_template('/turnos/consultar.html', turn=turns.consultaGeneral())

@app.route('/turnos/registrarTurnos')
def registrarTurnos():
    return render_template('/turnos/nuevo.html')

@app.route('/turnos/guardandoTurnos',methods=['post'])
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
def editarTurnos(id):
    turn = Turnos()
    return render_template('/turnos/editar.html', turns=turn.consultaIndividual(id))

@app.route('/turnos/editandoTurnos',methods=['post'])
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
def eliminarTurnos(id):
    turn = Turnos()
    turn.eliminar(id)
    flash('Registro del turno eliminado con exito')
    return redirect(url_for('consultarTurnos'))


#________________________________________________________________________________
#--------------------------------Ciudades-----------------------------------------
#________________________________________________________________________________
@app.route('/ciudades/consultarCiudades')
def consultarCiudades():
    ciudad = Ciudades()
    return render_template('/ciudades/consultar.html', ciud=ciudad.consultaGeneral())

@app.route('/ciudades/registrarCiudades')
def registrarCiudades():
    estates = Estados()
    return render_template('/ciudades/nuevo.html', est=estates.consultaGeneral())

@app.route('/ciudades/guardandoCiudades',methods=['post'])
def guardandoCiudades():
    ciudad = Ciudades()
    ciudad.nombre = request.form['nombre']
    ciudad.idEstado = request.form['idEstado']
    ciudad.estatus = request.form['estatus']
    ciudad.insertar()
    flash('Ciudad registrado exitosamente')
    return redirect(url_for('registrarCiudades'))

@app.route('/ciudades/ver/<int:id>')
def editarCiudades(id):
    ciudad = Ciudades()
    estates = Estados()
    return render_template('/ciudades/editar.html', ciud=ciudad.consultaIndividual(id), est=estates.consultaGeneral())

@app.route('/ciudades/editandoCiudades',methods=['post'])
def editandoCiudades():
    try:
        ciudad = Ciudades()
        ciudad.idCiudad = request.form['idEstado']
        ciudad.nombre = request.form['nombre']
        ciudad.idEstado = request.form['idEstado']
        ciudad.estatus = request.form['estatus']
        ciudad.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/ciudades/editar.html', ciud=ciudad)

@app.route('/ciudades/eliminarCiudades/<int:id>')
def eliminarCiudades(id):
    ciudad = Ciudades()
    ciudad.eliminar(id)
    flash('Registro del ciudades eliminado con exito')
    return redirect(url_for('consultarCiudades'))


#________________________________________________________________________________
#--------------------------------Percepciones-----------------------------------------
#__

@app.route('/percepciones/consultarPercepciones')
def consultarPercepciones():
    perceps = Percepciones()
    return render_template('/percepciones/consultar.html', perce=perceps.consultaGeneral())

@app.route('/percepciones/registrarPercepciones')
def registrarPercepciones():
    return render_template('/percepciones/nuevo.html')

@app.route('/percepciones/guardandoPercepciones',methods=['post'])
def guardandoPercepciones():
    perce = Percepciones()
    perce.nombre = request.form['nombre']
    perce.descripcion = request.form['descripcion']
    perce.diasPagar = request.form['diasPagar']
    perce.insertar()
    flash('Percepciones registradas exitosamente')
    return redirect(url_for('registrarPercepciones'))

@app.route('/percepciones/ver/<int:id>')
def editarPercepciones(id):
    perce = Percepciones()
    return render_template('/percepciones/editar.html', perceps=perce.consultaIndividual(id))

@app.route('/percepciones/editandoPercepciones',methods=['post'])
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
def eliminarPercepciones(id):
    perce = Percepciones()
    perce.eliminar(id)
    flash('Registro de Percepciones eliminado con exito')
    return redirect(url_for('consultarPercepciones'))

#________________________________________________________________________________
#--------------------------------Deducciones-----------------------------------------
#__

@app.route('/deducciones/consultarDeducciones')
def consultarDeducciones():
    deductions = Deducciones()
    return render_template('/deducciones/consultar.html', deduc=deductions.consultaGeneral())

@app.route('/deducciones/registrarDeducciones')
def registrarDeducciones():
    return render_template('/deducciones/nuevo.html')

@app.route('/deducciones/guardandoDeducciones',methods=['post'])
def guardandoDeducciones():
    deduc = Deducciones()
    deduc.nombre = request.form['nombre']
    deduc.descripcion = request.form['descripcion']
    deduc.porcentaje = request.form['porcentaje']
    deduc.insertar()
    flash('Deducciones registradas exitosamente')
    return redirect(url_for('registrarDeducciones'))

@app.route('/deducciones/ver/<int:id>')
def editarDeducciones(id):
    deduc = Deducciones()
    return render_template('/deducciones/editar.html', deductions=deduc.consultaIndividual(id))

@app.route('/deducciones/editandoDeducciones',methods=['post'])
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
def eliminarDeducciones(id):
    deduc = Deducciones()
    deduc.eliminar(id)
    flash('Registro de Deducciones eliminado con exito')
    return redirect(url_for('consultarDeducciones'))

#________________________________________________________________________________
#--------------------------------Periodos-----------------------------------------
#__

@app.route('/periodos/consultarPeriodos')
def consultarPeriodos():
    periodo = Periodos()
    return render_template('/periodos/consultar.html', peri=periodo.consultaGeneral())

@app.route('/periodos/registrarPeriodos')
def registrarPeriodos():
    return render_template('/periodos/nuevo.html')

@app.route('/periodos/guardandoPeriodos',methods=['post'])
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
def editarPeriodos(id):
    peri = Periodos()
    return render_template('/periodos/editar.html', periodo=peri.consultaIndividual(id))

@app.route('/periodos/editandoPeriodos',methods=['post'])
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
def eliminarPeriodos(id):
    peri = Periodos()
    peri.eliminar(id)
    flash('Periodo eliminado con exito')
    return redirect(url_for('consultarPeriodos'))


#________________________________________________________________________________
#--------------------------------Formas Pago-----------------------------------------
#__

@app.route('/formaspago/consultarFormasPago')
def consultarFormasPago():
    formaspa = FormasPago()
    return render_template('/formaspago/consultar.html', fop=formaspa.consultaGeneral())

@app.route('/formaspago/registrarFormasPago')
def registrarFormasPago():
    return render_template('/formaspago/nuevo.html')

@app.route('/formaspago/guardandoFormasPago',methods=['post'])
def guardandoFormasPago():
    fop = FormasPago()
    fop.nombre = request.form['nombre']
    fop.estatus = request.form['estatus']
    fop.insertar()
    flash('Forma de Pago registradas exitosamente')
    return redirect(url_for('registrarFormasPago'))

@app.route('/formaspago/ver/<int:id>')
def editarFormasPago(id):
    fop = FormasPago()
    return render_template('/formaspago/editar.html', formaspa=fop.consultaIndividual(id))

@app.route('/formaspago/editandoFormasPago',methods=['post'])
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
def eliminarFormasPago(id):
    peri = FormasPago()
    peri.eliminar(id)
    flash('forma de pago eliminada con exito')
    return redirect(url_for('consultarFormasPago'))

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
