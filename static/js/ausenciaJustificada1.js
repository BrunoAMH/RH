// Ejercicio 283: Ejecutar una función una vez se cargue un documento HTML.
function documentoCargado(){
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
    document.getElementById("dias2").value =dias;
}

document.addEventListener('DOMContentLoaded', documentoCargado, false);