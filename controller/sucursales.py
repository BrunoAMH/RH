from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_required
from model.DAO import Sucursales, Ciudades

sucursales = Blueprint("sucursales", __name__, static_folder="view", template_folder="controller")


@sucursales.route('/sucursales/consultarSucursales')
@login_required
def consultarSucursales():
    sucursal = Sucursales()
    ciudad = Ciudades()
    return render_template('/sucursales/consultar.html', sucu=sucursal.consultaGeneral(), ciud=ciudad.consultaGeneral())


@sucursales.route('/sucursales/registrarSucursales')
@login_required
def registrarSucursales():
    ciudad = Ciudades()
    return render_template('/sucursales/nuevo.html', ciud=ciudad.consultaGeneral())


@sucursales.route('/sucursales/guardandoSucursales', methods=['post'])
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
    return redirect('registrarSucursales')


@sucursales.route('/sucursales/ver/<int:id>')
@login_required
def editarSucursales(id):
    sucursal = Sucursales()
    ciudad = Ciudades()
    return render_template('/sucursales/editar.html', sucu=sucursal.consultaIndividual(id),
                           ciud=ciudad.consultaGeneral())


@sucursales.route('/sucursales/editandoSucursales', methods=['post'])
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


@sucursales.route('/sucursales/eliminarSucursales/<int:id>')
@login_required
def eliminarSucursales(id):
    sucursal = Sucursales()
    ciudad = Ciudades()
    sucursal.idSucursal = id
    sucursal.estatus = 'I'
    sucursal.actualizar()
    flash('Registro de sucursal eliminado con exito')
    return render_template('/sucursales/consultar.html', sucu=sucursal.consultaGeneral(), ciud=ciudad.consultaGeneral())
