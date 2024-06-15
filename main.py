
from obj import usuario 
from bbdd import micursor,miconexion


def menuPrincipal():  #menu_principal
    on = 1
    while on == 1:
        print("\nBIENVENIDO A LA APLICACION DE VIDEO/CLUB\n")
        try:
            opcion1 =str(input("ingrese su codigo: \n"))
            micursor.execute(f"select * from clientes  where  codigo ='{opcion1}'")
            result = micursor.fetchall()
            for i in result:
                print(i)
            user1 = usuario(i[1],i[2],i[3],i[4])
            print(user1)
            print(user1.get_nombre())
            opcion =int(input("OPCIONES:\n1-Menu de usuario\n2-Menu peliculas\n3-Salir \n"))
            if opcion == 1:
                print("Este es el menu usuario ")
                menuUsuario()
            elif opcion == 2:
                print("Este es el menu Peliculas")
            elif opcion == 3:
                print("Gracias por usar la aplicacion")
                #quit() 
                on = 0  
            else:
                print("Opcion incorrecta ")
        except ValueError:
            print("Debe ingresar un numero entero ")
            


def menuUsuario():  #menu_usuario
    print("\nMENU USUARIO")
    try:
        cliente= int(input("OPCIONES:\n1-darse de alta\n2-Modificar datos\n3-Ver datos\n4-Darse de baja\n"))
        if  cliente == 1:
            codigo = str(input("codigo "))
            nombre = str(input("nombre: "))
            direccion = str(input("dirección: "))
            telefono = str(input("teléfono: "))
            user1 = usuario(codigo, nombre, direccion, telefono)
            user1.darse_de_alta()

        elif cliente == 2:  #modificar datos
            direccion = str(input("Ingrese la direccion: "))
            telefono = int(input("Ingrese  el  telefono: "))
            usuario1 = usuario(direccion, telefono)
            usuario1.modificarDatos()

        # elif cliente = 3: #ver_datos
        #       pass

        elif cliente  == 4:    #darse_de_baja
            lista =[]
            user = str(input("ingrese su codigo: "))
            sql = (f"select * from clientes where codigo = '{user}'")
            micursor.execute(sql)
            result = micursor.fetchall()
            for i in result:
                for j in i:
                    lista.append(j)
            user1 = usuario(lista[1],lista[2],lista[3],lista[4])
            user1.darse_de_baja()

            
        else:
            pass
    except ValueError:
            print("Debe ingresar un numero entero")  

def menuPeliculas():  #menu_peliculas
    on = 1
    while on == 1:
        print("\nMENU PELICULAS\n")
        try:
            opcion =int(input("OPCIONES:\n1-Ver todas las peliculas\n2-Ver solo disponibles\n3-Alquilar Pelicula\n4-Devolver Pelicula \n"))
            if opcion == 1:
                pass  #ver_peliculas
            elif opcion == 2:
                pass
            elif opcion == 3:
               pass
            elif opcion == 4:
                pass
                #quit() 
                on = 0  
            else:
                print("Opcion incorrecta ")
        except ValueError:
            print("Debe ingresar un numero entero ")
            


menuPrincipal()