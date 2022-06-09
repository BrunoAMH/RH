const formulario = document.querySelector('#formulario-tarjeta');
var error = document.getElementById('error');
error.style.color='red';

formulario.fechaInicio.addEventListener('change', (e) => {
	var mensajeError = [];
	if(document.getElementById("fechaSolicitud").value>=document.getElementById("fechaInicio").value){
		document.getElementById("fechaInicio").value=null;
		alert("La fecha de solicitud debera de ser menor a la fecha de inicio");
		mensajeError.push('La fecha de solicitud debera de ser menor a la fecha de inicio');
	}else{

	}
		
	error.innerHTML =  mensajeError.join(', ');
});

formulario.fechaFin.addEventListener('change', (e) => {
	var mensajeError = [];
	var aFecha1 = document.getElementById("fechaInicio").value;
    aFecha1 = new Date(aFecha1);
    aFecha1 = (aFecha1.getDate() + 1) + "/" + (aFecha1.getMonth() + 1) + "/" + aFecha1.getFullYear();
    aFecha1 = aFecha1.split('/');


    var aFecha2 = document.getElementById("fechaFin").value;
    aFecha2 = new Date(aFecha2);
    aFecha2 = (aFecha2.getDate() + 1) + "/" + (aFecha2.getMonth() + 1) + "/" + aFecha2.getFullYear();
    aFecha2 = aFecha2.split('/');

    var fFecha1 = Date.UTC(aFecha1[2], aFecha1[1] - 1, aFecha1[0]);
    var fFecha2 = Date.UTC(aFecha2[2], aFecha2[1] - 1, aFecha2[0]);
    var dif = fFecha2 - fFecha1;
    var dias = (Math.floor(dif / (1000 * 60 * 60 * 24))+1);

	if(document.getElementById("fechaInicio").value>=document.getElementById("fechaFin").value){
		document.getElementById("fechaFin").value=null;
		document.getElementById("dias2").value=null;
		alert("La fecha de inicio debera de ser menor que la fecha de fin del periodo de ausencia");
		mensajeError.push('La fecha de inicio debera de ser menor que la fecha de fin del periodo de ausencia');
	}else{
        document.getElementById("dias2").value =dias;
	}
		
	error.innerHTML =  mensajeError.join(', ');
});

formulario.fechaFin.addEventListener('change', (e) => {
    var mensajeError = [];
    if(document.getElementById("dias2").value>document.getElementById("dias").value){
        document.getElementById("fechaFin").value=null;
        document.getElementById("dias2").value=null;
        alert("Los dias de ausemcia son mayores a los que dispone");
		mensajeError.push('Los dias de ausemcia son mayores a los que dispone');
    }else{

    }
    error.innerHTML =  mensajeError.join(', ');
});

formulario.fechaSolicitud.addEventListener('change', (e) => {
	var mensajeError = [];
	if(document.getElementById("fechaSolicitud").value>=document.getElementById("fechaInicio").value){
		document.getElementById("fechaInicio").value=null;
		alert("La fecha de solicitud debera de ser menor a la fecha de inicio");
		mensajeError.push('La fecha de solicitud debera de ser menor a la fecha de inicio');
	}else{

	}

	error.innerHTML =  mensajeError.join(', ');
});

formulario.ti.addEventListener('change', (e) => {
	document.getElementById("dias").value=e.target.value;
	if(document.getElementById("va").value==document.getElementById("ti").value){
        document.getElementById("tipo").value="Vacaciones";
    }

	if(document.getElementById("per").value==document.getElementById("ti").value){
        document.getElementById("tipo").value="Permiso";
    }
});