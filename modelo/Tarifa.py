class Tarifa:
    fecha_inicio_vigencia = ''
    fecha_fin_vigencia = ''
    monto = 0.0
    monto_adicional_guia = 0.0
    tipo_entrada = None
    tipo_visita = None

    def __init__(self, fecha_inicio_vigencia, fecha_fin_vigencia, monto, monto_adicional_guia, tipo_entrada, tipo_visita):
        self.fecha_inicio_vigencia = fecha_inicio_vigencia
        self.fecha_fin_vigencia = fecha_fin_vigencia
        self.monto = monto
        self.monto_adicional_guia = monto_adicional_guia
        self.tipo_entrada = tipo_entrada
        self.tipo_visita = tipo_visita
