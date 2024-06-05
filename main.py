def menu():
    Cliente.crear_tabla()  # Asegurarse de que la tabla está creada
    while True:
        print("\nGestión de Clientes")
        print("1. Agregar cliente")
        print("2. Ver clientes")
        print("3. Eliminar cliente")
        print("4. Actualizar cliente")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre: ")
            codigo = input("Código: ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            cliente = Cliente(nombre, codigo, direccion, telefono, email)
            cliente.agregar()
        elif opcion == '2':
            clientes = Cliente.obtener_todos()
            for cliente in clientes:
                print(cliente)
        elif opcion == '3':
            id = int(input("ID del cliente a eliminar: "))
            Cliente.eliminar(id)
        elif opcion == '4':
            id = int(input("ID del cliente a actualizar: "))
            nombre = input("Nuevo nombre: ")
            codigo = input("Nuevo código: ")
            direccion = input("Nueva dirección: ")
            telefono = input("Nuevo teléfono: ")
            email = input("Nuevo email: ")
            Cliente.actualizar(id, nombre, codigo, direccion, telefono, email)
        elif opcion == '5':
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    menu()
