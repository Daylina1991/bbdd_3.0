import mysql.connector

miconexion = mysql.connector.connect(host="localhost", user ="root", password ="")

micursor = miconexion.cursor()
micursor.execute("drop database  if exists proyecto_bbdd")
micursor.execute("create database proyecto_bbdd")
micursor.execute("use proyecto_bbdd")
micursor.execute("create table clientes (id int primary key auto_increment, codigo text (50),nombre text (50), direccion text (50), telefono text(50), situacion text (50), codigo_peli text (50) null)")
micursor.execute("create table peliculas(id int primary key auto_increment, codigo text (50),nombre_peli text (50),genero text(50),situacion text (50), codigo_cliente text(50) null)")

sql = "INSERT INTO clientes(codigo, nombre, direccion, telefono, situacion, codigo_peli) VALUES (%s, %s, %s, %s, %s, %s)"
val =[
    ("C001", "Juan", "Calle Falsa 123", "34151234", "l","null"),
    ("C002", "María", "Avenida Siempre Viva 742", "34155678", "l","null"),
    ("C003", "Carlos", "Calle Principal 456", "34158765", "l","null"),
    ("C004", "Ana", "Boulevard de los Sueños 890", "34154321", "l","null"),
    ("C005", "Pedro", "Calle Secundaria 101", "34156789", "l","null"),
    ("C006", "Luisa", "Avenida de la Paz 102", "34159876", "l","null"),
    ("C007", "Miguel", "Calle de la Amistad 203", "341534562", "l","null"),
    ("C008", "Laura", "Calle de la Esperanza 304", "34156543", "l","null"),
    ("C009", "Jorge", "Avenida del Sol 405", "34157890", "l","null"),
    ("C010", "Sofia", "Calle de las Flores 506", "34150987", "l","null")
]
micursor.executemany(sql, val )
miconexion.commit() 

sql = "INSERT INTO peliculas(codigo, nombre_peli, genero, situacion, codigo_cliente) VALUES (%s, %s, %s, %s, %s)"
val =[
    ("C001", "Inception", "Ciencia ficción", "l","null"),
    ("C002", "Titanic", "Romance", "l","null"),
    ("C003", "The Matrix", "Acción", "l","null"),
    ("C004", "Gladiator", "Drama", "l","null"),
    ("C005", "Avatar", "Ciencia ficción", "l","null"),
    ("C006", "The Lion King", "Animación", "l","null"),
    ("C007", "Forrest Gump", "Drama", "a","null"),
    ("C008", "The Godfather", "Crimen", "l","null"),
    ("C009", "Star Wars", "Ciencia ficción", "l","null"),
    ("C010", "Jurassic Park", "Aventura", "l","null")
]
micursor.executemany(sql, val )
miconexion.commit()

