from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker

from modelo.Usuario import Usuario
from utilitarios.Connection import Base, engine
from utilitarios.DBSession import DBSession


class Sesion(Base):
    __tablename__ = 'Sesion'

    id = Column(Integer, primary_key=True)
    fecha_inicio = Column(String)
    fecha_fin = Column(String)
    hora_inicio = Column(String)
    hora_fin = Column(String)
    usuario = Column(ForeignKey("Usuario.id"))

    def get_empleado_en_sesion(self):
        db_session = DBSession().get_db_session()

        usuario_actual = db_session.query(Usuario).filter(Usuario.id == self.usuario).first()

        return usuario_actual.obtener_empleado()
