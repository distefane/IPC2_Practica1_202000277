from pedido import Pedido
from os import system

class ListaEnlazada():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esta_vacia(self):
        return self.primero == None
    
    #Falta agregar la impresión del graphviz
    def agregarUltimo(self,nombre_cliente, telefono_cliente, cantidad, tipo):
        nuevo=Pedido(nombre_cliente, telefono_cliente, cantidad, tipo) 

        

        if str(nuevo.tipo) == "6 Galletas con Cobertura":
            tiempo = 1
        elif str(nuevo.tipo) == "Rosca Danesa":
            tiempo = 2
        elif str(nuevo.tipo) == "Pastel de Frutas":
            tiempo = 2.5
        elif str(nuevo.tipo) == "Galletas de Jengibre":
            tiempo = 0.5
        elif str(nuevo.tipo) == "Cupcakes Navideños":
            tiempo = 1.5
        else:
            print("No se ha ingresado un tipo de producto válido.")
            print("Por favor, ingrese uno de los siguientes:") 
            print("6 Galletas con Cobertura, Rosca Danesa, Pastel de Frutas,")
            print("Galletas de Jengibre, Cupcakes Navideños.")
            print("Escríbalo tal y como se muestra en la lista.")
            nuevo.tipo = input("Tipo de producto: ")
            if str(nuevo.tipo) == "6 Galletas con Cobertura":
                tiempo = 1
            elif str(nuevo.tipo) == "Rosca Danesa":
                tiempo = 2
            elif str(nuevo.tipo) == "Pastel de Frutas":
                tiempo = 2.5
            elif str(nuevo.tipo) == "Galletas de Jengibre":
                tiempo = 0.5
            elif str(nuevo.tipo) == "Cupcakes Navideños":
                tiempo = 1.5

        temp = self.primero        
        nuevo.tiempo = tiempo * nuevo.cantidad 

        if temp is None:
            self.primero = self.ultimo = nuevo
        else:
            temp = self.primero
            while temp.siguiente is not None:
                    temp=temp.siguiente
            
            temp.siguiente=nuevo
            global tiempo_nodos
            tiempo_nodos = 0
            while temp != None:
                tiempo_nodos += temp.tiempo
                temp = temp.siguiente
            
            nuevo.tiempo = tiempo_nodos
            
    def env_nombres(self):
        temp=self.primero
        cadena = ""
        while temp != None:
            if temp.siguiente is not None:
                cadena += "Cliente: " + str(temp.nombre_cliente) + "," + " Pedido: " + str(temp.tipo) + "," + " Tiempo de Espera: " + str(temp.tiempo)  + "|"
            else:
                cadena += "Cliente: " + str(temp.nombre_cliente) + "," + " Pedido: " + str(temp.tipo) + "," + " Tiempo de Espera: " + str(temp.tiempo)
            temp=temp.siguiente
        return cadena

    def eliminar_pedido(self):
        #Eliminar primer nodo de la lista
        if self.esta_vacia()==True:
            print("La lista está vacía")
        else:
            para_borrar = self.primero.tiempo
            temp = self.primero
            self.primero = temp.siguiente
            temp.siguiente = None
            #restarle el tiempo del nodo eliminado a los demás nodos
        temp=self.primero
        while temp != None:
            temp.tiempo -= para_borrar
            temp=temp.siguiente

    def recorrido(self):
        temp=self.primero
        while temp != None:
            print(temp.nombre_cliente,temp.telefono_cliente,temp.cantidad, temp.tipo, temp.tiempo)
            temp=temp.siguiente
            self.generar_graphviz()
        self.generar_graphviz()
        
    def generar_graphviz(self):
        nombres = self.env_nombres()
        if nombres == "":
            nombres = "Todos los pedidos fueron entregados."
        #primera impresión
        pedidos1 = """digraph structs {

        n1 [label=\""""

        pedidos2 = f"""{nombres}"""
        pedidos3 = """\" shape=record];

    }"""

        pedidos = pedidos1 + pedidos2 + pedidos3
        print("la cadena de jugadores completos es:", pedidos)
        generar1 = open("pedidos.dot", "w")
        generar1.write(pedidos)
        generar1.close()
        system("dot -Tpng pedidos.dot -o pedidos.png")
        system("cd ./pedidos.png")