class Abajur:
    #Construtor
    def __init__(self):
        self.__lampada = False
        self.__intensidade = 0

    #Getters e Setters
    @property
    def lampada(self):
        return self.__lampada
    
    @lampada.setter
    def lampada(self, estado):
        self.__lampada = estado

    @property
    def intensidade(self):
        return self.__intensidade
    
    @intensidade.setter
    def intensidade(self, intensidade):
        self.__intensidade = intensidade

    #Métodos
    def __liga_desliga_lampada(self):
        if self.__intensidade == 0:
            self.__lampada = False
        else:
            self.__lampada = True

    def __controla_intensidade(self):
        self.__intensidade += 1
        if self.__intensidade == 4:
            self.__intensidade = 0

    def tocar_botao(self):
        if input("Tocar botão [Enter]") == "":
            return True
        return False
    
    def mostrar_status(self):
        print("Status:")
        print(" -", self.__lampada)
        print(" -", self.__intensidade)

    def acoes(self):
        self.__controla_intensidade()
        self.__liga_desliga_lampada()

#Teste
abajur1 = Abajur()
while True:
    if abajur1.tocar_botao():
        abajur1.acoes()
    abajur1.mostrar_status()