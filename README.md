# Proyecto CRUD de Usuarios

Este proyecto consiste en una aplicación CRUD de usuarios que utiliza un backend en Flask y un frontend en React. La aplicación se conecta a una base de datos MySQL para gestionar los usuarios.

## Requisitos previos

- Python 3
- Node.js y npm (para el frontend con React)
- MySQL

## Instrucciones para ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/MiguelAngel-117/parcial-2.git
cd parcial-2
```

### 2. Instalar las librerias necesarias de python:
```
pip install -r requirements.txt
``` 
### 3. Crear BD (o modificar la conexión si ya existe una)
```
CREATE DATABASE userdb;
USE userdb;
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100) UNIQUE,
  password VARCHAR(100)
);
```

### 4. Ejecutar el backend en una terminal
```
cd ./backend
python app.py
```

### 5. Ejecutar el frontend en otra terminal
```
cd ./frontend
npm start
```