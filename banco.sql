CREATE DATABASE banco;
USE banco;

-- TABLA CLIENTES
CREATE TABLE clientes (
codigo INT AUTO_INCREMENT PRIMARY KEY,
tipo_cliente VARCHAR(50),
nombre VARCHAR(100),
documento VARCHAR(50) UNIQUE,
telefono VARCHAR(20),
correo VARCHAR(100)
);

-- TABLA CUENTAS
DROP TABLE IF EXISTS cuentas;


DROP TABLE cuentas;
CREATE TABLE cuentas (
    numero_cuenta INT AUTO_INCREMENT PRIMARY KEY,
    codigo_cliente INT,
    tipo_cuenta VARCHAR(50),
    moneda VARCHAR(20),
    sucursal VARCHAR(100),
    saldo DECIMAL(15,2),
    estado VARCHAR(20)
);

-- TABLA CREDITOS
CREATE TABLE creditos (
numero_operacion INT AUTO_INCREMENT PRIMARY KEY,
codigo_cliente INT,
monto DECIMAL(15,2),
plazo INT,
tasa_interes DECIMAL(5,2),
estado VARCHAR(20),

FOREIGN KEY (codigo_cliente) REFERENCES clientes(codigo)
);

-- TABLA TRANSACCIONES
CREATE TABLE transacciones
ALTER TABLE transacciones
ADD fecha DATETIME; (
codigo INT AUTO_INCREMENT PRIMARY KEY,
cuenta_origen INT,
cuenta_destino INT,
tipo VARCHAR(50),
monto DECIMAL(15,2),
canal VARCHAR(50),

FOREIGN KEY (cuenta_origen) REFERENCES cuentas(numero_cuenta),
FOREIGN KEY (cuenta_destino) REFERENCES cuentas(numero_cuenta)
);
SELECT * FROM clientes;
SELECT * FROM cuentas;
SELECT * FROM transacciones;
SELECT * FROM creditos;

SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS cuentas;

SET FOREIGN_KEY_CHECKS = 1;