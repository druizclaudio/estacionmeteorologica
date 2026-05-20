from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "Hola mundo"}

@app.get("/usuarios")
def obtener_usuarios():
    return [
        {"id": 1, "nombre": "Ana"},
        {"id": 2, "nombre": "Luis"}
    ]

@app.get("/usuarios/{usuario_id}")
def obtener_usuario(usuario_id: int):
    return {"id": usuario_id}

from pydantic import BaseModel

class Usuario(BaseModel):
    nombre: str
    edad: int

@app.post("/usuarios")
def crear_usuario(usuario: Usuario):
    return {
        "mensaje": "Usuario creado",
        "usuario": usuario
    }

class DatosMeteorologicos(BaseModel):
    temperatura: float
    presion: float

@app.get("/datos")
def ver_datos(temperatura: float, presion: float):
    return {
        "mensaje": "Datos meteorológicos obtenidos",
        "temperatura": temperatura,
        "presion": presion
    }
