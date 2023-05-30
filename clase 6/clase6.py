# Herencia

class Base:
    pass

class Hija(Base):
    pass

# Composición

class Base:
    pass

class Hija(Base):
    b = Base()  #Contiene una base, pero no es una BASE

h = Hija()
print(h.b)