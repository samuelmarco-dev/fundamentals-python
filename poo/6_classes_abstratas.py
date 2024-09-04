from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    # Decorator que indica que este é um método abstrato
    @abstractmethod  
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @abstractmethod
    def aumentar_volume(self):
        pass

    @abstractmethod
    def diminuir_volume(self):
        pass


class ControleTV(ControleRemoto):
    def __init__(self, marca):
        self.marca = marca
        self.volume = 10
        self.ligada = False

    def ligar(self):
        self.ligada = True
        print(f"TV {self.marca} ligada.")

    def desligar(self):
        self.ligada = False
        print(f"TV {self.marca} desligada.")

    def aumentar_volume(self):
        if self.ligada:
            self.volume += 1
            print(f"Volume aumentado para {self.volume}.")
        else:
            print("A TV está desligada.")

    def diminuir_volume(self):
        if self.ligada:
            self.volume -= 1
            print(f"Volume diminuído para {self.volume}.")
        else:
            print("A TV está desligada.")


class ControleSom(ControleRemoto):
    def __init__(self, marca):
        self.marca = marca
        self.volume = 5
        self.ligado = False

    def ligar(self):
        self.ligado = True
        print(f"Sistema de som {self.marca} ligado.")

    def desligar(self):
        self.ligado = False
        print(f"Sistema de som {self.marca} desligado.")

    def aumentar_volume(self):
        if self.ligado:
            self.volume += 1
            print(f"Volume do som aumentado para {self.volume}.")
        else:
            print("O sistema de som está desligado.")

    def diminuir_volume(self):
        if self.ligado:
            self.volume -= 1
            print(f"Volume do som diminuído para {self.volume}.")
        else:
            print("O sistema de som está desligado.")


# Exemplos de uso
controle_tv = ControleTV("LG")
controle_tv.ligar()
controle_tv.aumentar_volume()
controle_tv.aumentar_volume()
controle_tv.desligar()

controle_som = ControleSom("Sony")
controle_som.ligar()
controle_som.diminuir_volume()
controle_som.desligar()
