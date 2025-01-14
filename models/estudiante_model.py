from config import db

class Estudiante(db.Model):
    __tablename__ = 'estudiantes'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)

    # Clave foránea
    curso_id = db.Column(db.Integer, db.ForeignKey('cursos.id'), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'correo': self.correo,
            'curso_id': self.curso_id
        }
