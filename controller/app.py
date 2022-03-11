import datetime
from urllib import request

from flask import Flask,render_template,request,flash,redirect,url_for,abort
from flask_bootstrap import Bootstrap
from flask_login import current_user,login_user,logout_user,login_manager,login_required,LoginManager
from model.DAO import db, Estados, Puestos, Turnos, Ciudades
app=Flask(__name__, template_folder='../view', static_folder='../static')
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:Cocacola079*+@localhost/rh'
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
    return render_template('/estados/editar.html', puest=pues.consultaIndividual(id))

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
    return render_template('/puestos/editar.html', puest=pues)


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
    return redirect(url_for('consultarEstados'))

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)

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

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
