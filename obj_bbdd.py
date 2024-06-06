from bbdd import miconexion, micursor
#clase user                     
#atributos                    
#metodos                        
#ver todas las pelis               select
#ver solos disponibles             select where
#alquiler/devolver                 update


#darce de alta                     insert
# darce de baja                    delete
# ver su datos                     select
# modificar telf/direc             update
"""micursor.execute("UPDATE clientes SET nombre = 'Helio' WHERE id =1")
micursor.execute("DELETE  FROM peliculas WHERE id = 2")
micursor.execute("SELECT  nombre FROM  peliculas")"""


class usuario():
    def __init__(self, codigo, nombre, direccion, telefono, situacion, codigo_peli):
        self.__codigo =codigo
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__situacion = situacion 
        self.__codigo_peli = codigo_peli

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
        sql = "insert into from clientes (codigo, nombre, direccion, telefono, situacion, codigo_peli) values  (%s, %s,  %s, %s, %s, %s)"
        val = (self.get_codigo(), self.get_nombre(), self.get_direccion(), self.get_telefono(), self.get_situacion(),self.get_codigo_peli())
        micursor.execute(sql, val)
        miconexion.commit()
        

    def darse_de_baja(self):
        micursor.execute(f"delete from clientes  where codigo = {self.get_codigo()}")

    def ver_sus_datos(self):
        micursor.execute(f"select  * from clientes  where codigo = {self.get_codigo()}")


    def modificar_datos(self,n,newdato):
        if n == 1:
            micursor.execute(f"update  clientes set direccion = {newdato} where  codigo ={self.get_codigo()}")
        elif n == 2:
            micursor.execute(f"update clientes set telefono = {newdato} whre telefono ={self.get_telefono()}")
        else:
            ("Opción no válida, por favor intente de nuevo.")

    
            
    #gestion_pelis
    def ver_todas_las_pelis (self):
        micursor.execute("select * from peliculas ")
        resultado =micursor.fetchall()
        for i in resultado:
            print(i)

    def ver_solo_disponibles(self):
        micursor.execute("select * from peliculas where  situacion = 'l'")
        resultado =micursor.fetchall()
        for i in resultado:
            print(i)

    def alquilar_peli  (self):
        micursor.execute("")

    def devolver_peli (self):
        pass        

objeto = usuario()
objeto.ver_todas_las_pelis()

