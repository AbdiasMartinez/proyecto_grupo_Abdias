from app import db
from app.models.datos_model import DatosColombia
from app.services.api_service import APIClient
from sqlalchemy import func
import re

def listar():
    datos = DatosColombia.query.all()
    resultados = []
    for dato in datos:
        resultados.append(f"ID: {dato.id} - Entidad: {dato.entidad} | Tema: {dato.tema} | Fecha: {dato.fecha_actualizacion}")
    return resultados

def agregar(entidad, tema, fecha):
    nuevo = DatosColombia(entidad=entidad, tema=tema, fecha_actualizacion=fecha)
    db.session.add(nuevo)
    db.session.commit()

def actualizar(id, entidad, tema, fecha):
    dato = DatosColombia.query.get(id)
    if dato:
        dato.entidad = entidad
        dato.tema = tema
        dato.fecha_actualizacion = fecha
        db.session.commit()

def eliminar(id):
    dato = DatosColombia.query.get(id)
    if dato:
        db.session.delete(dato)
        db.session.commit()

def importar_desde_api():
    api = APIClient()
    datos_api = api.obtener_datos(limit=500)
    if datos_api:
        for item in datos_api:
            nombre_entidad_en_actividad = None
            actividad = item.get("actividad", "")
            match = re.search(r"Nombre:(.+?) -", actividad)
            if match:
                nombre_entidad_en_actividad = match.group(1).strip()

            entidad = nombre_entidad_en_actividad if nombre_entidad_en_actividad else item.get("responsable", "Desconocido")
            tema = actividad
            fecha = item.get("fecha", "Sin fecha")

            if not DatosColombia.query.filter_by(entidad=entidad, tema=tema).first():
                nuevo = DatosColombia(entidad=entidad, tema=tema, fecha_actualizacion=fecha)
                db.session.add(nuevo)
        db.session.commit()
        print("Datos importados correctamente.")
    else:
        print("No se recibieron datos de la API.")

def calcular_frecuencia_entidades():
    frecuencias = db.session.query(DatosColombia.entidad, func.count(DatosColombia.id)).group_by(DatosColombia.entidad).all()
    return frecuencias

def mostrar_frecuencia_entidades():
    frecuencias = calcular_frecuencia_entidades()
    if frecuencias:
        print("\n--- Frecuencia de Publicación por Entidad ---")
        for entidad, cantidad in frecuencias:
            print(f"Entidad: {entidad} - Publicaciones: {cantidad}")
        print("-------------------------------------------\n")
    else:
        print("\nNo hay datos para calcular la frecuencia.\n")