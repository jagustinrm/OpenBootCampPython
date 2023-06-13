# Crea un script que le pida al usuario una lista de países (separados por comas).
#  Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). 
# Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.

paises = input("Ingresar lista de países separados por comas:").split(", ")

print(paises)

listaPaises = list(set(paises))
listaPaises.sort()

for elements in  listaPaises:
    print(elements, end=", ")