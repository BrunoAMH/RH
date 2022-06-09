CREATE DATABASE RH;
USE RH;

CREATE TABLE Estados(
    idEstado INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(60) NOT NULL,
    siglas VARCHAR(10) NOT NULL,
    estatus CHAR NOT NULL,
    CONSTRAINT uk_estados UNIQUE (idEstado, nombre, siglas),
    CONSTRAINT pk_estados PRIMARY KEY (idEstado)
);

CREATE TABLE Ciudades(
    idCiudad INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(60) NOT NULL,
    idEstado INT NOT NULL,
    estatus CHAR NOT NULL,
	CONSTRAINT uk_ciudades UNIQUE (idCiudad, nombre),
    CONSTRAINT pk_ciudades PRIMARY KEY (idCiudad),
    CONSTRAINT fk_ciudades_estado FOREIGN KEY (idEstado) REFERENCES Estados (idEstado)
);


CREATE TABLE Sucursales (
    idSucursal INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    telefono VARCHAR(15) NOT NULL,
    direccion VARCHAR(80) NOT NULL,
    colonia VARCHAR(50) NOT NULL,
    codigoPostal VARCHAR(5) NOT NULL,
    presupuesto FLOAT NOT NULL,
    estatus CHAR NOT NULL,
    idCiudad INT NOT NULL,
    CONSTRAINT uk_sucursales UNIQUE (idSucursal, nombre),
    CONSTRAINT pk_sucursales PRIMARY KEY (idSucursal),
    CONSTRAINT fk_sucursales_ciudades FOREIGN KEY (idCiudad) REFERENCES Ciudades (idCiudad)
);

CREATE TABLE Turnos (
    idTurno INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(20) NOT NULL,
    horaInicio TIME NOT NULL,
    horaFin TIME NOT NULL,
    dias  VARCHAR(30) NOT NULL,
	CONSTRAINT uk_turnos UNIQUE (idTurno),
    CONSTRAINT pk_turnos PRIMARY KEY (idTurno)
);

CREATE TABLE Departamentos (
    idDepartamento INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    estatus CHAR NOT NULL,
	CONSTRAINT uk_departamentos UNIQUE (idDepartamento, nombre),
    CONSTRAINT pk_departamentos  PRIMARY KEY (idDepartamento)
);


CREATE TABLE Percepciones (
    idPercepcion INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(30) NOT NULL,
    descripcion VARCHAR(80) NOT NULL,
    diasPagar INT NOT NULL,
    CONSTRAINT uk_percepciones UNIQUE (idPercepcion, nombre),
    CONSTRAINT pk_percepciones PRIMARY KEY (idPercepcion)
);

CREATE TABLE Deducciones (
    idDeduccion INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(30) NOT NULL,
    descripcion VARCHAR(80) NOT NULL,
    porcentaje FLOAT NOT NULL,
	CONSTRAINT uk_deducciones UNIQUE (idDeduccion, nombre),
    CONSTRAINT pk_deducciones PRIMARY KEY (idDeduccion)
);


CREATE TABLE Periodos (
    idPeriodo INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    fechaInicio DATE NOT NULL,
    fechaFin DATE NOT NULL,
    estatus CHAR NOT NULL,
    CONSTRAINT uk_periodos UNIQUE (idPeriodo, nombre),
    CONSTRAINT pk_periodos PRIMARY KEY (idPeriodo)
);

CREATE TABLE FormasPago (
    idFormaPago  INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    estatus CHAR NOT NULL,
	CONSTRAINT uk_formasPago UNIQUE (idFormaPago, nombre),
    CONSTRAINT pk_formasPago PRIMARY KEY (idFormaPago)
);

CREATE TABLE Puestos (
    idPuesto INT  AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(60) NOT NULL,
    salarioMinimo FLOAT NOT NULL,
    salarioMaximo FLOAT NOT NULL,
    estatus CHAR NOT NULL,
	CONSTRAINT uk_puestos UNIQUE (idPuesto, nombre),
    CONSTRAINT pk_puestos PRIMARY KEY (idPuesto)
);

CREATE TABLE Empleados (
    idEmpleado INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(30) NOT NULL,
    apellidoPaterno VARCHAR(30) NOT NULL,
    apellidoMaterno VARCHAR(30) NOT NULL,
    sexo CHAR NOT NULL,
    fechaNacimiento DATE NOT NULL,
    curp VARCHAR(20) NOT NULL,
    estadoCivil VARCHAR(20) NOT NULL,
    fechaContratacion DATE NOT NULL,
    salarioDiario FLOAT,
    nss VARCHAR(11),
    diasVacaciones INT NOT NULL,
    diasPermiso INT NOT NULL,
    fotografia MEDIUMBLOB  NULL,
    direccion VARCHAR (80) NOT NULL,
    colonia VARCHAR (50) NOT NULL,
    codigoPostal VARCHAR (5) NOT NULL,
    escolaridad VARCHAR (80) NOT NULL,
    especialidad VARCHAR (100) NOT NULL, 
    email VARCHAR(100) NOT NULL,
    contraseña VARCHAR(20) NOT NULL,
    tipo VARCHAR(10) NOT NULL,
    estatus CHAR NOT NULL,
    idDepartamento INT NOT NULL,
    idPuesto INT NOT NULL,
    idCiudad INT NOT NULL,
    idSucursal INT NOT NULL,
    idTurno INT NOT NULL,
	CONSTRAINT uk_empleados UNIQUE (idEmpleado, curp, nss, email ),
    CONSTRAINT pk_empleados PRIMARY KEY (idEmpleado),
    CONSTRAINT fk_empleados_ciudades FOREIGN KEY (idCiudad) REFERENCES Ciudades (idCiudad),
    CONSTRAINT fk_empleados_turnos FOREIGN KEY (idTurno) REFERENCES Turnos (idTurno),
    CONSTRAINT fk_empleados_departamentos FOREIGN KEY (idDepartamento) REFERENCES Departamentos (idDepartamento),
    CONSTRAINT fk_empleados_puestos FOREIGN KEY (idPuesto) REFERENCES Puestos (idPuesto),
    CONSTRAINT fk_empleados_sucursales FOREIGN KEY (idSucursal) REFERENCES Sucursales (idSucursal)
);

CREATE TABLE HistorialPuestos (
    idEmpleado INT AUTO_INCREMENT NOT NULL,
    idPuesto INT NOT NULL,
    idDepartamento INT NOT NULL,
    fechaInicio DATE NOT NULL,
    fechaFin DATE NOT NULL,
    CONSTRAINT pk_historial_puestos PRIMARY KEY (idEmpleado, idPuesto, idDepartamento, fechaInicio),
    CONSTRAINT fk_historial_puestos_puestos FOREIGN KEY (idPuesto) REFERENCES Puestos (idPuesto),
    CONSTRAINT fk_historial_puestos_empleados FOREIGN KEY (idEmpleado) REFERENCES Empleados (idEmpleado),
    CONSTRAINT fk_historial_puestos_departamentos FOREIGN KEY (idDepartamento) REFERENCES Departamentos (idDepartamento)
);

CREATE TABLE Asistencias (
    idAsistencia INT AUTO_INCREMENT NOT NULL,
    fecha DATE NOT NULL,
    horaEntrada TIME NULL,
    horaSalida TIME NULL,
    dia VARCHAR(10) NOT NULL,
    idEmpleado INT NOT NULL,
    CONSTRAINT pk_asistencias PRIMARY KEY (idAsistencia),
    CONSTRAINT fk_asistencias_empleados FOREIGN KEY (idEmpleado) REFERENCES Empleados (idEmpleado)
);
use rh;
CREATE TABLE AusenciaJustificada (
    idAusencia INT  AUTO_INCREMENT NOT NULL,
    fechaSolicitud DATE NOT NULL,
    fechaInicio DATE NOT NULL,
    fechaFin DATE NOT NULL,
    tipo VARCHAR(100) NOT NULL,
    idEmpleadoSolicita INT NOT NULL,
    idEmpleadoAutoriza INT NOT NULL,
    evidencia MEDIUMBLOB  NULL,
    estatus CHAR NOT NULL,
    motivo VARCHAR(100),
    CONSTRAINT pk_ausencia_justificada PRIMARY KEY (idAusencia),
    CONSTRAINT fk_ausencia_justificada_empleados_2 FOREIGN KEY (idEmpleadoAutoriza) REFERENCES Empleados (idEmpleado),
    CONSTRAINT fk_ausencia_justificada_empleados FOREIGN KEY (idEmpleadoSolicita) REFERENCES Empleados (idEmpleado)
);

CREATE TABLE DocumentacionEmpleado (
    idDocumento INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(60) NOT NULL,
    fechaEntrega DATE NOT NULL,
    documento MEDIUMBLOB  NULL,
    idEmpleado INT NOT NULL,
    CONSTRAINT pk_documentacion PRIMARY KEY (idDocumento),
    CONSTRAINT fk_documentacion_empleado FOREIGN KEY (idEmpleado) REFERENCES Empleados (idEmpleado)
);

CREATE TABLE Nominas (
    idNomina INT AUTO_INCREMENT NOT NULL,
    fechaElaboracion DATE NOT NULL,
    fechaPago DATE NOT NULL,
    subtotal FLOAT NOT NULL,
    retenciones FLOAT NOT NULL,
    total FLOAT NOT NULL,
    diasTrabajados INT NOT NULL,
    estatus CHAR NOT NULL,
    idEmpleado INT NOT NULL,
    idFormaPago INT NOT NULL,
    idPeriodo INT NOT NULL,
    CONSTRAINT pk_nominas PRIMARY KEY (idNomina),
    CONSTRAINT fk_nominas_formas_pago FOREIGN KEY (idFormaPago) REFERENCES FormasPago (idFormaPago),
    CONSTRAINT fk_nominas_periodos FOREIGN KEY (idPeriodo) REFERENCES Periodos (idPeriodo),
    CONSTRAINT fk_nominas_empleados FOREIGN KEY (idEmpleado) REFERENCES Empleados (idEmpleado)
);

CREATE TABLE NominasPercepciones (
    idNomina INT AUTO_INCREMENT NOT NULL,
    idPercepcion INT NOT NULL,
    importe FLOAT NOT NULL,
    CONSTRAINT pk_nominas_percepciones PRIMARY KEY (idPercepcion, idNomina),
    CONSTRAINT fk_nominas_percepciones_nominas FOREIGN KEY (idNomina) REFERENCES Nominas (idNomina),
    CONSTRAINT fk_nominas_percepciones_percepciones FOREIGN KEY (idPercepcion) REFERENCES Percepciones (idPercepcion)
);

CREATE TABLE NominasDeducciones (
    idNomina INT AUTO_INCREMENT NOT NULL,
    idDeduccion INT NOT NULL,
    importe FLOAT NOT NULL,
    CONSTRAINT pk_nominas_deducciones PRIMARY KEY (idDeduccion, idNomina),
    CONSTRAINT fk_nominas_deducciones_nominas FOREIGN KEY (idNomina) REFERENCES Nominas (idNomina),
    CONSTRAINT fk_nominas_deducciones_deducciones FOREIGN KEY (idDeduccion) REFERENCES Deducciones (idDeduccion)
);
USE RH;
INSERT INTO `rh`.`estados` (`idEstado`, `nombre`, `siglas`, `estatus`) VALUES ('1', 'Estado de Mexico', 'DF', 'A');
INSERT INTO `rh`.`estados` (`idEstado`, `nombre`, `siglas`, `estatus`) VALUES ('2', 'Michoacan', 'MICH', 'A');
INSERT INTO `rh`.`estados` (`idEstado`, `nombre`, `siglas`, `estatus`) VALUES ('3', 'Jalisco', 'JAL', 'A');

INSERT INTO `rh`.`ciudades` (`idCiudad`, `nombre`, `idEstado`, `estatus`) VALUES ('1', 'Mexico', '1', 'A');
INSERT INTO `rh`.`ciudades` (`idCiudad`, `nombre`, `idEstado`, `estatus`) VALUES ('2', 'Morelia', '2', 'A');
INSERT INTO `rh`.`ciudades` (`idCiudad`, `nombre`, `idEstado`, `estatus`) VALUES ('3', 'Zapopan', '3', 'A');

INSERT INTO `rh`.`sucursales` (`idSucursal`, `nombre`, `telefono`, `direccion`, `colonia`, `codigoPostal`, `presupuesto`, `estatus`, `idCiudad`) VALUES ('1', 'Aguacates DF', '3519138521', 'Mexico Def', 'Del Mexico', '59351', '5200000', 'A', '1');
INSERT INTO `rh`.`sucursales` (`idSucursal`, `nombre`, `telefono`, `direccion`, `colonia`, `codigoPostal`, `presupuesto`, `estatus`, `idCiudad`) VALUES ('2', 'Agropecuaria Mich', '3519138233', 'El real Jerico', 'Las fuentes', '59877', '1520000', 'A', '2');
INSERT INTO `rh`.`sucursales` (`idSucursal`, `nombre`, `telefono`, `direccion`, `colonia`, `codigoPostal`, `presupuesto`, `estatus`, `idCiudad`) VALUES ('3', 'Dsitribuidora Tierra mojada', '3338574891', 'La cruzita', 'Las casas', '87410', '15200000', 'A', '3');

INSERT INTO `rh`.`turnos` (`idTurno`, `nombre`, `horaInicio`, `horaFin`, `dias`) VALUES ('1', 'Vespertino', '12:00:00', '20:00:00', 'LUNES-VIERNES');
INSERT INTO `rh`.`turnos` (`idTurno`, `nombre`, `horaInicio`, `horaFin`, `dias`) VALUES ('2', 'Matutino', '08:00:00', '16:00:00', 'LUNES-VIERNES');
INSERT INTO `rh`.`turnos` (`idTurno`, `nombre`, `horaInicio`, `horaFin`, `dias`) VALUES ('3', 'Nocturno', '18:00:00', '24:00:00', 'LUNES-VIERNES');

INSERT INTO `rh`.`departamentos` (`idDepartamento`, `nombre`, `estatus`) VALUES ('1', 'Personal General', 'A');
INSERT INTO `rh`.`departamentos` (`idDepartamento`, `nombre`, `estatus`) VALUES ('2', 'Recursos humanos', 'A');
INSERT INTO `rh`.`departamentos` (`idDepartamento`, `nombre`, `estatus`) VALUES ('3', 'Distribuidor', 'A');

INSERT INTO `rh`.`percepciones` (`idPercepcion`, `nombre`, `descripcion`, `diasPagar`) VALUES ('1', 'Utilidades', 'Pago de utilidades', '7');
INSERT INTO `rh`.`percepciones` (`idPercepcion`, `nombre`, `descripcion`, `diasPagar`) VALUES ('2', 'Bono de puntualidad', 'Pago por puntualidad', '8');
INSERT INTO `rh`.`percepciones` (`idPercepcion`, `nombre`, `descripcion`, `diasPagar`) VALUES ('3', 'Bono por conducta', 'Pago por conducta', '4');

INSERT INTO `rh`.`deducciones` (`idDeduccion`, `nombre`, `descripcion`, `porcentaje`) VALUES ('1', 'ISR', 'Descuento por ISR', '16');
INSERT INTO `rh`.`deducciones` (`idDeduccion`, `nombre`, `descripcion`, `porcentaje`) VALUES ('2', 'Mal comportamiento', 'Descuento por Mal comportamiento', '8');
INSERT INTO `rh`.`deducciones` (`idDeduccion`, `nombre`, `descripcion`, `porcentaje`) VALUES ('3', 'Poca puntualidad', 'Descuento por Impuntalidad', '5');

INSERT INTO `rh`.`periodos` (`idPeriodo`, `nombre`, `fechaInicio`, `fechaFin`, `estatus`) VALUES ('1', 'Otoño', '2022-06-22', '2022-12-21', 'A');
INSERT INTO `rh`.`periodos` (`idPeriodo`, `nombre`, `fechaInicio`, `fechaFin`, `estatus`) VALUES ('2', 'Primavera', '2022-03-20', '2022-06-22', 'A');
INSERT INTO `rh`.`periodos` (`idPeriodo`, `nombre`, `fechaInicio`, `fechaFin`, `estatus`) VALUES ('3', 'Invierno', '2021-12-21', '2022-03-20', 'A');

INSERT INTO `rh`.`formaspago` (`idFormaPago`, `nombre`, `estatus`) VALUES ('1', 'Pago en efectivo', 'A');
INSERT INTO `rh`.`formaspago` (`idFormaPago`, `nombre`, `estatus`) VALUES ('2', 'Pago en vales', 'A');
INSERT INTO `rh`.`formaspago` (`idFormaPago`, `nombre`, `estatus`) VALUES ('3', 'Deposito Bancario', 'A');

INSERT INTO `rh`.`puestos` (`idPuesto`, `nombre`, `salarioMinimo`, `salarioMaximo`, `estatus`) VALUES ('1', 'Diector de Recursos Humanos', '10000', '15000', 'A');
INSERT INTO `rh`.`puestos` (`idPuesto`, `nombre`, `salarioMinimo`, `salarioMaximo`, `estatus`) VALUES ('2', 'Empleado de recursos humanos ', '8000', '12000', 'A');
INSERT INTO `rh`.`puestos` (`idPuesto`, `nombre`, `salarioMinimo`, `salarioMaximo`, `estatus`) VALUES ('3', 'Empleado de Almacen ', '6000', '8000', 'A');
INSERT INTO `rh`.`puestos` (`idPuesto`, `nombre`, `salarioMinimo`, `salarioMaximo`, `estatus`) VALUES ('4', 'Empleado de Despensa', '4000', '600', 'A');

INSERT INTO `rh`.`empleados` (`idEmpleado`, `nombre`, `apellidoPaterno`, `apellidoMaterno`, `sexo`, `fechaNacimiento`, `curp`, `estadoCivil`, `fechaContratacion`, `salarioDiario`, `nss`, `diasVacaciones`, `diasPermiso`, `fotografia`, `direccion`, `colonia`, `codigoPostal`, `escolaridad`, `especialidad`, `email`, `contraseña`, `tipo`, `estatus`, `idDepartamento`, `idPuesto`, `idCiudad`, `idSucursal`, `idTurno`) VALUES ('1', 'Bruno Armando ', 'Martinez ', 'Huizar', 'H', '2000-05-28', 'MAHB000528HMNRZRA4', 'Soltero', '2022-02-02', '300', '15274781481', '5', '5', NULL, 'Ruta de chapultepec', 'de la nacion', '59610', 'Licenciatura', 'IA', 'bruno@gmail.com', 'Hola.123', 'Empleado', 'A', '1', '1', '1', '1', '1');
INSERT INTO `rh`.`empleados` (`idEmpleado`, `nombre`, `apellidoPaterno`, `apellidoMaterno`, `sexo`, `fechaNacimiento`, `curp`, `estadoCivil`, `fechaContratacion`, `salarioDiario`, `nss`, `diasVacaciones`, `diasPermiso`, `fotografia`, `direccion`, `colonia`, `codigoPostal`, `escolaridad`, `especialidad`, `email`, `contraseña`, `tipo`, `estatus`, `idDepartamento`, `idPuesto`, `idCiudad`, `idSucursal`, `idTurno`) VALUES ('2', 'Armando ', 'Mercado ', 'Alvarez ', 'H', '1998-02-03', 'MAHB874125TYHYBYAA0', 'Soltero', '2020-01-01', '500', '78954789741', '15', '15', NULL, 'Tanaquillo', 'Del Rancho', '59747', 'Maestria', 'Programacion y redes', 'Armando@gmail.com', 'Hola.123', 'Admin', 'A', '1', '1', '1', '1', '1');
INSERT INTO `rh`.`empleados` (`idEmpleado`, `nombre`, `apellidoPaterno`, `apellidoMaterno`, `sexo`, `fechaNacimiento`, `curp`, `estadoCivil`, `fechaContratacion`, `salarioDiario`, `nss`, `diasVacaciones`, `diasPermiso`, `fotografia`, `direccion`, `colonia`, `codigoPostal`, `escolaridad`, `especialidad`, `email`, `contraseña`, `tipo`, `estatus`, `idDepartamento`, `idPuesto`, `idCiudad`, `idSucursal`, `idTurno`) VALUES ('3', 'Luis', 'Esponoza', 'Mares', 'H', '2000-05-10', 'MAHB000528HMNRZR71', 'Soltero', '2021-01-01', '200', '15274781485', '7', '7', NULL, 'Palo Alto', 'de la nacion', '59610', 'Licenciatura', 'Bases de datos', 'luis@gmail.com', 'Hola.123', 'Empleado', 'A', '1', '2', '2', '2', '3');

INSERT INTO `rh`.`historialpuestos` (`idEmpleado`, `idPuesto`, `idDepartamento`, `fechaInicio`, `fechaFin`) VALUES ('1', '1', '1', '2020-02-02', '2022-02-01');
INSERT INTO `rh`.`historialpuestos` (`idEmpleado`, `idPuesto`, `idDepartamento`, `fechaInicio`, `fechaFin`) VALUES ('2', '1', '2', '2020-02-02', '2022-02-01');
INSERT INTO `rh`.`historialpuestos` (`idEmpleado`, `idPuesto`, `idDepartamento`, `fechaInicio`, `fechaFin`) VALUES ('3', '3', '3', '2020-02-02', '2022-02-01');

INSERT INTO `rh`.`asistencias` (`idAsistencia`, `fecha`, `horaEntrada`, `horaSalida`, `dia`, `idEmpleado`) VALUES ('1', '2022-06-03', '08:00:00', '16:00:00', 'LUNES', '1');
INSERT INTO `rh`.`asistencias` (`idAsistencia`, `fecha`, `horaEntrada`, `horaSalida`, `dia`, `idEmpleado`) VALUES ('2', '2022-06-03', '08:00:00', '16:00:00', 'LUNES', '2');
INSERT INTO `rh`.`asistencias` (`idAsistencia`, `fecha`, `horaEntrada`, `horaSalida`, `dia`, `idEmpleado`) VALUES ('3', '2022-06-03', '08:00:00', '16:00:00', 'LUNES', '3');

INSERT INTO `rh`.`ausenciajustificada` (`idAusencia`, `fechaSolicitud`, `fechaInicio`, `fechaFin`, `tipo`, `idEmpleadoSolicita`, `idEmpleadoAutoriza`, `evidencia`, `estatus`, `motivo`) VALUES ('1', '2022-06-03', '2022-06-09', '2022-06-12', 'Vacaciones', '1', '2', NULL, 'P', 'Estoy estresado y necesito descansar');
INSERT INTO `rh`.`ausenciajustificada` (`idAusencia`, `fechaSolicitud`, `fechaInicio`, `fechaFin`, `tipo`, `idEmpleadoSolicita`, `idEmpleadoAutoriza`, `evidencia`, `estatus`, `motivo`) VALUES ('2', '2022-03-01', '2022-03-20', '2022-03-22', 'Permiso', '3', '2', NULL, 'P', 'Mi tio murio y necesito ir al belorio');
INSERT INTO `rh`.`ausenciajustificada` (`idAusencia`, `fechaSolicitud`, `fechaInicio`, `fechaFin`, `tipo`, `idEmpleadoSolicita`, `idEmpleadoAutoriza`, `evidencia`, `estatus`, `motivo`) VALUES ('3', '2022-06-03', '2022-05-10', '2022-05-17', 'Vacaciones', '3', '2', NULL, 'P', 'ya me tocan mis vacaciones');

INSERT INTO `rh`.`documentacionempleado` (`idDocumento`, `nombre`, `fechaEntrega`, `documento`, `idEmpleado`) VALUES ('1', 'Curp', '2022-06-06', NULL, '1');
INSERT INTO `rh`.`documentacionempleado` (`idDocumento`, `nombre`, `fechaEntrega`, `documento`, `idEmpleado`) VALUES ('2', 'Acta de nacimiento', '2022-06-06', NULL, '1');
INSERT INTO `rh`.`documentacionempleado` (`idDocumento`, `nombre`, `fechaEntrega`, `documento`, `idEmpleado`) VALUES ('3', 'Curp', '2022-06-06', NULL, '3');
INSERT INTO `rh`.`documentacionempleado` (`idDocumento`, `nombre`, `fechaEntrega`, `documento`, `idEmpleado`) VALUES ('4', 'Acta de nacimiento', '2022-06-06', NULL, '3');

INSERT INTO `rh`.`nominas` (`idNomina`, `fechaElaboracion`, `fechaPago`, `subtotal`, `retenciones`, `total`, `diasTrabajados`, `estatus`, `idEmpleado`, `idFormaPago`, `idPeriodo`) VALUES ('1', '2022-02-02', '2022-02-04', '12000', '3000', '15000', '30', 'P', '1', '1', '1');
INSERT INTO `rh`.`nominas` (`idNomina`, `fechaElaboracion`, `fechaPago`, `subtotal`, `retenciones`, `total`, `diasTrabajados`, `estatus`, `idEmpleado`, `idFormaPago`, `idPeriodo`) VALUES ('2', '2022-02-02', '2022-02-04', '12000', '3000', '15000', '30', 'P', '2', '2', '2');
INSERT INTO `rh`.`nominas` (`idNomina`, `fechaElaboracion`, `fechaPago`, `subtotal`, `retenciones`, `total`, `diasTrabajados`, `estatus`, `idEmpleado`, `idFormaPago`, `idPeriodo`) VALUES ('3', '2022-02-02', '2022-02-04', '12000', '3000', '15000', '30', 'P', '3', '3', '3');

INSERT INTO `rh`.`nominaspercepciones` (`idNomina`, `idPercepcion`, `importe`) VALUES ('1', '1', '500');
INSERT INTO `rh`.`nominaspercepciones` (`idNomina`, `idPercepcion`, `importe`) VALUES ('2', '2', '400');
INSERT INTO `rh`.`nominaspercepciones` (`idNomina`, `idPercepcion`, `importe`) VALUES ('3', '3', '200');

INSERT INTO `rh`.`nominasdeducciones` (`idNomina`, `idDeduccion`, `importe`) VALUES ('1', '1', '250');
INSERT INTO `rh`.`nominasdeducciones` (`idNomina`, `idDeduccion`, `importe`) VALUES ('2', '2', '250');
INSERT INTO `rh`.`nominasdeducciones` (`idNomina`, `idDeduccion`, `importe`) VALUES ('3', '3', '250');

use rh;
USE rh;
/*----------------------------------------------------------------------------------------------------------------------------------------------*/
/*---------------------------------------------------------------NOMINAS------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------*/
DELIMITER //
CREATE PROCEDURE calcular_salario (IN id_empleado INT, IN id_formaPago INT, IN id_periodo INT)
	BEGIN
		DECLARE sub_total FLOAT;
        DECLARE salario FLOAT;
        DECLARE dias_trabajados int;
        DECLARE dias_justificados int;
        DECLARE fecha_inicio date;
        DECLARE fecha_fin date;
        SET fecha_inicio := (SELECT fechaInicio FROM rh.periodos WHERE idPeriodo = id_periodo);
        SET fecha_fin := (SELECT fechaFin FROM rh.periodos WHERE idPeriodo = id_periodo);
        SET salario := (SELECT salarioDiario FROM rh.empleados WHERE idEmpleado = id_empleado);
        SET dias_trabajados := (SELECT COUNT(*) FROM rh.asistencias WHERE idEmpleado = id_empleado AND horaSalida IS NOT NULL AND fecha BETWEEN fecha_inicio AND fecha_fin);
        SET sub_total := (dias_trabajados * salario);
        INSERT INTO rh.nominas(`fechaElaboracion`, `subtotal`, `retenciones`, `total`, `diasTrabajados`, `estatus`, `idEmpleado`, `idFormaPago`, `idPeriodo`) VALUES (current_date(), sub_total, 0, sub_total, dias_trabajados, 'C', id_empleado, id_formaPago, id_periodo);
    END //

/*----------------------------------------------------------------------------------------------------------------------------------------------*/
/*------------------------------------------------------------PERCEPCIONES----------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------*/
DELIMITER //
CREATE PROCEDURE anadir_percepcion (IN id_nomina INT, IN id_percepcion INT)
BEGIN
	DECLARE salario FLOAT;
    DECLARE dias INT;
    DECLARE importe_per FLOAT;
	SET salario := (SELECT empleados.salarioDiario FROM empleados INNER JOIN nominas ON empleados.idEmpleado=nominas.idEmpleado WHERE idNomina = id_nomina);
    SET dias := (SELECT diasPagar FROM percepciones WHERE idPercepcion = id_percepcion);
    SET importe_per := (salario * dias);
	INSERT INTO rh.nominaspercepciones(idNomina, idPercepcion, importe)
    VALUES (id_nomina, id_percepcion, importe_per);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE eliminar_percepcion (IN id_nomina INT, IN id_percepcion INT)
BEGIN
	DELETE FROM rh.nominaspercepciones WHERE idNomina = id_nomina AND idPercepcion = id_percepcion;
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER anadir_percepcion AFTER INSERT ON rh.nominaspercepciones
FOR EACH ROW BEGIN
	DECLARE money FLOAT;
    DECLARE total_percepciones FLOAT;
    SET total_percepciones := (SELECT importe FROM rh.nominaspercepciones WHERE idNomina = new.idNomina AND idPercepcion = new.idPercepcion);
    SET money := (SELECT subtotal FROM rh.nominas WHERE idNomina = new.idNomina);
	UPDATE rh.nominas SET subtotal = (money + total_percepciones) WHERE idNomina = new.idNomina;
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER eliminar_percepcion BEFORE DELETE ON rh.nominaspercepciones
FOR EACH ROW BEGIN
	DECLARE money FLOAT;
    DECLARE total_percepciones FLOAT;
    SET total_percepciones := (SELECT importe FROM rh.nominaspercepciones WHERE idNomina = old.idNomina AND idPercepcion = old.idPercepcion);
    SET money := (SELECT subtotal FROM rh.nominas WHERE idNomina = old.idNomina);
	UPDATE rh.nominas SET subtotal = (money - total_percepciones) WHERE idNomina = old.idNomina;
END //
DELIMITER ;

/*----------------------------------------------------------------------------------------------------------------------------------------------*/
/*-------------------------------------------------------------DEDUCCIONES----------------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------*/
DELIMITER //
CREATE PROCEDURE eliminar_deduccion (IN id_nomina INT, IN id_deduccion INT)
BEGIN
	DELETE FROM rh.nominasdeducciones WHERE idNomina = id_nomina AND idDeduccion = id_deduccion;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE anadir_deduccion (IN id_nomina INT, IN id_deduccion INT)
BEGIN
	DECLARE sub_total FLOAT;
    DECLARE por FLOAT;
    DECLARE monto FLOAT;
    DECLARE importe_deduccion FLOAT;
	SET sub_total := (SELECT subtotal FROM rh.nominas WHERE idNomina = id_nomina);
    SET por := (SELECT porcentaje FROM rh.deducciones WHERE idDeduccion = id_deduccion);
    SET monto := (sub_total * por);
    SET importe_deduccion := (monto/100);
	INSERT INTO rh.nominasdeducciones(idNomina, idDeduccion, importe)
    VALUES (id_nomina, id_deduccion, importe_deduccion);
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER add_deduccion AFTER INSERT ON rh.nominasdeducciones
FOR EACH ROW BEGIN
	DECLARE retenciones_actual FLOAT;
    DECLARE monto_deduccion FLOAT;
    SET monto_deduccion := (SELECT importe FROM rh.nominasdeducciones WHERE idNomina = new.idNomina AND idDeduccion = new.idDeduccion);
    SET retenciones_actual := (SELECT retenciones FROM rh.nominas WHERE idNomina = new.idNomina);
	UPDATE rh.nominas SET retenciones = (retenciones_actual + monto_deduccion) WHERE idNomina = new.idNomina;
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER eliminar_deduccion BEFORE DELETE ON rh.nominasdeducciones
FOR EACH ROW BEGIN
	DECLARE retenciones_actual FLOAT;
    DECLARE monto_deduccion FLOAT;
    SET monto_deduccion := (SELECT importe FROM rh.nominasdeducciones WHERE idNomina = old.idNomina AND idDeduccion = old.idDeduccion);
    SET retenciones_actual := (SELECT retenciones FROM rh.nominas WHERE idNomina = old.idNomina);
	UPDATE rh.nominas SET retenciones = (retenciones_actual - monto_deduccion) WHERE idNomina = old.idNomina;
END //
DELIMITER ;
/*----------------------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------HISTORIAL DE PUESTOS----------------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------------------------------------------------*/
DELIMITER //
CREATE TRIGGER historial_puesto AFTER INSERT ON rh.empleados
FOR EACH ROW BEGIN
	INSERT INTO rh.historialpuestos (idEmpleado, idPuesto, idDepartamento, fechaInicio, fechaFin)
    VALUES (NEW.idEmpleado, NEW.idPuesto, NEW.idDepartamento, current_date(), NULL);
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER historial_puesto_ascenso AFTER UPDATE ON rh.empleados
FOR EACH ROW BEGIN
	UPDATE  rh.historialpuestos SET fechaFin = (current_date) WHERE new.idEmpleado = old.idEmpleado;
    INSERT INTO rh.historialpuestos (idEmpleado, idPuesto, idDepartamento, fechaInicio, fechaFin)
    VALUES (NEW.idEmpleado, NEW.idPuesto, NEW.idDepartamento, current_date(), NULL);
END //
DELIMITER ;
