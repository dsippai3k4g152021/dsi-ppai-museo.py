from controlador.GestorVentaEntrada import GestorVentaEntrada


class PantallaVentaEntrada:
    cant_entrada = 0
    combo_tarifas = ''
    entradas = []
    tarifas_seleccionadas = []
    gestor_venta_entrada = None

    def tomar_op_venta_entradas(self):
        self.habilitar_ventana()

        self.gestor_venta_entrada = GestorVentaEntrada()

        self.gestor_venta_entrada.tomar_op_registrar_ventas(self)


    def habilitar_ventana(self):
        pass

    def mostrar_nombre_apellido_empleado(self):
        pass



