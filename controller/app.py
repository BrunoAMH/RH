import datetime
from urllib import request

from flask import Flask,render_template,request,flash,redirect,url_for,abort
from flask_bootstrap import Bootstrap
from flask_login import current_user,login_user,logout_user,login_manager,login_required,LoginManager
from model.DAO import db, Estados
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

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
