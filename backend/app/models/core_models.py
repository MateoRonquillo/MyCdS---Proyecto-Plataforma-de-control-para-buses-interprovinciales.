from sqlalchemy import Column, Integer, String, Boolean
from app.db.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(100), unique=True, index=True, nullable=False)
    cedula = Column(String(15), unique=True, nullable=False)
    rol = Column(String(50), nullable=False)
    activo = Column(Boolean, default=True)

class Cooperativa(Base):
    __tablename__ = "cooperativas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), unique=True, nullable=False)
    logo_url = Column(String(255), nullable=True)
    color_principal = Column(String(7), nullable=True)