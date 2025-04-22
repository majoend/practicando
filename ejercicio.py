
#Esto es un ejercicio de conversiones de longitudes

#Comenzamos definiendo las funciones que queremos convertir y que a su vez nos retorne los valores

def convertir_metros_a_kilometros(metros1): #ESTABLECEMOS LAS FUNCIONES DE LOS CODIGOS(VALORES QUE QUEREMOS PASAR)
    return metros1 / 1000

def convertir_metros_a_centimetros(metros2):
    return metros2 * 100

def convertir_metros_a_milimetros(metros3):
    return metros3 * 1000

def convertir_kilometros_a_millas(kilometros):
    return kilometros / 1.609

def convertir_centimetros_a_milimetros(centimetros):
    return centimetros * 10

def mostramos_un_menu_longitudes(): # ESTE MENU NOS MOSTRARA LAS OPCIONES A ELEGIR

    print('Bienvenido a la conversion de Python.\n ¿Qué valores desea convertir? \n') #USO \n para separar un poco las lineas
    
    print("1. Metros a kilometros") # menu de opciones
    print("2. Metros a centimetros")
    print("3. Metros a milimetros")
    print("4. Kilometros a millas")
    print("5. Centimetros a milimetros \n ")


def ejecucion_de_conversiones(): #CON ESTA FUNCIONES EJECUTAMOS LAS CONVERSIONES EN UN BUCLE WHILE

    while True:
        mostramos_un_menu_longitudes() #DEVOLVEMOS LA FUNCION DE ARRIBA PARA MOSTRAR LAS OPCIONES Y QUE EL USUARIO ELIJA
        opciones = input('Ingrese una opcion del menú:').strip()

        if opciones == "1":  # ESTABLECEMOS EL CODIGO DE ESTA FORMA, UN POCO REPETITIVO PARA APROVECHAR LAS FUNCIONES Y EL BUCLE
            metros1 = float(input('Ingresa la cantidad de metros a convertir en kilometros: '))
            kilometros = convertir_metros_a_kilometros(metros1)
            print(f'{metros1:,.0f} metro(s) equivale(n) a {kilometros:,.0f} kilometros')

        elif opciones == "2":
            metros2 = float(input('Ingresa la cantidad de metros a convertir en centimetros: '))
            centimetros = convertir_metros_a_centimetros(metros2)
            print(f'{metros2:,.0f} metro(s) equivale(n) a {centimetros:,.0f} centimetros')

        elif opciones == "3":
            metros3 = float(input('Ingresa la cantidad de metros a convertir en milimetros: '))
            milimetros = convertir_metros_a_milimetros(metros3)
            print(f'{metros3} metro(s) equivale(n) a {milimetros:,.0f} milimetros')

        elif opciones == "4":
            kilometros = float(input('Ingresa la cantidad de kilometros a convertir en millas: '))
            millas = convertir_kilometros_a_millas(kilometros)
            print(f'{kilometros} kilometros (s) equivale(n) a {millas:,.3f} millas')

        elif opciones == "5":
            centimetros = float(input('Ingresa la cantidad de centimetros a convertir en milimetros: '))
            milimetros = convertir_centimetros_a_milimetros(centimetros)
            print(f'{centimetros:,.0f} centimetros(s) equivale(n) a {milimetros:,.0f} milimetros')

        else: #PONEMOS UN ELSE PARA QUE CAPTE SI LO QUE ESTA EN EL MENU NO ES VALIDO ENTONCES CUMPLA SU FUNCION DEL PRINT
            print('Opción no válida')

        continuar_conversiones = input('Continuamos realizando conversiones? \n \n si/no: ').strip().lower()
        if continuar_conversiones != ('si' and 's'): #USAMOS EL OPERADOR LOGICO AND PARA VALIDAR CUALQUIERA DE LAS DOS RESPUESTAS
            print('Hasta la próxima')
            break #ROMPEMOS EL BUCLE CON UN BREAK PREGUNTANDO AL USUARIO SI DESEA CONTINUAR CONVIRTIENDO VALORES
        
ejecucion_de_conversiones() #LLAMAMOS NUESTRA FUNCION PARA QUE EL CICLO SE CUMPLA