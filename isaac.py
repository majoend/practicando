
#idento el codigo con un try previniendo que solo sean ingresados datos numericos

try:
    mts = (input('Ingresa la cantidad de metros:'))
    #ingreso un input como funcion de preguntarle al usuario que ingrese su valor
    mts = float(mts)
    #uso float porque los valores que me va a dar podrian venir con decimales AUNQUE TAMBIEN LO PODRIA HACER ASI
    #mts = float(input('Ingresa la cantidad de metros:')) #
    # ----> PERO NO, POR SI ACASO EL PRIMER CODIGO NECESITA SER MODIFICADO 
    cmts = mts * 100 

    #SE TOMAN LOS VALORES DE CUANTOS CENTIMETROS HAY EN UN METRO Y SE MULTIPLICA 

    print(f'La cantidad que acaba de ingresar de {mts:,.0f} metros equivalen a {cmts:,.0f} cm')

    #SE IMPRIME LA SALIDA DEL CODIGO, SE USA UN F-STRING COMO UNA MEJOR FORMA DE CONCATENAR, 
except ValueError:
    print('Ingrese solo valores numericos')  

