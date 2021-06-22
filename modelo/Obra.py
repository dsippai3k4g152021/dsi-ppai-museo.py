class Obra:
    nombreObra = ''
    codigoSensor = ''
    duracionResumida = 0.0
    duracionExtendida = 0.0
    valuacion = 0.0
    alto = 0.0
    ancho = 0.0
    peso = 0.0
    fechaCreacion = ''
    fechaPrimerIngreso = ''
    empleado_creo = None
    descripcion = ''

    def __init__(self, nombreObra, codigoSensor, duracionResumida, duracionExtendida, valuacion, alto, ancho, peso, fechaCreacion, fechaPrimerIngreso, empleado_creo, descripcion):
        self.nombreObra = nombreObra
        self.codigoSensor = codigoSensor
        self.duracionResumida = duracionResumida
        self.duracionExtendida = duracionExtendida
        self.valuacion = valuacion
        self.alto = alto
        self.ancho = ancho
        self.peso = peso
        self.fechaCreacion = fechaCreacion
        self.fechaPrimerIngreso = fechaPrimerIngreso
        self.empleado_creo = empleado_creo
        self.descripcion = descripcion