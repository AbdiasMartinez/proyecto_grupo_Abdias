from app import db

class DatosColombia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entidad = db.Column(db.String(150))
    tema = db.Column(db.String(150))
    fecha_actualizacion = db.Column(db.String(50))