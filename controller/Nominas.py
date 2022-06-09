from datetime import datetime

import mysql.connector as mysql
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required
from model.DAO import Nominas, Empleados, FormasPago, Periodos, Deducciones, Percepciones, NominasPercepciones, NominasDeducciones

nominas = Blueprint("nominas", __name__, static_folder="view", template_folder="controller")

config = {
'user': 'root',
'password': 'Cocacola079*+',
'host': 'localhost',
'port': '3306',
'database': 'rh',
'raise_on_warnings': True}


@nominas.route('/nominas/consultarNominas')
@login_required
def consultarNominas():
    nominas = Nominas()
    return render_template('/nominas/consultar.html', nom=nominas.consultaGeneral())

@nominas.route('/nominas/captura')
@login_required
def capturaNomina():
    empleado = Empleados()
    periodo = Periodos()
    formaPago = FormasPago()
    return render_template('/nominas/captura.html', emp=empleado.consultaGeneral(), per=periodo.consultaGeneral(), formasP=formaPago.consultaGeneral())

@nominas.route('/nominas/guardandoNomina', methods=['POST'])
@login_required
def guardandoNominas():
    nomina = Nominas()
    try:
        cnx = mysql.connect(**config)
        cursor = cnx.cursor()
        idEmp = request.form['opt_empleado']
        idPer = request.form['opt_periodo']
        idFormaPa = request.form['idForma']
        cursor.callproc('calcular_salario', (idEmp, idFormaPa, idPer))
        cnx.commit()
        cursor.close()
        cnx.close()
    except:
        flash('Error')
    nom = nomina.consultarUltimo()
    id = str(nom.idNomina +1)
    return redirect('/nominas/ver/'+id)


@nominas.route('/nominas/ver/<int:id>')
@login_required
def editarNominas(id):
    nominas = Nominas()
    deducciones = Deducciones()
    percepciones = Percepciones()
    nominPer = NominasPercepciones()
    nominDeduc = NominasDeducciones()
    return render_template('/nominas/editar.html', nom=nominas.consultaIndividual(id), deduc=deducciones.consultaGeneral(), percep=percepciones.consultaGeneral(),
                           np=nominPer.consultaGeneral(), nd=nominDeduc.consultaGeneral())

@nominas.route('/nominas/anadiendoPercepcion/<int:idNom>')
@login_required
def anadiendoPercepcion(idNom):
    nominas = Nominas()
    percepciones = Percepciones()
    return render_template('/nominas/percepciones.html', nom=nominas.consultaIndividual(idNom), percep=percepciones.consultaGeneral())

@nominas.route('/nominas/guardandoPercepcion/<int:idNom>/<int:idPer>', methods=['POST', 'GET'])
@login_required
def guardandoPercepcion(idNom, idPer):
    try:
        cnx = mysql.connect(**config)
        cursor = cnx.cursor()
        cursor.callproc('anadir_percepcion', (idNom, idPer))
        cnx.commit()
        cursor.close()
        cnx.close()
        flash('Percepcion guardada y aplicada')
    except:
        flash('Error al aplicar percepcion')
    return redirect(url_for('nominas.editarNominas', id=idNom))

@nominas.route('/nominas/anadiendoDeduccion/<int:idNom>')
@login_required
def anadiendoDeduccion(idNom):
    nominas = Nominas()
    deducciones = Deducciones()
    return render_template('/nominas/deducciones.html', nom=nominas.consultaIndividual(idNom), deduc=deducciones.consultaGeneral())

@nominas.route('/nominas/guardandoDeduccion/<int:idNom>/<int:idDec>', methods=['POST', 'GET'])
@login_required
def guardandoDeduccion(idNom, idDec):
    try:
        cnx = mysql.connect(**config)
        cursor = cnx.cursor()
        cursor.callproc('anadir_deduccion', (idNom, idDec))
        cnx.commit()
        cursor.close()
        cnx.close()
        flash('Deduccion guardada y aplicada')
    except:
        flash('Error al aplicar deduccion')
    return redirect(url_for('nominas.editarNominas', id=idNom))


@nominas.route('/nominas/eliminandoPercepcion/<int:idNom>/<int:idPer>', methods=['POST', 'GET'])
@login_required
def eliminandoPercepcion(idNom, idPer):
    try:
        cnx = mysql.connect(**config)
        cursor = cnx.cursor()
        cursor.callproc('eliminar_percepcion', (idNom, idPer))
        cnx.commit()
        cursor.close()
        cnx.close()
        flash('Percepcion eliminada')
    except:
        flash('Error al eliminar')
    return redirect(url_for('nominas.editarNominas', id=idNom))

@nominas.route('/nominas/eliminandoDeduccion/<int:idNom>/<int:idDec>', methods=['POST', 'GET'])
@login_required
def eliminandoDeduccion(idNom, idDec):
    try:
        cnx = mysql.connect(**config)
        cursor = cnx.cursor()
        cursor.callproc('eliminar_deduccion', (idNom, idDec))
        cnx.commit()
        cursor.close()
        cnx.close()
        flash('Deduccion eliminada')
    except:
        flash('Error al eliminar')
    return redirect(url_for('nominas.editarNominas', id=idNom))

@nominas.route('/nominas/aprobandoNomina/<int:id>')
@login_required
def aprobandoNominas(id):
    try:
        fecha_actual = datetime.today().strftime('%Y-%m-%d')
        nominas = Nominas()
        nominas.idNomina = id
        nominas.estatus = 'A'
        nominas.fechaPago = fecha_actual
        nominas.actualizar()
        flash('La nomina ha sido autorizada con exito')
    except:
        flash('!Error al actualizar!')
    return redirect(url_for('nominas.consultarNominas'))

@nominas.route('/nominas/finalizar', methods=['POST', 'GET'])
@login_required
def finalizarNominas():
    try:
        nominas = Nominas()
        nominas.idNomina = request.form['idNomina']
        subtotal = float(request.form['subtotal'])
        retenciones = float(request.form['retenciones'])
        nominas.total = (subtotal-retenciones)
        nominas.actualizar()
        flash('La nomina ha sido autorizada con exito')
    except:
        flash('!Error al actualizar!')
    return redirect(url_for('nominas.consultarNominas'))


@nominas.route('/nominas/eliminarNominas/<int:id>')
@login_required
def eliminarNomina(id):
    try:
        nominas = Nominas()
        nominas.idNomina = id
        nominas.estatus = 'E'
        nominas.actualizar()
        flash('Registro de nomina eliminado con exito')
        return redirect(url_for('nominas.consultarNominas'))
    except:
        flash('Error al eliminar registro')
#print(dir(mysql))
