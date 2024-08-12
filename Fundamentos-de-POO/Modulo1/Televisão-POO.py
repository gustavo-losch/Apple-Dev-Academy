class Televisao:
    #Construtor
    def __init__(self, marca, volume):
        self.__marca = marca
        self.__volume = volume

    #Getters e Setters
    def get_marca(self):
        return self.__marca
    
    def set_marca(self, marca):
        self.__marca = marca

    def get_volume(self):
        return self.__volume
    
    def set_volume(self, volume):
        self.__volume = volume

    #Métodos
    def aumentar_volume(self):
        if self.__volume < 10:
            self.__volume = self.__volume + 1

    def diminuir_volume(self):
        if self.__volume > 0:
            self.__volume = self.__volume - 1

    def mudar_nome(self):
        self.__marca = input()


# Teste --
televisao = Televisao('Samsung',5)

televisao.diminuir_volume()
televisao.aumentar_volume()

print(televisao.get_marca())
print(televisao.get_volume())