from sqlalchemy import Column, String, Integer

from utilitarios.Connection import Base


class Sede(Base):
    __tablename__ = 'Sede'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    cant_maxima_por_guia = Column(Integer)
    cant_maxima_visitantes = Column(Integer)
    tarifas = []
    exposiciones = []
