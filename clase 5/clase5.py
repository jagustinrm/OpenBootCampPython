def sumador(**kwargs):
    inicial = kwargs['inicial'] if 'inicial' in kwargs else 0
    final = kwargs['final'] if 'final' in kwargs else 0

    resultado = 0
    for x in range(inicial, final + 1):
        resultado += x

    return resultado
    
suma = sumador(inicial= 1, final= 10)
print(suma)


anonima = lambda nombre, nombre2: print("hola ", nombre, "hola", nombre2)
anonima()

sumatoria = lambda x: x+x
print(sumatoria(2))