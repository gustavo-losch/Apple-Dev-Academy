class Televisao:
    #Construtuor
    def __init__(self, marca, volume):
        self.__marca = marca
        self.__volume = volume
    
    #Getters e Setters
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def volume(self):
        return self.__volume
    
    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    #Métodos
    def aumentar_volume(self):
        if self.__volume < 10:
            self.__volume += 1
    
    def diminuir_volume(self):
        if self.__volume > 0:
            self.__volume -= 1

#Teste
tv = Televisao("LG", 5)
tv.volume = 7
print(tv.volume)
print(tv.marca)