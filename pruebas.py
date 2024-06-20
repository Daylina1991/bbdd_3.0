

def traerDatos(comodin):
    cursor.execute(f"select * from{comodin}")   # comodin para utilizar de manera generica
    variable = cursor.fetchall()  #imprime todo,se utiliza como un print
    for i in range #len(variable):   #len cuenta
        print(i)


traerDatos("Productos ")
traerDatos("clientes ")

def Modificar(comodin1,comodin2, comodin3, comodin4,comodin5 ):    #modificar de productos,utilizamos parametros para actulizar.
    cursor.execute(f"update  {comodin1} set {comodin2} = {'television'} where {comodin4}={comodin5}")  #actualizamos datos  # pasamos  como variables
    conexion.commit()  #serramos sentencia con commit

Modificar("clientes", "clientes", "lucas", "hdg", 5)



def alquilar(x,y):
    cursor.execute(f"update clientes set situacion = 'a' where  id = {x}")
    cursor.execute(f"update clientes set codigo  = 'y' where  id = {x}")
    cursor.execute(f"update peliculas set situacion = 'a' where  id = {y}")   # el cambio de estado de pelliculas y cliente 
    cursor.execute(f"update peliculas set dni = 'x' where  id = {y}")
    conn.commit()
alquilar(1,1)

def devolver(x,y):
    cursor.execute(f"update clientes set situacion ='l' where id = {x}")
    cursor.execute(f"update clientes set codigo  ='null' where id = {x}")
    cursor.execute(f"update peliculas set situacion ='l' where id = {y}")    #id es igual al id de la pelicula
    cursor.execute(f"update peliculas set dni ='null' where id = {y}")
    conn.commit()
    
    
"""micursor.execute("UPDATE clientes SET nombre = 'Helio' WHERE id =1")
micursor.execute("DELETE  FROM peliculas WHERE id = 2")
micursor.execute("SELECT  nombre FROM  peliculas")"""




