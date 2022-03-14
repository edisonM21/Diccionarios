'''contador=1
sumatoria=0
while(contador<=21):
    numero=int(input('ingrese un numero: '))
    if (numero<0):
        sumatoria+=1
    contador+=1
print(f'la cantidad de numeros negativos fur: {sumatoria}')'''

numero=0
suma=0
while (numero>=0):
    numero=int(input("Digite un numero: "))
    if(numero>=0):
        suma=numero+suma
print(f'la sumatoria de los positivos fue {suma}')

    