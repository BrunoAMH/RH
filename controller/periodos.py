from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_required
from model.DAO import Periodos
from pymysql import OperationalError

periodos = Blueprint("periodos", __name__, static_folder="view", template_folder="controller")

@percepciones.route('/percepciones/pagina/<int:page>')
def consultarPaginaPercepciones(page=1):
    try:
        e=Percepciones()
        paginacion=e.consultarPagina(page)
        perce=paginacion.items
        paginas=paginacion.pages
    except OperationalError:
        flash("No hay datos registrados")
        perce=None
    return render_template('percepciones/consultar.html', perce=perce,  paginas=paginas, pagina=page)

@periodos.route('/periodos/consultarPeriodos')
@login_required
def consultarPeriodos():
    periodo = Periodos()
    return render_template('/periodos/consultar.html', peri=periodo.consultaGeneral())


@periodos.route('/periodos/registrarPeriodos')
@login_required
def registrarPeriodos():
    return render_template('/periodos/nuevo.html')


@periodos.route('/periodos/guardandoPeriodos', methods=['post'])
@login_required
def guardandoPeriodos():
    peri = Periodos()
    peri.nombre = request.form['nombre']
    peri.fechaInicio = request.form['fechaInicio']
    peri.fechaFin = request.form['fechaFin']
    peri.estatus = request.form['estatus']
    peri.insertar()
    flash('Periodo registrado exitosamente')
    return redirect('registrarPeriodos')


@periodos.route('/periodos/ver/<int:id>')
@login_required
def editarPeriodos(id):
    peri = Periodos()
    return render_template('/periodos/editar.html', periodo=peri.consultaIndividual(id))


@periodos.route('/periodos/editandoPeriodos', methods=['post'])
@login_required
def editandoPeriodos():
    try:
        peri = Periodos()
        peri.idPeriodo = request.form['idPeriodo']
        peri.nombre = request.form['nombre']
        peri.fechaInicio = request.form['fechaInicio']
        peri.fechaFin = request.form['fechaFin']
        peri.estatus = request.form['estatus']
        peri.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/periodos/editar.html', periodo=peri)


@periodos.route('/periodos/eliminarPeriodos/<int:id>')
@login_required
def eliminarPeriodos(id):
    periodo = Periodos()
    periodo.idPeriodo = id
    periodo.estatus = 'I'
    periodo.actualizar()
    flash('Periodo eliminado con exito')
    return render_template('/periodos/consultar.html', peri=periodo.consultaGeneral())
