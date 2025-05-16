from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EntidadPublica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    sector = db.Column(db.String(100))
    fecha_ultima_actualizacion = db.Column(db.Date)
    frecuencia_publicacion = db.Column(db.String(50))
    cumple_publicacion = db.Column(db.Boolean, default=False)
    estado = db.Column(db.String(200))  # Ej: "Cumple a tiempo", "Incumplimiento", "Retraso leve"
