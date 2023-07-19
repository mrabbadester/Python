import random

def adivinhacao ():
    numero_secreto = random.randint (1, 20);
    tentativa = 0;
    
    print("Bem vindo ao jogo de advinhicação de número!");
    print("Estou pensando número entre 1 a 20.");

    while True:
        chute = int(input ("Qual é o seu palpite? "));
        tentativa += 1;

        if chute < numero_secreto:
            print("Mais... Tente mais uma vez.");
        elif chute > numero_secreto:
            print("Menos ...Tente mais uma vez.");
        else :
            print(f"Parabéns! Você acertou o número em {tentativa} tentativas");
            break

adivinhacao()