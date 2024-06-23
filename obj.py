from bbdd import miconexion, micursor

class usuario():
    def __init__(self, codigo, nombre, direccion, telefono):
        self.__codigo =codigo
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__situacion = "L"
        self.__codigo_peli = ""

    def get_codigo(self):
        return self.__codigo
    def set_codigo(self,newcodigo):
        self.__codigo = newcodigo
        

    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, newnombre):
        self.__nombre = newnombre
        

    def get_direccion(self):
        return self.__direccion
    def set_direccion(self, newdireccion):
        self.__direccion = newdireccion

    def get_telefono(self):
        return self.__telefono
    
    def set_telefono(self,newtelefono):
        self.__telefono = newtelefono

    def get_situacion(self):
        return self.__situacion
    def set_situacion(self, newsituacion):
        self.__situacion = newsituacion

    def get_codigo_peli(self):
        return self.__codigo_peli
    def set_codigo(self, newcodigo_peli):
        self.__codigo_peli = newcodigo_peli
        
        
    
    def darse_de_alta(self):
        sql = "INSERT INTO clientes(codigo, nombre, direccion, telefono, situacion) VALUES (%s, %s, %s, %s, %s)"
        val =(self.get_codigo(), self.get_nombre(), self.get_direccion(),self.get_telefono(), self.get_situacion())
        micursor.execute(sql, val )
        miconexion.commit() 

        

    def darse_de_baja(self):
        micursor.execute(f"delete from clientes  where codigo  = '{self.get_codigo}'") #corregido
        miconexion.commit()
        print("Usuario dado de baja correctamente")
        # micursor.execute(f"select situacion from clientes where  codigo ='{self.get_codigo()}'")
        # micursor.execute(f"update  clientes  set situacion = 'B' where codigo = '{self.get_codigo()}'")
        #miconexion.commit()
        
        

    def ver_datos(self):
        micursor.execute(f"select  * from clientes  where codigo = '{self.get_codigo()}'")
        datos = micursor.fetchall()
        for i in datos:
            print(i)  #corregido
        
        


    def modificarDatos(self,n,newdato): #user colocar en parametro
        if n == 1:
            
            micursor.execute(f"update  clientes set direccion ='{newdato}' where  codigo ='{self.get_codigo()}'")
            miconexion.commit()
            print("El telefono se modifico con exito")
        elif n == 2:
            micursor.execute(f"update clientes set telefono = '{newdato}' where codigo ='{self.get_codigo()}'")
            miconexion.commit()
            print("La direccion no se modifico correctamente")
        else:
            ("Opción no válida, por favor ingrese una opcion valida.") #corregido
            
    
    
    
            
    #gestion_pelis
    def ver_todas_las_pelis (self):   #pelis corregido
        print("PELICULAS\n")
        micursor.execute("select *  from peliculas")
        resultado =micursor.fetchall()
        for i in resultado:
            print(f"Nombre de la Pelicula {i}")
            
            

    def ver_solo_disponibles(self):
        print("PELICULAS DISPONIBLES\n")
        micursor.execute("select nombre_peli  from peliculas where  situacion = 'l'")#pelis_corregido
        resultado =micursor.fetchall()
        for i in resultado:
            print(i)

    def alquilar_peli(self,id_cliente,id_pelicula):
        micursor.execute(f"update clientes set situacion ='A' where id ={id_pelicula}")
        micursor.execute(f"update clientes set codigo_peli = 'y' where id ={id_cliente}")
        micursor.execute(f"update peliculas set situacion ='a' where  id = {id_pelicula}")
        micursor.execute(f"update peliculas set dni = 'x' where id ={id_pelicula}")
        miconexion.commit()
        
           
        
    def devolver_peli (self,id_cliente ,id_pelicula):
        micursor.execute(f"update clientes set situacion ='l' where id ={id_cliente}")
        micursor.execute(f"update clientes set codigo = 'null' where id = {id_cliente}")
        micursor.execute(f"update peliculas set situacion ='l' where id = {id_pelicula}")
        micursor.execute(f"update peliculas set dni = 'null where id = {id_pelicula}")
        miconexion.commit()
        
obj = usuario("C001", "dayana", "mataderos", "1169541265")
print(obj) 
# print(obj.get_telefono())
# obj.set_telefono("142574")
# print(obj.get_telefono())
#obj =usuario()

