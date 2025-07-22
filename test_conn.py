from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

# Cambia esto por tu URL real de conexión, sin caracteres problemáticos
DATABASE_URL = "postgresql://postgres:TuContraseñaAquí@db.egcyccjxnzboevxmrmub.supabase.co:5432/postgres"

def test_connection():
    try:
        engine = create_engine(DATABASE_URL)
        # Intenta conectar y ejecutar un query sencillo
        with engine.connect() as connection:
            result = connection.execute("SELECT NOW();")
            for row in result:
                print("Conexión exitosa, hora actual:", row[0])
    except OperationalError as e:
        print("Error de conexión:", e)

if __name__ == "__main__":
    test_connection()
