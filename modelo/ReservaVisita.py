class ReservaVisita:
    numero_reserva = 0
    cantidad_alumnos = 0
    cantidad_alumnos_confirmada = 0
    duracion_estimada = 0
    fecha_hora_creacion = ''
    fecha_hora_reserva = ''
    hora_fin_real = ''
    hora_inicio_real = ''
    sede = None

    def __init__(self, numero_reserva, cantidad_alumnos, cantidad_alumnos_confirmada, duracion_estimada, fecha_hora_creacion, fecha_hora_reserva, hora_fin_real, hora_inicio_real, sede):
        self.numero_reserva = numero_reserva
        self.cantidad_alumnos = cantidad_alumnos
        self.cantidad_alumnos_confirmada = cantidad_alumnos_confirmada
        self.duracion_estimada = duracion_estimada
        self.fecha_hora_creacion = fecha_hora_creacion
        self.fecha_hora_reserva = fecha_hora_reserva
        self.hora_fin_real = hora_fin_real
        self.hora_inicio_real = hora_inicio_real
        self.sede = sede



