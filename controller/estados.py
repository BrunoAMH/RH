from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_required
from model.DAO import Estados
from pymysql import OperationalError

estados = Blueprint("estados", __name__, static_folder="view", template_folder="controller")

@estados.route('/estados/pagina/<int:page>')
def consultarPaginaEstados(page=1):
    try:
        e=Estados()
        paginacion=e.consultarPagina(page)
        est=paginacion.items
        paginas=paginacion.pages
    except OperationalError:
        flash("No hay datos registrados")
        est=None
    return render_template('estados/consultar.html', est=est,  paginas=paginas, pagina=page)

@estados.route('/estados/consultarEstados')
@login_required
def consultarEstados():
    estates = Estados()
    return render_template('/estados/consultar.html', est=estates.consultaGeneral())

@estados.route('/estados/registrarEstados')
@login_required
def registrarEstados():
    return render_template('/estados/nuevo.html')

@estados.route('/estados/guardandoEstado', methods=['post'])
@login_required
def guardandoEstado():
    estates = Estados()
    estates.nombre = request.form['nombre']
    estates.siglas = request.form['siglas']
    estates.estatus = request.form['estatus']
    estates.insertar()
    flash('Estado registrado exitosamente')
    return redirect('registrarEstados')

@estados.route('/estados/ver/<int:id>')
@login_required
def editarEstado(id):
    estates = Estados()
    return render_template('/estados/editar.html', est=estates.consultaIndividual(id))

@estados.route('/estados/editandoEstado', methods=['post'])
@login_required
def editandoEstado():
    try:
        estates = Estados()
        estates.idEstado = request.form['idEstado']
        estates.nombre = request.form['nombreEstado']
        estates.siglas = request.form['siglas']
        estates.estatus = request.form['estatus']
        estates.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/estados/editar.html', est=estates)

@estados.route('/estados/eliminarEstado/<int:id>')
@login_required
def eliminarEstado(id):
    estates = Estados()
    estates.idEstado = id
    estates.estatus = 'I'
    estates.actualizar()
    flash('Registro del estado eliminado con exito')
    return render_template('/estados/consultar.html', est=estates.consultaGeneral())
