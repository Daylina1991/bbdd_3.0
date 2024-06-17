
from obj import usuario 
from bbdd import micursor,miconexion


def menuPrincipal():  #menu_principal
    # on = 1
    # while on == 1:
        print("\nBIENVENIDO A LA APLICACION DE VIDEO/CLUB\n")
        try:
            cliente =int(input("ELIJA UNA OPCION: \n1.Iniciar sesion\n2-Registrarse\n3-Salir\n"))
            if cliente == 1:
                opcion1 =str(input("ingrese su Codigo:\n"))
                micursor.execute(f"select * from clientes  where  codigo ='{opcion1}'")
                result = micursor.fetchall()
                for i in result:
                    print(i)
                opcion2 =str(input("Ingrese su Nombre\n"))
                micursor.execute(f"select * from clientes  where  nombre ='{opcion2}'")
                result = micursor.fetchall()
                for i in result:
                    print(i)
                    # if i == result:
                    #     print(i)
                    # else:
                    #     print("Ingrese un nombre registrado")
                    
                #user1= usuario(i[1],i[2],i[3],i[4])
                user1 = usuario(i[1],i[2],i[3],i[4])
                opcion =int(input("OPCIONES:\n1-Menu de usuario\n2-Menu peliculas\n3-Salir \n"))
                if opcion == 1:
                    print("Este es el menu usuario ")
                    menuUsuario(user1)
                elif opcion == 2:
                    print("Este es el menu Peliculas")
                elif opcion == 3:
                    print("Gracias por usar la aplicacion")
                    quit() 
                else:
                    print("Opcion incorrecta ")
    
                
            elif cliente == 2:
                codigo = str(input("ingrese un codigo de 4 digitos: "))
                nombre = str(input("nombre: "))
                direccion = str(input("dirección: "))
                telefono = str(input("teléfono: "))
                user1 = usuario(codigo, nombre, direccion, telefono)
                user1.darse_de_alta()
                opcion =int(input("OPCIONES:\n1-Menu de usuario\n2-Menu peliculas\n3-Salir \n"))
                if opcion == 1:
                    print("Este es el menu usuario ")
                    menuUsuario(user1)
                elif opcion == 2:
                    print("Este es el menu Peliculas")
                elif opcion == 3:
                    print("Gracias por usar la aplicacion")
                    quit() 
                else:
                    print("Opcion incorrecta ")
                
            elif cliente ==3:
                   quit()
               
            else:
                print("Ingrese una opcion correcta ")
        except ValueError:
            print("Debe ingresar un numero entero ")
            
            
           
                   
                
            
            
def menuUsuario(usuario1):  #menu_usuario
    print("\nMENU USUARIO")
    try:
        modi =int(input("ingrese una opcion:\n1-Ver datos\n2-Modificar datos\n3-Darse de baja\n4-Atras\n"))
        if modi ==1:
           usuario1.ver_datos()
        elif modi ==2:
            dire=int(input("Opciones:\n1-Modificar Direccion\n2-Modificar telefono\n"))
            newdato = str(input("Ingrese un nuevo dato\n"))
            usuario1.modificarDatos(dire,newdato)
        elif modi == 3:
            pass
        
        elif modi  == 4:    #darse_de_baja
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
            
        elif modi == 5:
            pass
        elif modi == 6:
            pass
        else:
            print("Debe ingresar una opcion correcta\n")
    except ValueError:
            print("Debe ingresar un numero entero\n")
           
        
        
            
         

def menuPeliculas():  #menu_peliculas
    on = 1
    while on == 1:
        try:
            opcion =int(input("OPCIONES:\n1-Ver todas las peliculas\n2-Ver solo disponibles\n3-Alquilar Pelicula\n4-Devolver Pelicula\n5"))
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
            