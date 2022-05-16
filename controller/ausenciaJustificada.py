from _datetime import datetime

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from model.DAO import AusenciaJustificada, Empleados

asistenciaJustificada = Blueprint("asistenciaJustificada", __name__, static_folder="view", template_folder="controller")

@asistenciaJustificada.route('/ausenciaJustificada/consultarAusenciaJustificada')
@login_required
def consultarAusenciaJustificada():
    ausencia = AusenciaJustificada()
    empleados = Empleados()
    if current_user.is_admin():
        return render_template('/ausenciaJustificada/consultarUsuarios.html', aus=ausencia.consultaGeneral(),
                               emp=empleados.consultaGeneral())
    else:
        return render_template('/ausenciaJustificada/consultar.html', aus=ausencia.consultaGeneral(),
                               emp=empleados.consultaGeneral())

@asistenciaJustificada.route('/ausenciaJustificada/registrarAusenciaJustificada')
@login_required
def registrarAusenciaJustificada():
    empl = Empleados()
    return render_template('/ausenciaJustificada/nuevo.html', emp=empl.consultaGeneral())


@asistenciaJustificada.route('/ausenciaJustificada/consultarImagen/<int:id>')
def consultarImagenAusenciaJustificada(id):
    ausencia = AusenciaJustificada()
    return ausencia.consultarImagen(id)


@asistenciaJustificada.route('/ausenciaJustificada/guardandoAusenciaJustificada', methods=['post'])
@login_required
def guardandoAusenciaJustificada():
    try:
        ausencia = AusenciaJustificada()
        ausencia.fechaSolicitud = request.form['fechaSolicitud']
        ausencia.fechaInicio = request.form['fechaInicio']
        ausencia.fechaFin = request.form['fechaFin']
        ausencia.tipo = request.form['tipo']
        ausencia.idEmpleadoSolicita = request.form['idEmpleadoSolicita']
        ausencia.idEmpleadoAutoriza = request.form['idEmpleadoAutoriza']
        ausencia.evidencia = request.files['evidencia'].stream.read()
        ausencia.estatus = request.form['estatus']
        ausencia.motivo = request.form['motivo']
        ausencia.insertar()
        flash('Ausencia Justificada registrada exitosamente')
        return redirect(url_for('registrarAusenciaJustificada'))
    except:
        flash('!Error al guardar!')
    return render_template('/ausenciaJustificada/nuevo.html', aus=ausencia)

@asistenciaJustificada.route('/ausenciaJustificada/ver/<int:id>')
@login_required
def editarAusenciaJustificada(id):
    ausencia = AusenciaJustificada()
    empl = Empleados()
    return render_template('/ausenciaJustificada/editar.html', aus=ausencia.consultaIndividual(id),
                           emp=empl.consultaGeneral())


@asistenciaJustificada.route('/ausenciaJustificada/editandoAusenciaJustificada', methods=['post'])
@login_required
def editandoAusenciaJustificada():
    try:
        ausencia = AusenciaJustificada()
        ausencia.idAusencia = request.form['idAusencia']
        ausencia.fechaSolicitud = request.form['fechaSolicitud']
        ausencia.fechaInicio = request.form['fechaInicio']
        ausencia.fechaFin = request.form['fechaFin']
        ausencia.tipo = request.form['tipo']
        ausencia.idEmpleadoSolicita = request.form['idEmpleadoSolicita']
        ausencia.idEmpleadoAutoriza = request.form['idEmpleadoAutoriza']
        evidencias = request.files['evidencia'].stream.read()
        if evidencias:
            ausencia.documento = evidencias
        ausencia.estatus = request.form['estatus']
        ausencia.motivo = request.form['motivo']
        ausencia.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/ausenciaJustificada/editar.html', aus=ausencia)


@asistenciaJustificada.route('/ausenciaJustificada/eliminarAusenciaJustificada/<int:id>')
@login_required
def eliminarAusenciaJustificada(id):
    ausencia = AusenciaJustificada()
    ausencia.eliminar(id)
    flash('Registro de Ausencia Justificada eliminado con exito')
    return redirect(url_for('consultarAusenciaJustificada'))
