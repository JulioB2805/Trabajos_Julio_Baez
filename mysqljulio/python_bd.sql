---crear base de datos
CREATE DATABASE IF NOT EXISTS curso_python_db_julio
   DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE curso_python_db_julio;

---Tabla categoria 
CREATE TABLE categoria (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE
);

---Tabla producto
CREATE TABLE producto (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    mombre VARCHAR(150) NOT NULL,
    id_categoria INT NOT NULL,
    precio_gs INT NOT NULL CHECK (precio_gs >=0),
    iva_porcentaje SMALLINT NOT NULL CHECK (iva_porcentaje IN (0,5,10)),
    CONSTRAINT fk_producto_categoria FOREIGN KEY(id_categoria)
       REFERENCES Categoria(id_categoria)
       ON DELETE RESTRICT
)