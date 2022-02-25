create database RH
use RH

CREATE TABLE Estados(
    idEstado INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(60) NOT NULL,
    siglas VARCHAR(10) NOT NULL,
    estatus CHAR NOT NULL,
    CONSTRAINT UK_Estados UNIQUE (idEstado, nombre, siglas),
    CONSTRAINT Chk_estatus check (estatus='A' or estatus='I'),
    CONSTRAINT PK_Estados PRIMARY KEY (idEstado)
);



CREATE TABLE Ciudades(
    idCiudad INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(60) NOT NULL,
    idEstado INT NOT NULL,
    estatus CHAR NOT NULL,
	CONSTRAINT UK_Ciudades UNIQUE (idCiudad, nombre),
    CONSTRAINT Chk_estatus check (estatus='A' or estatus='I'),
    CONSTRAINT PK_Ciudades PRIMARY KEY (idCiudad),
    CONSTRAINT FK_Ciudades_Estado foreign key (idEstado) references Estados (idEstado)
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
    CONSTRAINT UK_Sucursales UNIQUE (idSucursal, nombre),
    CONSTRAINT Chk_estatus check (estatus='A' or estatus='I'),
    CONSTRAINT PK_Sucursales PRIMARY KEY (idSucursal),
    CONSTRAINT FK_Sucursales_Ciudades foreign key (idCiudad) references Ciudades (idCiudad)
);


CREATE TABLE Turnos (
    idTurno INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(20) NOT NULL,
    horaInicio TIMESTAMP NOT NULL,
    horaFin TIMESTAMP NOT NULL,
    dias  VARCHAR(30) NOT NULL,
	CONSTRAINT UK_Turnos UNIQUE (idTurno),
    CONSTRAINT PK_Turnos PRIMARY KEY (idTurno)
);


CREATE TABLE Departamentos (
    idDepartamento INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    estatus CHAR NOT NULL,
	CONSTRAINT UK_Departamentos UNIQUE (idDepartamento, nombre),
    CONSTRAINT Chk_estatus check (estatus='A' or estatus='I'),
    CONSTRAINT PK_Departamentos  PRIMARY KEY (idDepartamento)
);


CREATE TABLE Percepciones (
    idPercepcion INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(30) NOT NULL,
    descripcion VARCHAR(80) NOT NULL,
    diasPagar INT NOT NULL,
    CONSTRAINT UK_Percepciones UNIQUE (idPercepcion, nombre),
    CONSTRAINT PK_Percepciones PRIMARY KEY (idPercepcion)
);

CREATE TABLE Deducciones (
    idDeduccion INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(30) NOT NULL,
    descripcion VARCHAR(80) NOT NULL,
    porcentaje FLOAT NOT NULL,
	CONSTRAINT UK_Deducciones UNIQUE (idDeduccion, nombre),
    constraint chk_porcentaje check (salario <= 100 and salario >=0 ),
    CONSTRAINT PK_Deducciones PRIMARY KEY (idDeduccion)
);


CREATE TABLE Periodos (
    idPeriodo INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    fechaInicio DATE NOT NULL,
    fechaFin DATE NOT NULL,
    estatus CHAR NOT NULL,
    CONSTRAINT UK_Periodos UNIQUE (idPeriodo, nombre),
    CONSTRAINT Chk_estatus check (estatus='A' or estatus='I'),
	CONSTRAINT Chk_Fechas check (fechaFin >= fechaInicio),
    CONSTRAINT PK_Periodos PRIMARY KEY (idPeriodo)
);

CREATE TABLE FormasPago (
    idFormaPago  INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    estatus CHAR NOT NULL,
	CONSTRAINT UK_FormasPago UNIQUE (idFormaPago, nombre),
    CONSTRAINT Chk_estatus check (estatus='A' or estatus='I'),
    CONSTRAINT PK_FormasPago PRIMARY KEY (idFormaPago)
);

CREATE TABLE Puestos (
    idPuesto INT  AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(60) NOT NULL,
    salarioMinimo FLOAT NOT NULL,
    salarioMaximo FLOAT NOT NULL,
    estatus CHAR NOT NULL,
	CONSTRAINT UK_Puestos UNIQUE (idPuesto, nombre),
    CONSTRAINT Chk_estatus check (estatus='A' or estatus='I'),
	CONSTRAINT Chk_Salario check (salarioMaximo > salarioMinimo),
    CONSTRAINT PK_Puestos PRIMARY KEY (idPuesto)
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
    nss VARCHAR(10),
    diasVacaciones INT NOT NULL,
    diasPermiso INT NOT NULL,
    fotografia BLOB NOT NULL,
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
	CONSTRAINT UK_Empleados UNIQUE (idEmpleado, curp, nss, email ),
    constraint Chk_Empleados_nss check (nss like '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'),
    CONSTRAINT Chk_estatus check (estatus='A' or estatus='I'),
    CONSTRAINT PK_Empleados PRIMARY KEY (idEmpleado),
    CONSTRAINT FK_Empleados_Ciudades foreign key (idCiudad) references Ciudades (idCiudad),
    CONSTRAINT FK_Empleados_Turnos foreign key (idTurno) references Turnos (idTurno),
    CONSTRAINT FK_Empleados_Departamentos foreign key (idDepartamento) references Departamentos (idDepartamento),
    CONSTRAINT FK_Empleados_Puestos foreign key (idPuesto) references Puestos (idPuesto),
    CONSTRAINT FK_Empleados_Sucursales foreign key (idSucursal) references Sucursales (idSucursal)
);

CREATE TABLE HistorialPuestos (
    idEmpleado INT AUTO_INCREMENT NOT NULL,
    idPuesto INT NOT NULL,
    idDepartamento INT NOT NULL,
    fechaInicio DATE NOT NULL,
    fechaFin DATE NOT NULL,
    CONSTRAINT Chk_Fecha check (fechaFin > fechaInicio),
    CONSTRAINT PK_HistorialPuestos PRIMARY KEY (idEmpleado, idPuesto, idDepartamento, fechaInicio),
    CONSTRAINT FK_HistorialPuestos_Puestos foreign key (idPuesto) references Puestos (idPuesto),
    CONSTRAINT FK_HistorialPuestos_Empleados foreign key (idEmpleado) references Empleados (idEmpleado),
    CONSTRAINT FK_HistorialPuestos_Departamentos foreign key (idDepartamento) references Departamentos (idDepartamento)
);

CREATE TABLE Asistencias (
    idAsistencia INT AUTO_INCREMENT NOT NULL,
    fecha DATE NOT NULL,
    horaEntrada TIMESTAMP NOT NULL,
    horaSalida TIMESTAMP NOT NULL,
    dia VARCHAR(10) NOT NULL,
    idEmpleado INT NOT NULL,
    CONSTRAINT PK_Asistencias PRIMARY KEY (idAsistencia),
    CONSTRAINT FK_Asistencias_Empleados foreign key (idEmpleado) references Empleados (idEmpleado)
);

CREATE TABLE AusenciaJustificada (
    idAusencia INT  AUTO_INCREMENT NOT NULL,
    fechaSolicitud DATE NOT NULL,
    fechaInicio DATE NOT NULL,
    fechaFin DATE NOT NULL,
    tipo CHAR NOT NULL,
    idEmpleadoSolicita INT NOT NULL,
    idEmpleadoAutoriza INT NOT NULL,
    evidencia BLOB NOT NULL,
    estatus CHAR NOT NULL,
    motivo VARCHAR(100),
	CONSTRAINT Chk_estatus check (estatus='A' or estatus='I'),
    CONSTRAINT Chk_empleadosdif check (idEmpleadoSolicita != idEmpleadoAutoriza),
    CONSTRAINT PK_AusenciaJustificada PRIMARY KEY (idAusencia),
    CONSTRAINT FK_AusenciaJustificada_Empleados_2 foreign key (idEmpleadoAutoriza) references Empleados (idEmpleado),
    CONSTRAINT FK_AusenciaJustificada_Empleados foreign key (idEmpleadoSolicita) references Empleados (idEmpleado)
);

CREATE TABLE DocumentacionEmpleado (
    idDocumento INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(60) NOT NULL,
    fechaEntrega DATE NOT NULL,
    documento BLOB NOT NULL,
    idEmpleado INT NOT NULL,
    CONSTRAINT PK_DocumentacionEmpleado PRIMARY KEY (idDocumento),
    CONSTRAINT FK_DocumentacionEmpleado_Empleados foreign key (idEmpleado) references Empleados (idEmpleado)
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
    CONSTRAINT Chk_estatus check (estatus='P' or estatus='D'),
    CONSTRAINT PK_Nominas PRIMARY KEY (idNomina),
    CONSTRAINT FK_Nominas_FormasPago foreign key (idFormaPago) references FormasPago (idFormaPago),
    CONSTRAINT FK_Nominas_Periodos foreign key (idPeriodo) references Periodos (idPeriodo),
    CONSTRAINT FK_Nominas_Empleados foreign key (idEmpleado) references Empleados (idEmpleado)
);

CREATE TABLE NominasPercepciones (
    idNomina INT AUTO_INCREMENT NOT NULL,
    idPercepcion INT NOT NULL,
    importe FLOAT NOT NULL,
    CONSTRAINT PK_NominasPercepciones PRIMARY KEY (idPercepcion, idNomina),
    CONSTRAINT FK_NominasPercepciones_Nominas foreign key (idNomina) references Nominas (idNomina),
    CONSTRAINT FK_NominasPercepciones_Percepciones foreign key (idPercepcion) references Percepciones (idPercepcion)
);

CREATE TABLE NominasDeducciones (
    idNomina INT AUTO_INCREMENT NOT NULL,
    idDeduccion INT NOT NULL,
    importe FLOAT NOT NULL,
    CONSTRAINT PK_NominasDeducciones PRIMARY KEY (idDeduccion, idNomina),
    CONSTRAINT FK_NominasDeducciones_Nominas foreign key (idNomina) references Nominas (idNomina),
    CONSTRAINT FK_NominasDeducciones_Deducciones foreign key (idDeduccion) references Deducciones (idDeduccion)
);
