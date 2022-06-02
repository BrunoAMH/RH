
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required
from model.DAO import historial_de_puestos, Puestos, Departamentos, Empleados
from pymysql import OperationalError


historialPuestos = Blueprint("historialPuestos", __name__, static_folder="view", template_folder="controller")

@historialPuestos.route('/historialPuestos/consultar/<int:id>')
@login_required
def consultarHistorialPuestos(id):
    histPues = historial_de_puestos()
    emp = Empleados()
    puestos = Puestos()
    departamentos = Departamentos()
    return render_template('/historialPuestos/consultar.html', emp=emp.consultaGeneral(), hp=histPues.consultaGeneral(),
                           pues=puestos.consultaGeneral(), depa=departamentos.consultaGeneral(), id=id)


@historialPuestos.route('/historialPuestos/ver/<int:idEmp>/<int:idPues>/<int:idDep>/<fecha>')
@login_required
def editarHistorialPuestos(idEmp, idPues, idDep, fecha):
    histPues = historial_de_puestos()
    return render_template('/historialPuestos/editar.html', hp=histPues.consultaIndividual(idEmp, idPues, idDep, fecha))


@historialPuestos.route('/historialPuestos/editandoHistorialPuesto', methods=['POST'])
@login_required
def editandoHistorialPuestos():
    try:
        histPues = historial_de_puestos()
        histPues.idEmpleado = request.form['idEmpleado']
        histPues.idPuesto = request.form['idPuesto']
        histPues.idDepartamento = request.form['idDepartamento']
        histPues.fechaInicio = request.form['fechaInicio']
        histPues.fechaFin = request.form['fechaFin']
        histPues.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return redirect(url_for('consultarEmpleadosPersonal'))


@historialPuestos.route('/historialPuestos/eliminarHistorialPuestos/<int:id>')
@login_required
def eliminarHistorialPuestos(id):
    histPues = historialPuestos()
    histPues.eliminar(id)
    flash('Registro eliminado con exito')
    return render_template('/formaspago/consultar.html', hs=histPues.consultaGeneral())

