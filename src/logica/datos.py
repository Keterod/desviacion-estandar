class Datos:
    def __init__(self, datos):
        self.__datos = datos

    def desviacion(self):
        if len(self.__datos) == 1:
            return 0
        else:
            return None

