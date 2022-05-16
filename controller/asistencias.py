import json
import time
from _datetime import datetime

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user

from model.DAO import Asistencias, Empleados

asistencias = Blueprint("asistencias", __name__, static_folder="view", template_folder="controller")
curren_day = time.ctime()
@asistencias.route('/asistencias/consultarAsistencias')
@login_required
def consultarAsistencias():
    asistencia = Asistencias()
    return render_template('/asistencias/consultar.html', asist=asistencia.consultaGeneral())

@asistencias.route('/asistencias/fecha/<string:fecha>', methods=['GET'])
def consultarFecha(fecha, idEmpleado):
    asist = Asistencias()
    return json.dumps(asist.consultarFecha(fecha, current_user.idEmpleado))

@asistencias.route('/asistencias/guardandoAsistencia', methods=['GET', 'POST'])
@login_required
def guardandoAsistencia():
    try:
        fecha_actual = datetime.today().strftime('%Y-%m-%d')
        dia_actual = time.ctime()
        dia_actual = dia_actual.split()
        asistencia = Asistencias()
        if asistencia.consultarFecha(fecha_actual, current_user.idEmpleado):
            ass = asistencia.consultarFecha(fecha_actual, current_user.idEmpleado)
            asistencia.idAsistencia = ass.idAsistencia
            asistencia.horaSalida = dia_actual[3]
            asistencia.actualizar()
        else:
            asistencia.fecha = fecha_actual
            asistencia.horaEntrada = dia_actual[3]
            asistencia.dia = dia_actual[0]
            asistencia.idEmpleado = current_user.idEmpleado
            asistencia.insertar()
            flash('Asistencia registrada exitosamente')
    except:
        flash('Error al registrar asistencia')
    return redirect(url_for('asistencias.consultarAsistencias'))


@asistencias.route('/asistencias/ver/<int:id>')
@login_required
def editarAsistencia(id):
    asistencia = Asistencias()
    empleados = Empleados()
    return render_template('/asistencias/editar.html', asist=asistencia.consultaIndividual(id), emp=empleados.consultaGeneral())

@asistencias.route('/asistencias/editandoAsistencia', methods=['POST'])
@login_required
def editandoAsistencia():
    try:
        asistencia = Asistencias()
        asistencia.idAsistencia = request.form['idAsistencia']
        asistencia.fecha = request.form['fecha']
        asistencia.horaEntrada = request.form['horaEntrad']
        asistencia.horaSalida = request.form['horaSalid']
        asistencia.dia = request.form['dia']
        asistencia.idEmpleado = request.form['idEmpleado']
        asistencia.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return redirect(url_for('asistencias.consultarAsistencias'))

@asistencias.route('/asistencias/eliminarAsistencia/<int:id>')
@login_required
def eliminarAsistencia(id):
    asistencia = Asistencias()
    asistencia.idAsistencia = id
    asistencia.eliminar(id)
    flash('Registro de asistencia eliminado con exito')
    return redirect(url_for('asistencias.consultarAsistencias'))
