from interfaz.PantallaVentaEntrada import PantallaVentaEntrada
from utilitarios.Connection import Base, engine


if __name__ == '__main__':
#    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    pantalla_venta_entrada = PantallaVentaEntrada()
    pantalla_venta_entrada.tomar_op_venta_entradas()
