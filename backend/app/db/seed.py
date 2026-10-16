from app.db.database import SessionLocal
from app.models.core_models import Usuario, Cooperativa

def run_seed():
    db = SessionLocal()
    try:
        # Verificar si ya existen datos para no duplicarlos
        if db.query(Usuario).first():
            print("Los datos semilla ya existen en la base de datos. Omitiendo...")
            return

        print("Insertando datos semilla...")
        
        # Crear Cooperativas de prueba
        coop1 = Cooperativa(nombre="Flota Pelileo", color_principal="#FF5733")
        coop2 = Cooperativa(nombre="Cooperativa Baños", color_principal="#003366")
        db.add_all([coop1, coop2])

        # Crear Usuarios de prueba (Incluyéndote a ti como admin)
        admin = Usuario(nombre="Estiven Chiluisa", correo="admin@pasajes.ec", cedula="1800000000", rol="admin")
        cliente = Usuario(nombre="Juan Perez", correo="juan@correo.com", cedula="1700000000", rol="cliente")
        db.add_all([admin, cliente])

        db.commit()
        print("¡Datos semilla insertados con éxito!")
    except Exception as e:
        db.rollback()
        print(f"Error al insertar datos: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    run_seed()