from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_required
from model.DAO import Percepciones

percepciones = Blueprint("percepciones", __name__, static_folder="view", template_folder="controller")


@percepciones.route('/percepciones/consultarPercepciones')
@login_required
def consultarPercepciones():
    perceps = Percepciones()
    return render_template('/percepciones/consultar.html', perce=perceps.consultaGeneral())

@app.route('/percepciones/nombre/<string:nombre>', methods=['get'])
def consultarNombrePercepciones(nombre):
    e=Percepciones()
    return json.dumps(e.consultarNombrePercepciones(nombre))


@percepciones.route('/percepciones/registrarPercepciones')
@login_required
def registrarPercepciones():
    return render_template('/percepciones/nuevo.html')


@percepciones.route('/percepciones/guardandoPercepciones', methods=['post'])
@login_required
def guardandoPercepciones():
    perce = Percepciones()
    perce.nombre = request.form['nombre']
    perce.descripcion = request.form['descripcion']
    perce.diasPagar = request.form['diasPagar']
    perce.insertar()
    flash('Percepciones registradas exitosamente')
    return redirect('registrarPercepciones')


@percepciones.route('/percepciones/ver/<int:id>')
@login_required
def editarPercepciones(id):
    perce = Percepciones()
    return render_template('/percepciones/editar.html', perceps=perce.consultaIndividual(id))


@percepciones.route('/percepciones/editandoPercepciones', methods=['post'])
@login_required
def editandoPercepciones():
    try:
        perce = Percepciones()
        perce.idPercepcion = request.form['idPercepcion']
        perce.nombre = request.form['nombre']
        perce.descripcion = request.form['descripcion']
        perce.diasPagar = request.form['diasPagar']
        perce.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/percepciones/editar.html', perceps=perce)


@percepciones.route('/percepciones/eliminarPerceociones/<int:id>')
@login_required
def eliminarPercepciones(id):
    perceps = Percepciones()
    perceps.eliminar(id)
    flash('Registro de Percepciones eliminado con exito')
    return render_template('/percepciones/consultar.html', perce=perceps.consultaGeneral())
