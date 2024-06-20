import mysql.connector

miconexion = mysql.connector.connect(host="localhost", user ="root", password ="")
micursor = miconexion.cursor()

#comentas
micursor.execute("drop database  if exists proyecto_bbdd")
micursor.execute("create database proyecto_bbdd")
micursor.execute("use proyecto_bbdd")
micursor.execute("create table clientes (id int primary key auto_increment, codigo text (50),nombre text (50), direccion text (50), telefono text(50), situacion text (50), codigo_peli text (50) null)")
micursor.execute("create table peliculas(id int primary key auto_increment, codigo text (50),nombre_peli text (50),genero text(50),situacion text (50), codigo_cliente text(50) null)")

sql = "INSERT INTO clientes(codigo, nombre, direccion, telefono, situacion) VALUES (%s, %s, %s, %s, %s)"
val =[
    ("C001", "Dayana", "Murguiondo 123", "34151234", "l"),
    ("C002", "María", "Avenida Siempre Viva 742", "34155678", "l"),
    ("C003", "Carlos", "Calle Principal 456", "34158765", "l"),
    ("C004", "Ana", "Boulevard de los Sueños 890", "34154321", "l"),
    ("C005", "Pedro", "Calle Secundaria 101", "34156789", "l"),
    ("C006", "Luisa", "Avenida de la Paz 102", "34159876", "l"),
    ("C007", "Miguel", "Calle de la Amistad 203", "341534562", "l"),
    ("C008", "Laura", "Calle de la Esperanza 304", "34156543", "l"),
    ("C009", "Jorge", "Avenida del Sol 405", "34157890", "l"),
    ("C010", "Sofia", "Calle de las Flores 506", "34150987", "l")
]
micursor.executemany(sql, val )
miconexion.commit() 

sql = "INSERT INTO peliculas(codigo, nombre_peli, genero, situacion) VALUES (%s, %s, %s, %s)"
val =[
    ("C001", "Inception", "Ciencia ficción", "l"),
    ("C002", "Titanic", "Romance", "l"),
    ("C003", "The Matrix", "Acción", "l"),
    ("C004", "Gladiator", "Drama", "l"),
    ("C005", "Avatar", "Ciencia ficción", "l"),
    ("C006", "The Lion King", "Animación", "l"),
    ("C007", "Forrest Gump", "Drama", "a"),
    ("C008", "The Godfather", "Crimen", "l"),
    ("C009", "Star Wars", "Ciencia ficción", "l"),
    ("C010", "Jurassic Park", "Aventuraa", "l")
]
micursor.executemany(sql, val ) 
miconexion.commit()

