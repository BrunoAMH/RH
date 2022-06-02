from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_required
from model.DAO import Deducciones

deducciones = Blueprint("deducciones", __name__, static_folder="view", template_folder="controller")

@deducciones.route('/deducciones/consultarDeducciones')
@login_required
def consultarDeducciones():
    deductions = Deducciones()
    return render_template('/deducciones/consultar.html', deduc=deductions.consultaGeneral())

@app.route('/deducciones/nombre/<string:nombre>', methods=['get'])
def consultarNombreDeducciones(nombre):
    e=Deducciones()
    return json.dumps(e.consultarNombreDeducciones(nombre))

@deducciones.route('/deducciones/registrarDeducciones')
@login_required
def registrarDeducciones():
    return render_template('/deducciones/nuevo.html')


@deducciones.route('/deducciones/guardandoDeducciones',methods=['post'])
@login_required
def guardandoDeducciones():
    deduc = Deducciones()
    deduc.nombre = request.form['nombre']
    deduc.descripcion = request.form['descripcion']
    deduc.porcentaje = request.form['porcentaje']
    deduc.insertar()
    flash('Deducciones registradas exitosamente')
    return redirect('registrarDeducciones')

@deducciones.route('/deducciones/ver/<int:id>')
@login_required
def editarDeducciones(id):
    deduc = Deducciones()
    return render_template('/deducciones/editar.html', deductions=deduc.consultaIndividual(id))

@deducciones.route('/deducciones/editandoDeducciones',methods=['post'])
@login_required
def editandoDeducciones():
    try:
        deduc = Deducciones()
        deduc.idDeduccion = request.form['idDeduccion']
        deduc.nombre = request.form['nombre']
        deduc.descripcion = request.form['descripcion']
        deduc.porcentaje = request.form['porcentaje']
        deduc.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/deducciones/editar.html', deductions=deduc)

@deducciones.route('/deducciones/eliminarDeducciones/<int:id>')
@login_required
def eliminarDeducciones(id):
    deductions = Deducciones()
    deductions.eliminar(id)
    flash('Registro de Deducciones eliminado con exito')
    return render_template('/deducciones/consultar.html', deduc=deductions.consultaGeneral())
