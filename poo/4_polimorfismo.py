class Animal:
    # def emitir_som(self):
    #     pass
    
    def emitir_som(self):
        raise NotImplementedError("Subclasses devem implementar este método")

class Cachorro(Animal):
    def emitir_som(self):
        return "Latido"

class Gato(Animal):
    def emitir_som(self):
        return "Miau"

class Vaca(Animal):
    def emitir_som(self):
        return "Muuu"

# Função que recebe qualquer animal e chama o método emitir_som
def fazer_animal_emitir_som(animal):
    print(animal.emitir_som())

# Criando instâncias das subclasses
cachorro = Cachorro()
gato = Gato()
vaca = Vaca()

# Utilizando polimorfismo
fazer_animal_emitir_som(cachorro)  # Output: Latido
fazer_animal_emitir_som(gato)      # Output: Miau
fazer_animal_emitir_som(vaca)      # Output: Muuu
