class Entrada:
    numero = 0
    fecha_venta = ''
    hora_venta = ''
    monto = 0.0
    sede = None
    tarifa = None

    def __init__(self, numero, fecha_venta, hora_venta, monto, sede, tarifa):
        self.numero = numero
        self.fecha_venta = fecha_venta
        self.hora_venta = hora_venta
        self.monto = monto
        self.sede = sede
        self.tarifa = tarifa
