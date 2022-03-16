var porcentaje = document.getElementById("porcentaje");
var nombre = document.getElementById("nombre");
var error = document.getElementById('error');
error.style.color='red';

function enviarFormulario(form){
	var mensajeError = [];

	if(porcentaje.value == null || porcentaje.value <= 0 || porcentaje.value >= 100 ){
		mensajeError.push('Ingrese un valor mayor a 0 o menor a 100');
	}
	
	error.innerHTML =  mensajeError.join(', ');

	return false;
}

