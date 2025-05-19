import unittest
from flask import Flask
from app.controllers.datos_controller import DatosController
from app.models.datos_model import db

class TestDatosController(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.controller = DatosController(self.app)

    def test_agregar_listar(self):
        self.controller.agregar('Entidad', 123.45)
        datos = self.controller.listar()
        self.assertEqual(len(datos), 1)
        self.assertEqual(datos[0].nombre_entidad, 'Entidad')

    def test_actualizar(self):
        nuevo = self.controller.agregar('E1', 1.0)
        actualizado = self.controller.actualizar(nuevo.id, 'E2', 2.0)
        self.assertEqual(actualizado.nombre_entidad, 'E2')

    def test_eliminar(self):
        nuevo = self.controller.agregar('E', 5.0)
        res = self.controller.eliminar(nuevo.id)
        self.assertTrue(res)
        self.assertEqual(len(self.controller.listar()), 0)