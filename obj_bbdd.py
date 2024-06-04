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
    
    def darce_de_alta(self):
        micursor.execute("insert into from clientes (codigo, nombre, direccion, telefono, situacion, codigo_peli) values ")
    val = ("C0011", "Dayana","Calle falsa 364", "64388378", "l","null")
    micursor.execute(val)
    miconexion.commit()
        

    def darce_de_baja(self):
        micursor.execute("delete from clientes where id = 4")
        resultado =micursor.fetchall()
    def ver_sus_datos(self):
        micursor.execute("select  * from clientes  where id= 3")
    def modificar_datos(self):
        micursor.execute("update  clientes set nombre = 'Maria' where id = 3 ")

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

