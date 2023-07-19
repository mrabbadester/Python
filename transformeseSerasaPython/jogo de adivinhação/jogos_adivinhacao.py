import random

def adivinhacao():
    print("Bem vindo ao jogo de adivinhação de numeros")
    print("Vamos personalizar o joga!")
    
    limite_inferior = int(input("Digite o limite inferior do intervalo de números: "))
    limite_superior = int(input("Digite o limite superior do intervalo de números: "))
    max_tentenativas = int(input("Digite o número máximo de tentativas: "))
    
    numero_secreto = random.randint
    (limite_inferior, limite_superior)
    tentativas = 0
    
    print(f"\nOk! Estou pensando em um número entre {limite_inferior} e {limite_superior}.")
    print(f"Você tem no máximo {max_tentenativas} tentativas.")
    
    while tentativas < max_tentenativas:
        palpite = int(input("\nDigite o seu palpite: "))
        tentativas += 1
        
        if palpite < numero_secreto:
            print("Tente um número maior")
        elif palpite > numero_secreto:
            print("Tente uma numero menos")
        else:
            print(f"Parabens! Você acertou o numero em {tentativas}tentetivas")
            break
         
        if tentativas == max_tentenativas:
            print(f"\nSuas tentativas acabaram o numero correto era {numero_secreto}.")
            
            jogar_novamente = input("\nDeseja jogar novamente? (S/N): ")
        if jogar_novamente.lower() == "s":
                adivinhacao()
        else:
            print("\nObrigado por jogar! ate proxima.")
                
        adivinhacao()
                