function consultarEmail(){
    var ajax= new XMLHttpRequest();
    var email=document.getElementById("email").value;
    var url="/empleados/email/" + email;
    ajax.open("get", url,true);
    var div = document.getElementById("notificaciones1");
    ajax.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            var respuesta=JSON.parse(this.responseText);
            if(respuesta.estatus=='Error'){
                div.innerHTML=respuesta.mensaje;
                document.getElementById("registrar").setAttribute("disabled","true");
            }else{
                div.innerHTML="";
                document.getElementById("registrar").removeAttribute("disabled");
            }
        }
    };
    ajax.send();
}

function consultarCurp(){
    var ajax= new XMLHttpRequest();
    var email=document.getElementById("curp").value;
    var url="/empleados/curp/" + email;
    ajax.open("get", url,true);
    var div = document.getElementById("notificaciones2");
    ajax.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            var respuesta=JSON.parse(this.responseText);
            if(respuesta.estatus=='Error'){
                div.innerHTML=respuesta.mensaje;
                document.getElementById("registrar").setAttribute("disabled","true");
            }else{
                div.innerHTML="";
                document.getElementById("registrar").removeAttribute("disabled");
            }
        }
    };
    ajax.send();
}

function consultarNombreDoc(){
    var ajax= new XMLHttpRequest();
    var email=document.getElementById("curp").value;
    var url="/empleados/curp/" + email;
    ajax.open("get", url,true);
    var div = document.getElementById("notificaciones2");
    ajax.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            var respuesta=JSON.parse(this.responseText);
            if(respuesta.estatus=='Error'){
                div.innerHTML=respuesta.mensaje;
                document.getElementById("registrar").setAttribute("disabled","true");
            }else{
                div.innerHTML="";
                document.getElementById("registrar").removeAttribute("disabled");
            }
        }
    };
    ajax.send();
}

function consultarNss(){
    var ajax= new XMLHttpRequest();
    var email=document.getElementById("nss").value;
    var url="/empleados/nss/" + email;
    ajax.open("get", url,true);
    var div = document.getElementById("notificaciones3");
    ajax.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            var respuesta=JSON.parse(this.responseText);
            if(respuesta.estatus=='Error'){
                div.innerHTML=respuesta.mensaje;
                document.getElementById("registrar").setAttribute("disabled","true");
            }else{
                div.innerHTML="";
                document.getElementById("registrar").removeAttribute("disabled");
            }
        }
    };
    ajax.send();
}


function validarEmpleados(form){
    var fechaNacimiento=form.fechaNacimiento.value;
    var mensaje = validarEdad(fechaNacimiento);
    var div = document.getElementById("notificaciones5");
    var ban = false;
    if (mensaje != "") {
        div.innerHTML = mensaje;
        ban = false;
    }
    else {
        div.innerHTML = "";
        ban = true;
    }
    return ban;
}

function calcularEdad(cadena){
    var hoy = new Date();
    var cumpleanos = new Date(cadena);
    var edad = hoy.getFullYear() - cumpleanos.getFullYear();
    var m = hoy.getMonth() - cumpleanos.getMonth();
    if (m < 0 || (m === 0 && hoy.getDate() < cumpleanos.getDate())) {
        edad--;
    }
    return edad;
}

function validarEdad(cadena){
    var salida="";
    if(calcularEdad(cadena)<18){
        salida = "<p>La persona que deseas contratar debe de ser mayor de edad.</p> <br>"
    }
    return salida;
}

function consultarNombrePeriodos(){
    var ajax= new XMLHttpRequest();
    var nombre=document.getElementById("nombre").value;
    var url="/periodos/nombre/" + nombre;
    ajax.open("get", url,true);
    var div = document.getElementById("notificaciones6");
    ajax.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            var respuesta=JSON.parse(this.responseText);
            if(respuesta.estatus=='Error'){
                div.innerHTML=respuesta.mensaje;
                document.getElementById("registrar").setAttribute("disabled","true");
            }else{
                div.innerHTML="";
                document.getElementById("registrar").removeAttribute("disabled");
            }
        }
    };
    ajax.send();
}


function consultarNombreFormasPago(){
    var ajax= new XMLHttpRequest();
    var nombre=document.getElementById("nombre").value;
    var url="/formaspago/nombre/" + nombre;
    ajax.open("get", url,true);
    var div = document.getElementById("notificaciones7");
    ajax.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            var respuesta=JSON.parse(this.responseText);
            if(respuesta.estatus=='Error'){
                div.innerHTML=respuesta.mensaje;
                document.getElementById("registrar").setAttribute("disabled","true");
            }else{
                div.innerHTML="";
                document.getElementById("registrar").removeAttribute("disabled");
            }
        }
    };
    ajax.send();
}


function consultarNombreSucursales(){
    var ajax= new XMLHttpRequest();
    var nombre=document.getElementById("nombre").value;
    var url="/sucursales/nombre/" + nombre;
    ajax.open("get", url,true);
    var div = document.getElementById("notificaciones8");
    ajax.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            var respuesta=JSON.parse(this.responseText);
            if(respuesta.estatus=='Error'){
                div.innerHTML=respuesta.mensaje;
                document.getElementById("registrar").setAttribute("disabled","true");
            }else{
                div.innerHTML="";
                document.getElementById("registrar").removeAttribute("disabled");
            }
        }
    };
    ajax.send();
}