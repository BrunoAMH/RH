const formulario = document.querySelector('#formulario-tarjeta');
var error = document.getElementById('error');
error.style.color='red';

formulario.EmpleadoAutoriza.addEventListener('change', (e) => {
	var mensajeError = [];
	if(document.getElementById("EmpleadoSolicita").value==document.getElementById("EmpleadoAutoriza").value){
		document.getElementById("ass").value=null;
		mensajeError.push('El empleado que solicita dicha ausencia debe de ser diferente al que autoriza');
	}else if(document.getElementById("fechaSolicitud").value>=document.getElementById("fechaInicio").value){
		document.getElementById("ass").value=null;
		mensajeError.push('La fecha de solicitud debera de ser menor a la fecha de inicio');
	}else if(document.getElementById("fechaInicio").value>=document.getElementById("fechaFin").value){
		document.getElementById("ass").value=null;
		mensajeError.push('La fecha de inicio debera de ser menor que la fecha de fin del periodo de ausencia');
	}else{
		document.getElementById("ass").value='Todo correcto';
	}
		
	error.innerHTML =  mensajeError.join(', ');
});

formulario.fechaInicio.addEventListener('change', (e) => {
	var mensajeError = [];
	if(document.getElementById("EmpleadoSolicita").value==document.getElementById("EmpleadoAutoriza").value){
		document.getElementById("ass").value=null;
		mensajeError.push('El empleado que solicita dicha ausencia debe de ser diferente al que autoriza');
	}else if(document.getElementById("fechaSolicitud").value>=document.getElementById("fechaInicio").value){
		document.getElementById("ass").value=null;
		mensajeError.push('La fecha de solicitud debera de ser menor a la fecha de inicio');
	}else if(document.getElementById("fechaInicio").value>=document.getElementById("fechaFin").value){
		document.getElementById("ass").value=null;
		mensajeError.push('La fecha de inicio debera de ser menor que la fecha de fin del periodo de ausencia');
	}else{
		document.getElementById("ass").value='Todo correcto';
	}
		
	error.innerHTML =  mensajeError.join(', ');
});

formulario.fechaFin.addEventListener('change', (e) => {
	var mensajeError = [];
	if(document.getElementById("EmpleadoSolicita").value==document.getElementById("EmpleadoAutoriza").value){
		document.getElementById("ass").value=null;
		mensajeError.push('El empleado que solicita dicha ausencia debe de ser diferente al que autoriza');
	}else if(document.getElementById("fechaSolicitud").value>=document.getElementById("fechaInicio").value){
		document.getElementById("ass").value=null;
		mensajeError.push('La fecha de solicitud debera de ser menor a la fecha de inicio');
	}else if(document.getElementById("fechaInicio").value>=document.getElementById("fechaFin").value){
		document.getElementById("ass").value=null;
		mensajeError.push('La fecha de inicio debera de ser menor que la fecha de fin del periodo de ausencia');
	}else{
		document.getElementById("ass").value='Todo correcto';
	}
		
	error.innerHTML =  mensajeError.join(', ');
});

formulario.ass.addEventListener('change', (e) => {
	document.getElementById("ass").value=null;
});
