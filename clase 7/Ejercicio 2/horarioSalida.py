import time

def calcular_tiempo_restante():
    hora_actual = time.localtime().tm_hour
    

    hora_salida = 19 

    if hora_actual >= hora_salida:
        print("¡Es hora de ir a casa!")
    else:
        horas_restantes =  hora_salida - hora_actual
        print(f"Quedan {horas_restantes} horas.")


calcular_tiempo_restante()
