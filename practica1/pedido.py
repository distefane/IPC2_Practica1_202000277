class Pedido():
    def __init__(self, nombre_cliente, telefono_cliente, cantidad, tipo):
        self.nombre_cliente = nombre_cliente
        self.telefono_cliente = telefono_cliente
        self.cantidad = cantidad
        self.tipo = tipo
        self.tiempo = None
        self.siguiente = None