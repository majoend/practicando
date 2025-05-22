
#Se llama asignacion multiple cuando varias variables tienen un mismo valor
print(nombre1 := 'hola')
#print(nombre1,nombre2,nombre3) #SALE IMPRESO TRES VECES 

#Esta es otra forma de asignacion multiple
nombre = 'Isaac'
apellido = 'Salas'
edad = 28
estatura = 132.6
print(nombre, apellido, edad, estatura)

#Otra forma
nombre, apellido, edad, talla_zapato = 'Orlando', 'Salas', 11, 35
print(nombre, apellido, edad, talla_zapato)

#PARA SITIOS WEB, EN LUGAR DE PONER TODO EL NOMBRE PODEMOS MANIPULAR LA CADENA DE ESTA FORMA:
#SIEMPRE DEBEMOS DARLE UN NOMBRE CLARO A LAS VARIABLES

website = 'https://www.youtube.com/'
#usamos la funcion slice 

slice = slice(12,-5)
print(website[slice]) #ESTABA PONIENDO (), SE DEB USAR []

#BUCLES ANIDADOS: ---> BASICAMENTE UN BUCLE DENTRO DE OTRO BUCLE

#for i --> bucle  externo
#for j --> bucle  interno

fila = int(input('Ingresar fila:'))
columna = int(input('Ingresar columna:'))
simbolo = (input('Ingresar simbolo:'))


for i in range(fila):
    for j in range(columna):
       print(simbolo, end='') #---> se pone un end para no saltar entre lineas 
    print() #---> se debe salir asi del bucle 

pelicula = ""
while True:
    pelicula = input('cual es tu pelicula de magis fav:')
    if pelicula != "": #---> SI PELICULA ES DISTINTO A UNA CADENA VACIA, OSEA CONTIENE TEXTO, ENTONCES SALIMOS DEL BUCLE
        break


#---> BUCLES FOR Y WHILE 
# continue ---> saltar las condiciones que le estemos dando
# break ---> finaliza el bucle si la declaracion verdadera se cumple
# pass ---> no hace nada basicamente para evitar errores de espacios vacios