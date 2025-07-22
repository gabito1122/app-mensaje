# Importamos librerías necesarias
from sqlalchemy import create_engine           # Motor para conectar con la base de datos
from sqlalchemy.ext.declarative import declarative_base  # Para crear modelos (tablas)
from sqlalchemy.orm import sessionmaker         # Para abrir sesiones de consulta
from dotenv import load_dotenv                   # Para cargar variables del archivo .env
import os                                        # Para leer variables de entorno

# Carga las variables del archivo .env automáticamente
load_dotenv()

# Lee la URL de conexión a la base de datos desde la variable de entorno
DATABASE_URL = os.getenv("DATABASE_URL")

# Crea el "engine" que maneja la conexión a la base de datos PostgreSQL
engine = create_engine(DATABASE_URL)

# Crea una clase Base para crear tus modelos (tablas)
Base = declarative_base()

# Crea una "fábrica" para abrir sesiones (consultas) a la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función para usar en cada petición y cerrar sesión después
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
