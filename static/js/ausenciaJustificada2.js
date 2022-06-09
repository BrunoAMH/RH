const formulario = document.querySelector('#formulario-tarjeta');
formulario.estatus.addEventListener('change', (e) => {
	if(document.getElementById("tipo").value=="Vacaciones"){
        document.getElementById("diasVacaciones").value=document.getElementById("dias").value-document.getElementById("dias2").value;
    }

	if(document.getElementById("tipo").value=="Permiso"){
        document.getElementById("diasPermiso").value=document.getElementById("dias").value-document.getElementById("dias2").value;
    }
});
