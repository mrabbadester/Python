import random

tentativas = 0

print("Olá! Qual é o seu nome?")
meuNome = input()
numero = random.randint(1, 100)
print("Bem, " + meuNome + ", Pensando em um número entre 1 e 100.")
while tentativas < 6:
    print("Tente adivio") 
    
    palpite = input()
    palpite = int(palpite)
    
    tentativas = tentativas + 1
    if palpite < numero:
        print(" é muito baixo!") 
        
    if palpite > numero:
        print("é muito alto!")
        
    if palpite == numero:
        break