#Classe base animal

class Animal:
    def __init__(self, nome):
        self.nome = nome;
        
    def emitir_som(self):
        pass 

# Classe derivada: Cachorro (herda de animal)
class Cachorro(Animal):
    def emitir_som(self):
        return 'Au Au!'

class Gato(Animal):
    def emitir_som(self):
        return 'Miau!'
    
#Classe derviada: Vaca (herda de animal)
class Vaca(Animal):
    def emitir_som(self):
        return 'Moo!'
    
def emitir_som_animal(animal):
    print(animal.emitir_som());

#Criando objetos das classes derivadas    
cachorro = Cachorro("Tom");
gato = Gato("Lupi");
vaca = Vaca("Mimosa");

#chamada do metodos emitir som para cada obejto (animal)
emitir_som_animal(Cachorro());
