from config import db

class Curso(db.Model):
    __tablename__ = 'cursos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255), nullable=True)

    # Relación con Estudiante
    estudiantes = db.relationship('Estudiante', backref='curso', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'estudiantes': [estudiante.to_dict() for estudiante in self.estudiantes]
        }
