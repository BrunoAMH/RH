from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_required
from model.DAO import Turnos
from pymysql import OperationalError

turnos = Blueprint("turnos", __name__, static_folder="view", template_folder="controller")

@turnos.route('/turnos/pagina/<int:page>')
def consultarPaginaTurnos(page=1):
    try:
        e=Turnos()
        paginacion=e.consultarPagina(page)
        turn=paginacion.items
        paginas=paginacion.pages
    except OperationalError:
        flash("No hay datos registrados")
        turn=None
    return render_template('turnos/consultar.html', turn=turn,  paginas=paginas, pagina=page)

@turnos.route('/turnos/consultarTurnos')
@login_required
def consultarTurnos():
    turns = Turnos()
    return render_template('/turnos/consultar.html', turn=turns.consultaGeneral())


@turnos.route('/turnos/registrarTurnos')
@login_required
def registrarTurnos():
    return render_template('/turnos/nuevo.html')


@turnos.route('/turnos/guardandoTurnos', methods=['POST'])
@login_required
def guardandoTurnos():
    turn = Turnos()
    turn.nombre = request.form['nombre']
    turn.horaInicio = request.form['horaInicio']
    turn.horaFin = request.form['horaFin']
    lun = request.form.get("lunes")
    mar = request.form.get("martes")
    mie = request.form.get("miercoles")
    jue = request.form.get("jueves")
    vie = request.form.get("viernes")
    sab = request.form.get("sabado")
    dom = request.form.get("domingo")
    dias_trabajo = (str(lun)+str(mar)+str(mie)+str(jue)+str(vie)+str(sab)+str(dom))
    for x in range(len(dias_trabajo)):
        dias_trabajo = dias_trabajo.replace("None", "")
    turn.dias = dias_trabajo
    turn.insertar()
    flash('Turnos registrado exitosamente')
    return redirect('registrarTurnos')


@turnos.route('/turnos/ver/<int:id>')
@login_required
def editarTurnos(id):
    turn = Turnos()
    return render_template('/turnos/editar.html', turns=turn.consultaIndividual(id))


@turnos.route('/turnos/editandoTurnos', methods=['POST'])
@login_required
def editandoTurnos():
    try:
        turn = Turnos()
        turn.idTurno = request.form['idTurno']
        turn.nombre = request.form['nombre']
        turn.horaInicio = request.form['horaInicio']
        turn.horaFin = request.form['horaFin']
        turn.dias = request.form['dias']
        turn.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/turnos/editar.html', turns=turn)


@turnos.route('/turnos/eliminarTurnos/<int:id>')
@login_required
def eliminarTurnos(id):
    turn = Turnos()
    turn.eliminar(id)
    flash('Registro del turno eliminado con exito')
    return render_template('/turnos/consultar.html', turn=turn.consultaGeneral())
