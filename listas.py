nombres = ['Juan', 'Karla', 'Ricardo', 'María']

#imprimir la lista de nombres

print(nombres[0])
print(nombres[-1])

print(nombres[0:2])


print(nombres[:3])

print(nombres[1:])

nombres[3] = 'Martín'

print(nombres)


for nombre in nombres:
    print(nombre)

print(len(nombres))

nombres.append('María')

print(nombres)

nombres.insert(1, 'Octavio')
print(nombres)

nombres.remove('Octavio')
print(nombres)

nombres.pop()
nombres.pop()
print(nombres)


del nombres[0]
print(nombres)

nombres.clear()
print(nombres)

del nombres
print(nombres)