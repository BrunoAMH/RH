from _datetime import datetime

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required
from model.DAO import Asistencias, Empleados

asistencias = Blueprint("asistencias", __name__, static_folder="view", template_folder="controller")

@asistencias.route('/asistencias/consultarAsistencias')
@login_required
def consultarAsistencias():
    asistencia = Asistencias()
    return render_template('/asistencias/consultar.html', asist=asistencia.consultaGeneral())


@asistencias.route('/asistencias/guardandoAsistencia', methods=['GET', 'POST'])
@login_required
def guardandoAsistencia():
    asistencia = Asistencias()
    asistencia.fecha = datetime.today().strftime('%Y-%m-%d')
    asistencia.horaEntrada = '07:00:00'
    asistencia.horaSalida = '15:00:00'
    asistencia.dia = 'Jueves'
    asistencia.idEmpleado = 4
    asistencia.insertar()
    flash('Asistencia registrado exitosamente')
    return redirect(url_for('asistencias.consultarAsistencias'))


@asistencias.route('/asistencias/ver/<int:id>')
@login_required
def editarAsistencia(id):
    asistencia = Asistencias()
    return render_template('/asistencias/editar.html', asist=asistencia.consultaIndividual(id))

@asistencias.route('/asistencias/editandoAsistencia', methods=['POST'])
@login_required
def editandoAsistencia():
    try:
        asistencia = Asistencias()
        asistencia.fecha = request.form['fecha']
        asistencia.horaEntrada = request.form['horaEntrada']
        asistencia.horaSalida = request.form['horaSalida']
        asistencia.dia = request.form['dia']
        asistencia.idEmpleado = Empleados.query.get(int(id))
        asistencia.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/asistencias/editar.html', asist=asistencia)

@asistencias.route('/asistencias/eliminarAsistencia/<int:id>')
@login_required
def eliminarAsistencia(id):
    asistencia = Asistencias()
    asistencia.idAsistencia = id
    asistencia.eliminar(id)
    flash('Registro de asistencia eliminado con exito')
    return redirect(url_for('asistencias.consultarAsistencias'))
