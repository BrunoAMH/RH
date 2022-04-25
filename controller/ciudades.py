from flask import Blueprint, render_template, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required
from model.DAO import Estados, Ciudades

ciudades = Blueprint("ciudades", __name__, static_folder="view", template_folder="controller")


@ciudades.route('/ciudades/consultarCiudades')
@login_required
def consultarCiudades():
    #ciudad = Ciudades.query.join(Estados).paginate(1, 3, True)
    ciudad = Ciudades()
    estates = Estados()
    return render_template('/ciudades/consultar.html', ciud=ciudad.consultaGeneral(), est=estates.consultaGeneral())


@ciudades.route('/ciudades/registrarCiudades')
@login_required
def registrarCiudades():
    estates = Estados()
    return render_template('/ciudades/nuevo.html', est=estates.consultaGeneral())


@ciudades.route('/ciudades/guardandoCiudades', methods=['post'])
@login_required
def guardandoCiudades():
    ciudad = Ciudades()
    ciudad.nombre = request.form['nombre']
    ciudad.idEstado = request.form['idEstado']
    ciudad.estatus = request.form['estatus']
    ciudad.insertar()
    flash('Ciudad registrado exitosamente')
    return redirect('registrarCiudades')


@ciudades.route('/ciudades/ver/<int:id>')
@login_required
def editarCiudades(id):
    ciudad = Ciudades()
    estates = Estados()
    return render_template('/ciudades/editar.html', ciud=ciudad.consultaIndividual(id), est=estates.consultaGeneral())


@ciudades.route('/ciudades/editandoCiudades', methods=['post'])
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


@ciudades.route('/ciudades/eliminarCiudades/<int:id>')
@login_required
def eliminarCiudades(id):
    ciudad = Ciudades()
    estates = Estados()
    ciudad.idCiudad = id
    ciudad.estatus = 'I'
    ciudad.actualizar()
    flash('Registro de ciudad eliminado con exito')
    return render_template('/ciudades/consultar.html', ciud=ciudad.consultaGeneral(), est=estates.consultaGeneral())
