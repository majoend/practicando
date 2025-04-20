
#---> BUCLES FOR

frutas = 2 #---> para numeros

for i in range(0, 3): #<----IMPRIME HOLA EL NUMERO DE VECES QUE SE LE DIGA AQUI
    if frutas != "": # si frutas es distinto a una cadena vacia se cumple la impresion en el bucle

        print('hola')

frutas = 'pera' #--> para listas, cadenas de textos etc, el bucle recorre las veces en la palabra EXAMPLE: 
#SI TIENE DOS LETRAS IMPRIME DOS VECES, SI TIENE CUATRO LETRAS IMPRIME CUATRO VECES
for i in frutas:
    if frutas != "":
        print('HI')

#AHORA VAMOS CON EL CONTINUE, BREAK, Y PASS

video = '9-9-77777-888'
for i in video:
    if i == "7": # SE PONE LA i COMO caracter a saltarnos 
        continue # PONEMOS EL CONTINUE PARA QUE SE CUMPLA EL BUCLE Y SE SALTE EL CARACTER GUARDADO EN i
    print(i, end="") 



