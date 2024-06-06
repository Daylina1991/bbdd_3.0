def menu():
    while True:
        print("\nGestión de Clientes")
        print("1. crear usuario")
        print("2. eliminar usuario")
        print("3. Eliminar usuario")
        print("4. Actualizar usuario")
        print("5. Salir")
        usuario = input("Seleccione una opción: ")
        if usuario == 1:
            codigo = int(input("codigo "))
            nombre = str(input("nombre: "))
            direccion = str(input("dirección: "))
            telefono = int(input("teléfono: "))
            situacion = str(input("situacion: "))
            codigo_peli = int(input("codigo_peli: "))
        elif usuario == 2:
            
        elif usuario == 3:
            id = int(input("ID del cliente a eliminar: "))
        elif usuario== 4:
            id = int(input("ID del cliente a actualizar: "))
            codigo = input("nuevo código: ")
            nombre = input("nuevo nombre: ")
            direccion = input("nueva dirección: ")
            telefono = input("nuevo teléfono: ")
            situacion = input("nueva situacion: ")
        elif usuario == 5:
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    menu()
