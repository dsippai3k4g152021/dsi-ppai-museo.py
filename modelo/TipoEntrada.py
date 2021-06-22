class TipoVisita:
    nombre = ''

    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_nombre(self):
        return self.nombre