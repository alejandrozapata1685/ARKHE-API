ARKHE API

API REST desarrollada con FastAPI para el proyecto de la inmobiliaria ARKHE.

Descripción

ARKHE API es una aplicación backend que permite gestionar diferentes funcionalidades de una inmobiliaria.

Actualmente cuenta con un sistema básico de autenticación de usuarios mediante:

Registro de usuarios.
Inicio de sesión.
Encriptación de contraseñas.
Generación de tokens de acceso.
Base de datos mediante SQLAlchemy.
Tecnologías utilizadas
Python
FastAPI
SQLAlchemy
SQLite
Pydantic
JWT
Uvicorn
Postman
Git y GitHub
Estructura del proyecto
ARKHE-API/
│
├── App/
│   ├── auth.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
│
├── .gitignore
├── README.md
└── requirements.txt
Instalación

Clonar el repositorio:

git clone https://github.com/alejandrozapata1685/ARKHE-API.git

Entrar a la carpeta:

cd ARKHE-API

Crear y activar el entorno virtual:

python -m venv venv

En Windows:

venv\Scripts\activate

Instalar las dependencias:

pip install -r requirements.txt
Ejecución

Para iniciar la API:

uvicorn App.main:app --reload

La API estará disponible en:

http://127.0.0.1:8001
Documentación

FastAPI genera automáticamente la documentación de la API.

Swagger:

http://127.0.0.1:8001/docs

Redoc:

http://127.0.0.1:8001/redoc
Endpoints actuales
Inicio
GET /

Permite comprobar que la API está funcionando.

Registro
POST /api/auth/register

Permite registrar un nuevo usuario.

Ejemplo:

{
  "nombre": "Juan Perez",
  "email": "juan@gmail.com",
  "password": "12345678"
}
Inicio de sesión
POST /api/auth/login

Permite iniciar sesión utilizando el correo y la contraseña registrados.

Pruebas

Los endpoints pueden probarse utilizando Postman o la documentación interactiva de FastAPI disponible en /docs.

Control de versiones

El proyecto utiliza Git para el control de versiones y GitHub como repositorio remoto.

Autor

Alejandro Zapata

Proyecto académico y de desarrollo para la inmobiliaria ARKHE.