from sqlalchemy import Column, Integer, String, ForeignKey

from modelo.Empleado import Empleado
from utilitarios.Connection import Base
from utilitarios.DBSession import DBSession


class Usuario(Base):
    __tablename__ = 'Usuario'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    contrasena = Column(String)
    caducidad = Column(Integer)
    empleado = Column(ForeignKey("Empleado.id"))

    def obtener_empleado(self):
        db_session = DBSession().get_db_session()

        empleado_actual = db_session.query(Empleado).filter(Empleado.id == self.empleado).first()

        return empleado_actual

