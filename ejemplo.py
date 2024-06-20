from bbdd import miconexion,micursor

def menu():
    print("BIENVENIDO A LA APP")#menu pricipal
    usuario = int(input("OPCIONES:\n1-INICIAR SESION\n2-REGISTARSE\n3-SALIR\n"))
    if usuario ==1:
        datos = iniciarsesion()
        menuUser(datos)
    elif usuario ==2:
        registrarse()
    elif usuario ==3:
        print("GRACIAS POR USAR LA APLICACION")
        quit()#salir
    else:
        print("elija una opcion correcta\n")


def iniciarsesion():
    nombre = str(input("ingrese su nombre\n"))
    password = str(input("Ingrese su password\n"))
    micursor.execute(f"select * from clientes where nombre ='{nombre}' and codigo ='{password}'")
    resultado =micursor.fetchall() #todo lo que encuentra guarda aca en fetchall sinonimo de select de sql
    return resultado
    
    # if micursor.fetchall():
          
    #       resultado = micursor.fetchall()
    #       print(resultado)
    #       return resultado
    # else:
    #     print("Acceso denegado")


def registrarse():
    #codigo = str(input("Ingrese su codigo\n"))
    nombre = str(input("Ingrese su nombre\n"))
    direccion = str(input("Ingrese su direcion\n"))
    telefono = str(input("Ingrese su telefono\n"))
    sql = ("insert into clientes (codigo,nombre,direccion,telefono, situacion ) values (%s,%s,%s,%s, %s)")
    val = ("C011", nombre, direccion, telefono, "L") # codigo y situacion colocamos manual
    micursor.execute(sql, val)
    miconexion.commit()

def menuUser(usuario):
    print("Bienvenido aL MENU USER\n")
    opcion2 =int(input("OPCIONES:\n1-Ver sus datos\n2-Modificar sus datos\n3-Darse de baja\n4-Ver todas las peliculas\n5-Ver solo disponibles\n6-Alquilar pelicula\n7-Devolver pelicula\n8-Atras\n9-SALIR\n"))
    if opcion2 ==1:
        verDatos(usuario)
    elif opcion2 ==2:
        pass#modificar
    elif opcion2 ==3:
        pass#darce de baja
    elif opcion2 ==4:
        pass#ver todas las pelis
    elif opcion2 ==5:
        pass#ver solo disponibles
    elif opcion2 ==6:
        pass#alquilar
    elif opcion2 ==7:
        pass#devolver
    elif opcion2 ==8:
        pass#atras
    elif opcion2 ==9:
        print("GRACIAS POR USAR LA APLICACION")
        quit()#sirve salir
    else:
        print("elija una opcion correcta\n")

def verDatos(user):
    for i in user:
        1
        print(i)

menu()

