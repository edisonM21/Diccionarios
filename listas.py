'''#listas
nombres=['javany','simon','Edison']
edades=[32,18,19]
descuentos=[True,False,False,5]
#impresion de lista
print(nombres)
print(nombres)
#accediendo a los elementos de una lista
for nombre in nombres:
    print(nombre)

for edad in edades:
    print(edad)

nombres.append('Marta')
print(nombre)'''

'''espacio=int(input("Digite el tamaño de la lista"))
multiplos=[]
contador=0

for multiplo in range(1,espacio+1):
    contador+=7
    multiplos.append(contador)
    print(multiplos)'''

tamaño=int(input("Digite el tamaño de la lista: "))
numeros=[]
for numero in range(tamaño):
    numero=int(input("Digite un numero: "))
    numeros.append(numero)
print(numeros)