
#Se llama asignacion multiple cuando varias variables tienen un mismo valor
nombre1 = nombre2 = nombre3 = 'hola'
print(nombre1,nombre2,nombre3) #SALE IMPRESO TRES VECES 

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