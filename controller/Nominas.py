from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_required
from model.DAO import Nominas, Empleados, FormasPago, Periodos

nominas = Blueprint("nominas", __name__, static_folder="view", template_folder="controller")


@nominas.route('/nominas/consultarNominas')
@login_required
def consultarNominas():
    nominas = Nominas()
    return render_template('/nominas/consultar.html', nom=nominas.consultaGeneral())


@nominas.route('/nominas/registrarNominas')
@login_required
def registrarNominas():
    nominas = Nominas()
    return render_template('/nominas/nuevo.html', nom=nominas.consultaGeneral())


@nominas.route('/nominas/guardandoNomina', methods=['POST'])
@login_required
def guardandoNominas():
    nominas = Nominas()
    nominas.fechaElaboracion = request.form['fechaElaboracion']
    nominas.fechaPago = request.form['fechaPago']
    nominas.subtotal = request.form['subtotal']
    nominas.retenciones = request.form['subtotal']
    nominas.total = request.form['subtotal']
    nominas.insertar()
    flash('Ciudad registrado exitosamente')
    return redirect('registrarCiudades')


@nominas.route('/nominas/ver/<int:id>')
@login_required
def editarNominas(id):
    nominas = Nominas()
    return render_template('/nominas/editar.html', nom=nominas.consultaGeneral())


@nominas.route('/nominas/editandoNomina', methods=['POST'])
@login_required
def editandoNominas():
    try:
        nominas = Nominas()
        nominas.idNomina = request.form['idCiudad']
        nominas.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/nominas/editar.html', nom=nominas)


@nominas.route('/nominas/eliminarNominas/<int:id>')
@login_required
def eliminarCiudades(id):
    nominas = Nominas()
    nominas.idNomina = id
    nominas.estatus = 'I'
    nominas.actualizar()
    flash('Registro de nomina eliminado con exito')
    return render_template('/ciudades/consultar.html', nom=nominas.consultaGeneral())
