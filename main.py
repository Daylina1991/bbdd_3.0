
from obj import obj
def menuPrincipal():
    on = 1
    while on == 1:
        print("\n BIENVENIDO A LA APLICACION DE VIDEO/CLUB")
        try:
            opcion =int(input("Opciones: 1-Menu de usuario\n2-Menu peliculas\n3-Salir "))
            if opcion == 1:
                print("Este es el menu usuario ")
            elif opcion == 2:
                print("Este es el menu Peliculas")
            elif opcion == 3:
                print("Gracias por usar la aplicacion")
                quit()
            else:
                print("Opcion incorrecta ")
        except ValueError:
            print("Debe ingresar un numero entero ")
def menuUsuario():
    try:
        print("\n Este es el menu usuario")
        usuario = int(input("Opciones \n 1- Ver datos\n2-Modificar datos\nDarse de baja "))
            if usuario == 1:
                codigo = int(input("codigo "))
                nombre = str(input("nombre: "))
                direccion = str(input("dirección: "))
                telefono = int(input("teléfono: "))
                situacion = str(input("situacion: "))
                codigo_peli = int(input("codigo_peli: "))
            elif usuario == 2:
                 id = int(input("ID del cliente a eliminar: "))
                
            elif usuario  == 3:
                pass
            else:
                pass
    except ValueError:
            print("Debe ingresar un numero entero  hola")  