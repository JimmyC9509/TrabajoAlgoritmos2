from flask_sqlalchemy import SQLAlchemy

# Variables para la configuracion
DB_USERNAME = 'root'
DB_PASSWORD = ''
DB_HOST = 'localhost'
DB_NAME = 'gestion_estudiantes'

# Configuracion de la base de datos
DATABASE_URI = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
db = SQLAlchemy()
