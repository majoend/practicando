
#operador morsa: BASICAMENTE ES PONER UNA VARIABLE Y USAR EL PRINT COMO EN EL EJEMPLO USANDO :=

print(saludo := 'Hola, que tal')

print(edad := 25)

def saludo():
    return

saludo()



def numerospares_impares(numeros):

    if numeros % 2 == 0:
        return "El número es par"
    else:
        return "El número es impar"

numeros = int(input('Ingresa un numero')) 
print(numerospares_impares(numeros))

