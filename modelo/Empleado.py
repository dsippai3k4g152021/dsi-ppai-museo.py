from sqlalchemy import Column, String, ForeignKey, Integer

from utilitarios.Connection import Base
from modelo.Sede import Sede
from utilitarios.DBSession import DBSession

class Empleado(Base):
    __tablename__ = 'Empleado'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    dni = Column(String)
    cuit = Column(String)
    sexo = Column(String)
    fecha_nacimiento = Column(String)
    mail = Column(String)
    telefono = Column(String)
    domicilio = Column(String)
    fecha_ingreso = Column(String)
    codigo_validacion = Column(String)
    sede = Column(ForeignKey("Sede.id"))


    def obtenerSede(self):
        db_session = DBSession().get_db_session()

        #Obtener sede del empleado
        _sede= db_session.query(Sede).filter(Sede.id == self.sede).first()

        return _sede
