import functools

lista = [1, 2, 3, 4, 5, 6, 7]

def filtroImpares (x):
    if x % 2:
        return True
    else:
        return False
    
filtro = list(filter(filtroImpares, lista))
print(functools.reduce(lambda a, b: a+b, filtro))