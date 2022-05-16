
from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_required
from model.DAO import historialPuestos

historialPuestos = Blueprint("historialPuestos", __name__, static_folder="view", template_folder="controller")


@historialPuestos.route('/historialPuestos/consultarHistorialPuestos')
@login_required
def consultarHistorialPuestos():
    histPues = historialPuestos()
    return render_template('/historialPuestos/consultar.html', hp=histPues.consultaGeneral())


@historialPuestos.route('/historialPuestos/ver/<int:id>')
@login_required
def editarHistorialPuestos(id):
    histPues = historialPuestos()
    return render_template('/historialPuestos/editar.html', hs=histPues.consultaIndividual(id))


@historialPuestos.route('/historialPuestos/editandoHistorialPuesto', methods=['post'])
@login_required
def editandoHistorialPuestos():
    try:
        histPues = historialPuestos()
        histPues.idEmpleado = request.form['idEmpleado']
        histPues.idPuesto = request.form['idPuesto']
        histPues.idDepartamento = request.form['idDepartamento']
        histPues.fechaInicio = request.form['fechaInicio']
        histPues.fechaFin = request.form['fechaFin']
        histPues.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/formaspago/editar.html', hs=histPues())


@historialPuestos.route('/historialPuestos/eliminarHistorialPuestos/<int:id>')
@login_required
def eliminarHistorialPuestos(id):
    histPues = historialPuestos()
    histPues.eliminar(id)
    flash('Registro eliminado con exito')
    return render_template('/formaspago/consultar.html', hs=histPues.consultaGeneral())
