import pytest
from app import app, db
from app.models.datos_model import DatosColombia
from app.controllers import datos_controller as controller # Aseguramos que se importa el controlador

# Configuración para las pruebas
@pytest.fixture(scope='module')
def test_client():
    # Configura la aplicación para el modo de prueba
    app.config['TESTING'] = True
    # Usa una base de datos en memoria para que las pruebas no afecten tu DB real
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        # Crea todas las tablas en la base de datos en memoria
        db.create_all() 
        # Proporciona un cliente de prueba de Flask para interactuar con la aplicación
        yield app.test_client() 
        # Elimina las tablas después de que todas las pruebas del módulo hayan terminado
        db.drop_all() 

# Pruebas unitarias
def test_agregar_dato(test_client):
    with app.app_context():
        # Antes de agregar, la base de datos debería estar vacía
        db.session.query(DatosColombia).delete() # Asegura que la DB esté limpia para esta prueba
        db.session.commit()
        assert DatosColombia.query.count() == 0
        
        # Agregamos un dato usando la función del controlador
        controller.agregar("Entidad de Prueba", "Tema de Prueba", "2025-05-23")
        
        # Verificamos que el dato se agregó correctamente
        assert DatosColombia.query.count() == 1
        dato_agregado = DatosColombia.query.first()
        assert dato_agregado.entidad == "Entidad de Prueba"
        assert dato_agregado.tema == "Tema de Prueba"
        assert dato_agregado.fecha_actualizacion == "2025-05-23"

def test_listar_datos(test_client):
    with app.app_context():
        # Asegurarse de que la DB esté limpia para esta prueba
        db.session.query(DatosColombia).delete()
        db.session.commit()

        # Agregamos algunos datos
        controller.agregar("Entidad A", "Tema X", "2025-01-01")
        controller.agregar("Entidad B", "Tema Y", "2025-01-02")
        
        # Listamos los datos
        resultados = controller.listar()
        
        # Verificamos que la lista contenga los datos agregados
        assert len(resultados) == 2
        # Verificamos que las cadenas de resultados contengan la información esperada
        assert "Entidad: Entidad A" in resultados[0] or "Entidad: Entidad A" in resultados[1]
        assert "Entidad: Entidad B" in resultados[0] or "Entidad: Entidad B" in resultados[1]

def test_eliminar_dato(test_client):
    with app.app_context():
        # Asegurarse de que la DB esté limpia para esta prueba
        db.session.query(DatosColombia).delete()
        db.session.commit()

        # Agregamos un dato para eliminar
        controller.agregar("Entidad a Eliminar", "Tema a Eliminar", "2025-03-01")
        dato_para_eliminar = DatosColombia.query.first()
        
        # Verificamos que el dato exista
        assert DatosColombia.query.count() == 1
        
        # Eliminamos el dato
        controller.eliminar(dato_para_eliminar.id)
        
        # Verificamos que el dato se eliminó
        assert DatosColombia.query.count() == 0

def test_actualizar_dato(test_client):
    with app.app_context():
        # Asegurarse de que la DB esté limpia para esta prueba
        db.session.query(DatosColombia).delete()
        db.session.commit()

        # Agregamos un dato para actualizar
        controller.agregar("Vieja Entidad", "Viejo Tema", "2025-04-01")
        dato_para_actualizar = DatosColombia.query.first()
        
        # Actualizamos el dato
        controller.actualizar(dato_para_actualizar.id, "Nueva Entidad", "Nuevo Tema", "2025-04-02")
        
        # Verificamos que el dato se actualizó correctamente
        dato_actualizado = db.session.query(DatosColombia).get(dato_para_actualizar.id) # Usando .get() directamente en la sesión para evitar warning
        assert dato_actualizado.entidad == "Nueva Entidad"
        assert dato_actualizado.tema == "Nuevo Tema"
        assert dato_actualizado.fecha_actualizacion == "2025-04-02"

# Prueba para la funcionalidad de importar desde API (simplificada)
# Esta prueba no llama a la API real para evitar dependencias externas.
# Se asume que api.obtener_datos() devuelve una lista de diccionarios.
# Para una prueba más robusta de la API, se usaría un mock.
def test_importar_desde_api_local(test_client, monkeypatch):
    with app.app_context():
        db.session.query(DatosColombia).delete()
        db.session.commit()

        # Usamos monkeypatch para simular la respuesta de la API
        # IMPORTANTE: Cambiamos la firma a (*args, **kwargs) para que acepte cualquier argumento
        def mock_obtener_datos(*args, **kwargs):
            return [
                {"responsable": "Entidad A", "actividad": "Actividad 1", "fecha": "2024-01-01"},
                {"responsable": "Entidad B", "actividad": "Nombre:Entidad B Real - Actividad 2", "fecha": "2024-01-02"},
                {"responsable": "Entidad A", "actividad": "Actividad 3", "fecha": "2024-01-03"}
            ]
        
        monkeypatch.setattr(controller.APIClient, 'obtener_datos', mock_obtener_datos)
        
        controller.importar_desde_api()
        
        # Verificamos que los datos se importaron y procesaron correctamente
        assert DatosColombia.query.count() == 3
        # Podemos verificar las entidades extraídas
        entidades_en_db = [d.entidad for d in DatosColombia.query.all()]
        assert "Entidad A" in entidades_en_db
        assert "Entidad B Real" in entidades_en_db # Verifica que extrajo el nombre del 'actividad'

def test_calcular_frecuencia_entidades(test_client):
    with app.app_context():
        db.session.query(DatosColombia).delete()
        db.session.commit()

        # Agregamos datos con diferentes frecuencias
        controller.agregar("Entidad X", "Tema 1", "2025-01-01")
        controller.agregar("Entidad Y", "Tema 2", "2025-01-02")
        controller.agregar("Entidad X", "Tema 3", "2025-01-03")
        controller.agregar("Entidad Y", "Tema 4", "2025-01-04")
        controller.agregar("Entidad X", "Tema 5", "2025-01-05")

        frecuencias = controller.calcular_frecuencia_entidades()
        
        # Convertir a diccionario para fácil verificación
        frecuencias_dict = dict(frecuencias)

        assert frecuencias_dict.get("Entidad X") == 3
        assert frecuencias_dict.get("Entidad Y") == 2
        assert len(frecuencias_dict) == 2 # Solo dos entidades únicas

