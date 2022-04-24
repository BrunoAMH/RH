from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_required, current_user
from model.DAO import DocumentacionEmpleado, Empleados

documentacion = Blueprint("documentacion", __name__, static_folder="view", template_folder="controller")


@documentacion.route('/documentacionEmpleado/consultarDocumentacionEmpleado')
@login_required
def consultarDocumentacionEmpleado():
    docemp = DocumentacionEmpleado()
    empleados = Empleados()
    if current_user.is_admin():
        return render_template('/documentacionEmpleado/consultarUsuarios.html', doc=docemp.consultaGeneral(),
                               emp=empleados.consultaGeneral())
    else:
        return render_template('/documentacionEmpleado/consultar.html', doc=docemp.consultaGeneral(),
                               emp=empleados.consultaGeneral())


@documentacion.route('/documentacionEmpleado/registrarDocumentacionEmpleado')
@login_required
def registrarDocumentacionEmpleado():
    empl = Empleados()
    return render_template('/documentacionEmpleado/nuevo.html', emp=empl.consultaGeneral())


@documentacion.route('/documentacionEmpleado/consultarImagen/<int:id>')
def consultarImagenDocumentacionEmpleado(id):
    docemp = DocumentacionEmpleado()
    return docemp.consultarImagen(id)


@documentacion.route('/documentacionEmpleado/guardandoDocumentacionEmpleado', methods=['post'])
@login_required
def guardandoDocumentacionEmpleado():
    docemp = DocumentacionEmpleado()
    docemp.nombre = request.form['nombre']
    docemp.fechaEntrega = request.form['fechaEntrega']
    docemp.documento = request.files['documento'].stream.read()
    docemp.idEmpleado = request.form['idEmpleado']
    docemp.insertar()
    flash('Documentacion registrada exitosamente')
    return redirect('registrarDocumentacionEmpleado')


@documentacion.route('/documentacionEmpleado/ver/<int:id>')
@login_required
def editarDocumentacionEmpleado(id):
    docemp = DocumentacionEmpleado()
    empl = Empleados()
    return render_template('/documentacionEmpleado/editar.html', doc=docemp.consultaIndividual(id),
                           emp=empl.consultaGeneral())


@documentacion.route('/documentacionEmpleado/editandoDocumentacionEmpleado', methods=['post'])
@login_required
def editandoDocumentacionEmpleado():
    try:
        docemp = DocumentacionEmpleado()
        docemp.idDocumento = request.form['idDocumento']
        docemp.nombre = request.form['nombre']
        docemp.fechaEntrega = request.form['fechaEntrega']
        docemp.documento = request.files['documento'].stream.read()
        docemp.idEmpleado = request.form['idEmpleado']
        docemp.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/documentacionEmpleado/editar.html', doc=docemp)


@documentacion.route('/documentacionEmpleado/eliminarDocumentacionEmpleado/<int:id>')
@login_required
def eliminarDocumentacionEmpleado(id):
    docemp = DocumentacionEmpleado()
    docemp.eliminar(id)
    flash('Registro de Dcoumento eliminado con exito')
    return redirect('consultarSucursales')
