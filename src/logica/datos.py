class Datos:
    def __init__(self, datos):
        self.__datos = datos

    def desviacion(self):
        if len(self.__datos) == 1:
            return 0
        if len(self.__datos) > 1:
            media = sum(self.__datos) / len(self.__datos)
            suma_cuadrados = sum((x - media) ** 2 for x in self.__datos)
            desviacion = (suma_cuadrados / len(self.__datos)) ** 0.5
            return desviacion
        else:
            return None
