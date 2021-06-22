from modelo.Sesion import Sesion
from utilitarios.DBSession import DBSession


class GestorVentaEntrada:
    entradas = []
    empleado_logueado = None
    sesion_actual = None
    tarifas = []
    exposiciones = []
    sede = None
    pantalla_venta_entrada = None

    def tomar_op_registrar_ventas(self, pantalla_venta_entrada):
        self.pantalla_venta_entrada = pantalla_venta_entrada

        self.buscar_empleado_logueado()

        self.buscar_sede()

    def buscar_empleado_logueado(self):
        db_session = DBSession().get_db_session()
        self.sesion_actual = db_session.query(Sesion).first()

        self.empleado_logueado = self.sesion_actual.get_empleado_en_sesion()



    def buscarSede(self):
        #Obtener sede a traves del empleado logueado
        self.sede=self.empleado_logueado.obtenerSede()
        
    def buscarTarifasDeSede(self):
        #Obtener Tarifas de la sede actual
        self.tarifas=self.sede.obtenerTarifasVigentes()

    def BuscarExposicionVigente():

        self.exposiciones=self.sede.calcularDuracionaAExposicionesVigentes()

         # sesion = Sesion(id=1, fecha_inicio='20', fecha_fin='21', hora_inicio='22', hora_fin='23', usuario=1)
        # usuario = Usuario(id=1, nombre='jdoe', contrasena='pass123', caducidad=10, empleado=1)
        # empleado = Empleado(id=1, nombre='John', apellido='Doe', dni='1000000', cuit='20-1000000-7', sexo='M', fecha_nacimiento='01/01/1990', mail='jdoe@gmail.com', telefono='0014223344', domicilio='test address', fecha_ingreso='01/01/2020', codigo_validacion='ax20', sede=1)
        # sede = Sede(id=1, nombre='Museo Pictórico de Córdoba', cant_maxima_por_guia=5, cant_maxima_visitantes=100)
        #
        #
        # self.connection.add(sesion)
        # self.connection.add(usuario)
        # self.connection.add(empleado)
        # self.connection.add(sede)
        # self.connection.commit()

