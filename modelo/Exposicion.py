class Exposicion:
    nombre = ''
    hora_apertura = ''
    hora_cierre = ''
    fecha_inicio = ''
    fecha_fin = ''
    fecha_inicio_replanificada = ''
    fecha_fin_replanificada = ''
    empleado_creo = None
    detalle_exposicion = []

    def __init__(self, nombre, hora_apertura, hora_cierre, fecha_inicio, fecha_fin, fecha_inicio_replanificada, fecha_fin_replanificada, empleado_creo, detalle_exposicion):
        self.nombre = nombre
        self.hora_apertura = hora_apertura
        self.hora_cierre = hora_cierre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.fecha_inicio_replanificada = fecha_inicio_replanificada
        self.fecha_fin_replanificada = fecha_fin_replanificada
        self.empleado_creo = empleado_creo
        self.detalle_exposicion = detalle_exposicion





