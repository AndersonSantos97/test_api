from sqlalchemy import Column, Integer, String
from .conexion import Base

class Nationalities(Base):
    __tablename__ = "nationalities"
    id = Column(Integer, primary_key=True, index=True)
    abreviacion = Column(String(10))
    descripcion = Column(String(100))
    

    