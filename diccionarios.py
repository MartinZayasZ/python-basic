#dict (key, value)
diccionario = {
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System',
}

print(diccionario)

#rango de elementos
print(len(diccionario))

#acceder a un elemento
print(diccionario['IDE'])

#otra forma de acceder a un elemento
print(diccionario.get('OOP'))

#modificar elemento
diccionario['IDE'] = 'Nuevo IDE'
print(diccionario)


for termino, valor in diccionario.items():
    print(termino, valor)

for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

#comprobar element
print('IDE' in diccionario)

#agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

diccionario.pop('DBMS')
print(diccionario)

diccionario.clear()
print(diccionario)

del diccionario
print(diccionario)
