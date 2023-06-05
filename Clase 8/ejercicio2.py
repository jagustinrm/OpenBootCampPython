import pickle

class Vehículo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def __str__(self):
        return f"Vehículo: {self.marca} {self.modelo}, Color: {self.color}"


vehiculo = Vehículo("Toyota", "Corolla", "Rojo")


archivo = open("vehiculo.bin", "wb")
pickle.dump(vehiculo, archivo)
archivo.close()

archivo = open("vehiculo.bin", "rb")
vehiculo_cargado = pickle.load(archivo)
archivo.close()

print(vehiculo_cargado)
