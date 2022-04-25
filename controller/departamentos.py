from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_required
from model.DAO import Departamentos

departamentos = Blueprint("departamentos", __name__, static_folder="view", template_folder="controller")

@departamentos.route('/departamentos/consultarDepartamentos')
@login_required
def consultarDepartamentos():
    departments = Departamentos()
    return render_template('/departamentos/consultar.html', depa=departments.consultaGeneral())

@departamentos.route('/departamentos/registrarDepartamentos')
@login_required
def registrarDepartamentos():
    return render_template('/departamentos/nuevo.html')

@departamentos.route('/departamentos/guardandoDepartamentos',methods=['post'])
@login_required
def guardandoDepartamentos():
    depa = Departamentos()
    depa.nombre = request.form['nombre']
    depa.estatus = request.form['estatus']
    depa.insertar()
    flash('Departamento registrado exitosamente')
    return redirect('registrarDepartamentos')

@departamentos.route('/departamentos/ver/<int:id>')
@login_required
def editarDepartamentos(id):
    depa = Departamentos()
    return render_template('/departamentos/editar.html', departments=depa.consultaIndividual(id))

@departamentos.route('/departamentos/editandoDepartamentos',methods=['post'])
@login_required
def editandoDepartamentos():
    try:
        depa = Departamentos()
        depa.idDepartamento = request.form['idDepartamento']
        depa.nombre = request.form['nombre']
        depa.estatus = request.form['estatus']
        depa.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/departamentos/editar.html', departments=depa)

@departamentos.route('/departamentos/eliminarDepartamentos/<int:id>')
@login_required
def eliminarDepartamentos(id):
    departments = Departamentos()
    departments.idDepartamento = id
    departments.estatus = 'I'
    departments.actualizar()
    flash('Registro de departamentos eliminado con exito')
    return render_template('/departamentos/consultar.html', depa=departments.consultaGeneral())