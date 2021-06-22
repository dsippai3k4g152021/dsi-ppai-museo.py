from modelo.TipoEntrada import TipoEntrada
from modelo.TipoVisita import TipoVisita
from utilitarios.DBSession import DBSession


class Tarifa:
    fecha_inicio_vigencia = ''
    fecha_fin_vigencia = ''
    monto = 0.0
    monto_adicional_guia = 0.0
    tipo_entrada = None
    tipo_visita = None

    def mostrarMontosVigentes(self):
        db_session = DBSession().get_db_session()
        #Obtener tipo de entrada
        self.tipo_entrada=db_session.query(TipoEntrada).filter(TipoVisita.id == self.tipo_entrada).first()

        #Obtener tipo de visita
        self.tipo_visita=db_session.query(TipoVisita).filter(TipoVisita.id == self.tipo_visita).first()

        #VERIFICAR RETORNO ENTRE TODOS
        return [self.tipo_entrada.MostrarNombre(),self.tipo_visitaMostrarNombre()]