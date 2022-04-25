from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_required
from model.DAO import Puestos

puestos = Blueprint("puestos", __name__, static_folder="view", template_folder="controller")

@puestos.route('/puestos/consultarPuestos')
@login_required
def consultarPuestos():
    puesto = Puestos()
    return render_template('/puestos/consultar.html', pues=puesto.consultaGeneral())

@puestos.route('/puestos/registrarPuestos')
@login_required
def registrarPuestos():
    return render_template('/puestos/nuevo.html')

@puestos.route('/puestos/guardandoPuestos',methods=['post'])
@login_required
def guardandoPuestos():
    pues = Puestos()
    pues.nombre = request.form['nombre']
    pues.salarioMinimo = request.form['salarioMinimo']
    pues.salarioMaximo = request.form['salarioMaximo']
    pues.estatus = request.form['estatus']
    pues.insertar()
    flash('Puesto registrado exitosamente')
    return redirect('registrarPuestos')

@puestos.route('/puestos/ver/<int:id>')
@login_required
def editarPuestos(id):
    pues = Puestos()
    return render_template('/puestos/editar.html', puesto=pues.consultaIndividual(id))

@puestos.route('/puestos/editandoPuestos',methods=['post'])
@login_required
def editandoPuestos():
    try:
        pues = Puestos()
        pues.idPuesto = request.form['idPuesto']
        pues.nombre = request.form['nombrePuesto']
        pues.salarioMinimo = request.form['salarioMinimo']
        pues.salarioMaximo = request.form['salarioMaximo']
        pues.estatus = request.form['estatus']
        pues.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/puestos/editar.html', puesto=pues)


@puestos.route('/puestos/eliminarPuestos/<int:id>')
@login_required
def eliminarPuestos(id):
    puesto = Puestos()
    puesto.idPuesto = id
    puesto.estatus = 'I'
    puesto.actualizar()
    flash('Registro del puesto eliminado con exito')
    return render_template('/puestos/consultar.html', pues=puesto.consultaGeneral())


