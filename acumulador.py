'''suma=0
opcion=1
while(opcion<=20):
    suma=suma+100
    opcion=opcion+1
print(f'el contador quedo en: {opcion}')
print(f'la suma quedo en: {suma}')'''

print("///////////////////// MENU //////////////////////")
print("1.Recibir votos \n\n")
opcion=0
opcion2=0
senado=0
camara=0
pacto=0
centro=0
equipo=0

while(opcion!=4):
    print("1.Senado")
    print("2.camara")
    print("3.consulta")
    print("4.Salir")

    opcion=int(input("Ingrese una opcion: "))
    if(opcion==1):
        senado +=1
    elif(opcion==2):
        camara +=1
    elif(opcion==3):
        
        print("1.pacto")
        print("2.centro")
        print("3.Derecha")
        print("4.salir")

        if opcion2==1:
            pacto+=1
        elif opcion2==2:
            centro+=1
        elif opcion2==3:
            equipo+=1


