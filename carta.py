from ast import If


opcion=100

print("///////////////////// MENU A LA CARTA //////////////////////")
print("1.Calcular la suma")
print("2.Calcular la resta")
print("3.Calcular la multiplicacion")
print("4.Calcular la division")
print("0.Salir")
print("////////////////////////////////////////////////////////////")
while(opcion!=0):
    opcion=int(input("DIGITA UNA OPCION: "))
    if(opcion==1):
        numero1=int(input("Digita un numero: "))
        numero2=int(input("Digita otro numero: "))
        print(f'{numero1}+{numero2}={(numero1+numero2)}')

    elif(opcion==2):
        numero1=int(input("Digita un numero: "))
        numero2=int(input("Digita otro numero: "))
        print(f'{numero1}-{numero2}={(numero1-numero2)}')

    elif(opcion==3):
        numero1=int(input("Digita un numero: "))
        numero2=int(input("Digita otro numero: "))
        print(f'{numero1}*{numero2}={(numero1*numero2)}')
    elif(opcion==4):
        numero1=int(input("Digita un numero: "))
        numero2=int(input("Digita otro numero: "))
        print(f'{numero1}/{numero2}={(numero1/numero2)}')
    else:
        print("Error digitando la opcion .|.")





