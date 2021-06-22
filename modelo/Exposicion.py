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


    def esVigente(self):
        fechaActual=""
        #Verificamos vigencia de la exposicion
        if(self.fecha_fin > fechaActual and self.fecha_inicio < fechaActual):{
            return self
        }




