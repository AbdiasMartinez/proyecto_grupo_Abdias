import pytest
from app import app, db
from app.models.datos_model import DatosColombia
from app.controllers import datos_controller as controller

@pytest.fixture(scope='module')
def test_client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all() 
        yield app.test_client() 
        db.drop_all() 

def test_agregar_dato(test_client):
    with app.app_context():
        db.session.query(DatosColombia).delete()
        db.session.commit()
        assert DatosColombia.query.count() == 0
        
        controller.agregar("Entidad de Prueba", "Tema de Prueba", "2025-05-23")
        
        assert DatosColombia.query.count() == 1
        dato_agregado = DatosColombia.query.first()
        assert dato_agregado.entidad == "Entidad de Prueba"
        assert dato_agregado.tema == "Tema de Prueba"
        assert dato_agregado.fecha_actualizacion == "2025-05-23"

def test_listar_datos(test_client):
    with app.app_context():
        db.session.query(DatosColombia).delete()
        db.session.commit()

        controller.agregar("Entidad A", "Tema X", "2025-01-01")
        controller.agregar("Entidad B", "Tema Y", "2025-01-02")
        
        resultados = controller.listar()
        
        assert len(resultados) == 2
        assert "Entidad: Entidad A" in resultados[0] or "Entidad: Entidad A" in resultados[1]
        assert "Entidad: Entidad B" in resultados[0] or "Entidad: Entidad B" in resultados[1]

def test_eliminar_dato(test_client):
    with app.app_context():
        db.session.query(DatosColombia).delete()
        db.session.commit()

        controller.agregar("Entidad a Eliminar", "Tema a Eliminar", "2025-03-01")
        dato_para_eliminar = DatosColombia.query.first()
        
        assert DatosColombia.query.count() == 1
        
        controller.eliminar(dato_para_eliminar.id)
        
        assert DatosColombia.query.count() == 0

def test_actualizar_dato(test_client):
    with app.app_context():
        db.session.query(DatosColombia).delete()
        db.session.commit()

        controller.agregar("Vieja Entidad", "Viejo Tema", "2025-04-01")
        dato_para_actualizar = DatosColombia.query.first()
        
        controller.actualizar(dato_para_actualizar.id, "Nueva Entidad", "Nuevo Tema", "2025-04-02")
        
        dato_actualizado = db.session.query(DatosColombia).get(dato_para_actualizar.id)
        assert dato_actualizado.entidad == "Nueva Entidad"
        assert dato_actualizado.tema == "Nuevo Tema"
        assert dato_actualizado.fecha_actualizacion == "2025-04-02"

def test_importar_desde_api_local(test_client, monkeypatch):
    with app.app_context():
        db.session.query(DatosColombia).delete()
        db.session.commit()

        def mock_obtener_datos(*args, **kwargs):
            return [
                {"responsable": "Entidad A", "actividad": "Actividad 1", "fecha": "2024-01-01"},
                {"responsable": "Entidad B", "actividad": "Nombre:Entidad B Real - Actividad 2", "fecha": "2024-01-02"},
                {"responsable": "Entidad A", "actividad": "Actividad 3", "fecha": "2024-01-03"}
            ]
        
        monkeypatch.setattr(controller.APIClient, 'obtener_datos', mock_obtener_datos)
        
        controller.importar_desde_api()
        
        assert DatosColombia.query.count() == 3
        entidades_en_db = [d.entidad for d in DatosColombia.query.all()]
        assert "Entidad A" in entidades_en_db
        assert "Entidad B Real" in entidades_en_db

def test_calcular_frecuencia_entidades(test_client):
    with app.app_context():
        db.session.query(DatosColombia).delete()
        db.session.commit()

        controller.agregar("Entidad X", "Tema 1", "2025-01-01")
        controller.agregar("Entidad Y", "Tema 2", "2025-01-02")
        controller.agregar("Entidad X", "Tema 3", "2025-01-03")
        controller.agregar("Entidad Y", "Tema 4", "2025-01-04")
        controller.agregar("Entidad X", "Tema 5", "2025-01-05")

        frecuencias = controller.calcular_frecuencia_entidades()
        
        frecuencias_dict = dict(frecuencias)

        assert frecuencias_dict.get("Entidad X") == 3
        assert frecuencias_dict.get("Entidad Y") == 2
        assert len(frecuencias_dict) == 2