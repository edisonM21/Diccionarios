'''suma=0
opcion=1
while(opcion<=20):
    suma=suma+100
    opcion=opcion+1
print(f'el contador quedo en: {opcion}')
print(f'la suma quedo en: {suma}')'''

print("Conteo De Votos\n\n")

#inicializo variables de opcion
opcion = 0
opcion2 = 0

#inicializo contadores

senado= 0
camara = 0
pacto = 0
centro = 0
derecha = 0
#hago ciclo while
while(opcion != 4):
    #imprimo opciones
    print("\n1)Senado\n2)Camara\n3)Consulta\n4)salir\n5)Mostrar votos")
    #Digito opcion
    opcion = int(input("Ingrese una opcion del menu: "))

    #Condiciones para cada opcion
    if opcion == 1:
        senado += 1 
    elif opcion == 2:
        camara += 1
    elif opcion == 3:
        print("\n  1)pacto\n  2)centro\n  3)derecha\n  4)salir\n")

        #Evaluar condicion del usuario
        opcion2 = int(input("Ingrese una opcion: "))

        if opcion2 == 1:
            pacto += 1
        elif opcion2 == 2:
            centro += 1
        elif opcion2 == 3:
            derecha += 1
    elif opcion == 5:
        #imprimir votos
        print(f'Senado: {senado}\nCamara: {camara}\nPacto: {pacto}\nCentro: {centro}\nDerecha: {derecha}') 


