#condicion = True
#i = 0
#while condicion:
#    i += 1
#    print('Ejecutando ciclo while')
#    if i == 10:
#        condicion = False
#else:
#    print('Fin del ciclo while')



#cadena = 'Hola'

#for letra in cadena:
#    print(letra)
#else:
#    print('Fin ciclo for')

#for letra in 'Holanda':
#    if letra == 'a':
#        print(f'Letra encontrada: {letra}')
#        break;
#else:
#    print('Ciclo for terminado')


for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')
