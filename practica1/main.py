from lista_enlazada import ListaEnlazada

ingreso = ListaEnlazada()

while True:
    print("Hola, ingresa el número de la acción que deseas realizar:")
    print("1. Crear pedido.")
    print("2. Entregar pedido.")
    print("3. Ver datos del desarrollador.")
    print("4. Salir.")
    opcion = int(input("Opción: "))
    if opcion == 1:
        print("Ingresa los datos del pedido:")
        nombre_cliente = input("Nombre del cliente: ")
        telefono_cliente = int(input("Teléfono del cliente: "))
        cantidad = int(input("Cantidad de productos: "))
        tipo = input("Tipo de producto: ")
        ingreso.agregarUltimo(nombre_cliente, telefono_cliente, cantidad, tipo)
        ingreso.recorrido()
    elif opcion == 2:
        ingreso.eliminar_pedido()
        ingreso.recorrido()
    elif opcion == 3:
        print("Estudiante: Diana Berducido.")
        print("Carnet: 202000277")
    elif opcion == 4:
        print("Gracias por utilizar el programa.")
        break
