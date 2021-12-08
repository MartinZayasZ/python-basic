frutas = ('Naranja', 'Platano', 'Guayaba')
print(frutas)

#cantidad de elementos
print(len(frutas))

#acceder a un elemento
print(frutas[0])

#navegación inversa
print(frutas[-1])

#acceder a un rango
print(frutas[0:2])

for fruta in frutas:
    print(fruta, end = ' ')

#modificar tupla

frutasLista = list(frutas)
frutasLista[0] = 'Manzana'

frutas = tuple(frutasLista)
print('\n',frutas)