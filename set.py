planetas = {'Marte', 'Venus', 'Júpiter'}
print(planetas)

print(len(planetas))

#acceder elemento
print('Marte' in planetas)

#agregar un elemento
planetas.add('Tierra')
print(planetas)

#no se pueden duplicar
planetas.add('Tierra')
print(planetas)

#eliminar elemento
planetas.remove('Tierra')
print(planetas)

#eliminar elemento sin arrojar error
planetas.discard('Tierra2')
print(planetas)

#limpiar set
planetas.clear()
print(planetas)

#eliminar el set
del planetas
print(planetas)