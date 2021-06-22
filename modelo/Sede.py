from sqlalchemy import Column, String, Integer

from modelo.Tarifas import Tarifas
from modelo.Exposicion import Exposicion
from utilitarios.DBSession import DBSession
from utilitarios.Connection import Base


class Sede(Base):
    __tablename__ = 'Sede'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    cant_maxima_por_guia = Column(Integer)
    cant_maxima_visitantes = Column(Integer)
    tarifas = [1,2,3]
    exposiciones = [1,2,3]

    def obtenerTarifasVigentes(self):
        db_session = DBSession().get_db_session()  
        _tarifas=[] 

        #Obtenemos todas las Tarifas que pertenecen a la sede actual
        for i in self.tarifas:
            #Obtenemos una tarifa a la vez por ID
            tarifa=db_session.query(Tarifas).filter(Tarifas.id == self.tarifas[i]).first()
            #Obtenemos los datos de la tarifa
            _tarifas.append(tarifa.mostrarMontosVigentes())
        return _tarifas

    def calcularDuracionaAExposicionesVigentes(self):
        db_session = DBSession().get_db_session()  
        _exposiciones=[] 

        #Obtenemos todas las exposiciones vigentes que pertenecen a la sede actual
        for i in self.exposiciones:
            #Obtenemos una exposicion a la vez por ID
            exposicion=db_session.query(Exposicion).filter(Exposicion.id == self.exposiciones[i]).first()
            #Obtenemos la exposicion si es Vigente
            _exposiciones.append(exposicion.esVigente())

        return _exposiciones