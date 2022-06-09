from _datetime import datetime

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from model.DAO import AusenciaJustificada, Empleados
import os
import pdfkit
from datetime import datetime
from datetime import timedelta
from jinja2 import Environment, FileSystemLoader
ruta= os.path.join(os.getcwd()+'/..')

#ruta = 'C:/Users/Espinoza/Documents/GitHub/RH'

asistenciaJustificada = Blueprint("asistenciaJustificada", __name__, static_folder="view", template_folder="controller")

@asistenciaJustificada.route('/docVacaciones/<int:id>/<int:e>/<int:e2>/<string:fechaFin>/<int:dias>')
def docVacaciones(id,e,e2,fechaFin,dias):
    env = Environment(loader=FileSystemLoader("../static"))
    template = env.get_template("docs/Formato-Vacaciones.html")
    permiso = AusenciaJustificada()
    empleado = Empleados()
    empleado2 = Empleados()
    permiso = permiso.consultaIndividual(id)
    empleado = empleado.consultaIndividual(e)
    empleado2 = empleado2.consultaIndividual(e2)
    date_object1 = datetime.strptime(fechaFin, "%Y-%m-%d").date()
    hace_una_semana = date_object1 + timedelta(days=1)
    Dias_Pedidos =dias

    datos={
        'permiso': permiso,
        'empleado': empleado,
        'empleado2': empleado2,
        'fecha_incorporacion': hace_una_semana,
        'dias': Dias_Pedidos

    }
    html = template.render(datos)
    file = open(ruta + '/static/docs/Formato-VacacionesTMP.html',"w")
    file.write(html)
    file.close()
    pdfkit.from_file(ruta + '\static\docs\Formato-VacacionesTMP.html',ruta+'\static\docs\Formato-Vacaciones.pdf')
    pdf = open(ruta+'\static\docs\Formato-Vacaciones.pdf',"rb")
    doc = pdf.read()
    pdf.close()
    #os.remove(ruta + '\static\docs\Formato-VacacionesTMP.html')
    #os.remove(ruta+'\Static\docs\Formato-Vacaciones.pdf')
    return doc

@asistenciaJustificada.route('/docPermisos/<int:id>/<int:e>/<int:e2>/<string:fechaFin>/<int:dias>')
def docPermisos(id,e,e2,fechaFin,dias):
    env = Environment(loader=FileSystemLoader("../static"))
    template = env.get_template("docs/Formato-Permisos.html")
    permiso = AusenciaJustificada()
    empleado = Empleados()
    empleado2 = Empleados()
    permiso = permiso.consultaIndividual(id)
    empleado = empleado.consultaIndividual(e)
    empleado2 = empleado2.consultaIndividual(e2)
    date_object1 = datetime.strptime(fechaFin, "%Y-%m-%d").date()
    hace_una_semana = date_object1 + timedelta(days=1)
    Dias_Pedidos =dias

    datos={
        'permiso': permiso,
        'empleado': empleado,
        'empleado2': empleado2,
        'fecha_incorporacion': hace_una_semana,
        'dias': Dias_Pedidos

    }
    html = template.render(datos)
    file = open(ruta + '/static/docs/Formato-PermisosTMP.html',"w")
    file.write(html)
    file.close()
    pdfkit.from_file(ruta + '\static\docs\Formato-PermisosTMP.html',ruta+'\static\docs\Formato-Permisos.pdf')
    pdf = open(ruta+'\static\docs\Formato-Permisos.pdf',"rb")
    doc = pdf.read()
    pdf.close()
    #os.remove(ruta + '\static\docs\Formato-PermisosTMP.html')
    #os.remove(ruta+'\Static\docs\Formato-Permisos.pdf')
    return doc


@asistenciaJustificada.route('/ausenciaJustificada/consultarAusenciaJustificada')
@login_required
def consultarAusenciaJustificada():
    ausencia = AusenciaJustificada()
    empleados = Empleados()
    if current_user.is_admin() or current_user.is_staff():
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
    if ausencia.consultaIndividual(id).estatus=="A":
        return render_template('/ausenciaJustificada/visualizar.html', aus=ausencia.consultaIndividual(id), emp=empl.consultaGeneral())
    else:
        if ausencia.consultaIndividual(id).idEmpleadoSolicita!=current_user.idEmpleado:
            return render_template('/ausenciaJustificada/editar.html', aus=ausencia.consultaIndividual(id),
                               emp=empl.consultaGeneral())
        else:
            return render_template('/ausenciaJustificada/visualizar.html', aus=ausencia.consultaIndividual(id),
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
        ausencia.estatus = request.form['estatus']
        dias = request.form['dias2']
        if ausencia.estatus=='A' and ausencia.tipo=="Vacaciones":
            ausencia.evidencia = docVacaciones(ausencia.idAusencia, ausencia.idEmpleadoSolicita, ausencia.idEmpleadoAutoriza, ausencia.fechaFin, dias)
        if ausencia.estatus == 'A' and ausencia.tipo == "Permiso":
            ausencia.evidencia = docPermisos(ausencia.idAusencia, ausencia.idEmpleadoSolicita,
                                             ausencia.idEmpleadoAutoriza, ausencia.fechaFin, dias)
        ausencia.motivo = request.form['motivo']
        ausencia.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/ausenciaJustificada/visualizar.html', aus=ausencia)



@asistenciaJustificada.route('/ausenciaJustificada/eliminarAusenciaJustificada/<int:id>')
@login_required
def eliminarAusenciaJustificada(id):
    ausencia = AusenciaJustificada()
    ausencia.eliminar(id)
    flash('Registro de Ausencia Justificada eliminado con exito')
    return redirect(url_for('consultarAusenciaJustificada'))
