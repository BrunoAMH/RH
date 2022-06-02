from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_required
from model.DAO import FormasPago
from pymysql import OperationalError

formasPago = Blueprint("formasPago", __name__, static_folder="view", template_folder="controller")

@formasPago.route('/formaspago/pagina/<int:page>')
def consultarPaginaperiodos(page=1):
    try:
        e=FormasPago()
        paginacion=e.consultarPagina(page)
        fop=paginacion.items
        paginas=paginacion.pages
    except OperationalError:
        flash("No hay datos registrados")
        fop=None
    return render_template('formaspago/consultar.html', fop=fop,  paginas=paginas, pagina=page)


@formasPago.route('/formaspago/consultarFormasPago')
@login_required
def consultarFormasPago():
    formaspa = FormasPago()
    return render_template('/formaspago/consultar.html', fop=formaspa.consultaGeneral())


@formasPago.route('/formaspago/registrarFormasPago')
@login_required
def registrarFormasPago():
    return render_template('/formaspago/nuevo.html')


@formasPago.route('/formaspago/guardandoFormasPago', methods=['post'])
@login_required
def guardandoFormasPago():
    fop = FormasPago()
    fop.nombre = request.form['nombre']
    fop.estatus = request.form['estatus']
    fop.insertar()
    flash('Forma de Pago registradas exitosamente')
    return redirect('registrarFormasPago')


@formasPago.route('/formaspago/ver/<int:id>')
@login_required
def editarFormasPago(id):
    fop = FormasPago()
    return render_template('/formaspago/editar.html', formaspa=fop.consultaIndividual(id))


@formasPago.route('/formaspago/editandoFormasPago', methods=['post'])
@login_required
def editandoFormasPago():
    try:
        fop = FormasPago()
        fop.idFormaPago = request.form['idFormaPago']
        fop.nombre = request.form['nombre']
        fop.estatus = request.form['estatus']
        fop.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/formaspago/editar.html', formaspa=fop)


@formasPago.route('/formaspago/eliminarFormasPago/<int:id>')
@login_required
def eliminarFormasPago(id):
    formaspa = FormasPago()
    formaspa.idFormaPago = id
    formaspa.estatus = 'I'
    formaspa.actualizar()
    flash('forma de pago eliminada con exito')
    return render_template('/formaspago/consultar.html', fop=formaspa.consultaGeneral())
