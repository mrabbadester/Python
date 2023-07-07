# 1 - utlilizando um loop "while", imprimima os numeros de 1 a 0

contador = 10;

while contador >= 1:
  print(contador);
  contador -= 1;

# 2 - utlilizando um loop "for", imprimima os numeros de 1 a 0 
notas = [];
nota = float(input("Digite uma nota (-1 para sair): "));

while nota >= 0:
  notas.append(nota);
  nota = float(input("Digite uma nota (-1 para sair): "));
  
print(notas); 
    
# 3 - utlilizando um loop "while", clacule a soma dos numeros de 1 a 100
senha = input("Informe uma senha: ");
contador = 0;
senhaBloqueada = False;

while senha != '123456':
  print("Senha incorreta");
  contador += 1;
  if(contador == 3):
    senhaBloqueada = True;
    break;
  senha = input("Digite a senha: ");

if(senhaBloqueada):
  print("Sua senha foi bloqueada!");
else:
  print("Senha correta!");


# 4 - utlilizando um loop "for", clacule a soma dos numeros de 1 a 100
quantidade = int(input("Informe a quantidade de numeros pares a serem impressos: "));
contador = 1;

while quantidade > 0:
  if contador % 2 == 0 :
    print(contador);
    quantidade -= 1;
  contador += 1;
    
    
# 5 - utlilizando um loop "while", imprima os numeros de 1 a 20
numeroSecreto = 42;
palpite = int(input("Digite um número: "));

while palpite != numeroSecreto:
  print("Você errou! Tente novamente")
  palpite = int(input("Digite um número: "));

print("Parabéns! Você acertou o palpite!");


# 6 - utlilizando um loop "for", imprima os numeros pares de 1 a 20
palavra = input("Digite uma plavra ('sair' para encerrar): ");
palavra = palavra.lower();
while palavra != 'sair' :
  print(palavra);
  palavra = input("Digite uma plavra ('sair' para encerrar)");
  palavra = palavra.lower();

#Exemplo: implementação de meu opções.
opcao = 0;

while opcao != 4:
  print("Menu: ");
  print("1. opção 1");
  print("2. opção 2");
  print("3. opção 3");
  print("4. Sair");
  
  opcao = int(input("Informa opção escolhida: "));
  if opcao == 1:
    print("Opção 1 selecionada!");
  elif opcao == 2:
    print("Opção 2 selecionada!");
  elif opcao == 3:
    print("Opção 3 selecionada!");
  elif opcao == 4:
   print("Saindo...");
  break;
else:
  print("Opção inválida, tente novamente");
  
  
  #emulando do while 
  
  palavraSecreta = "pyhton";
  conuter = 0;
  
  while True:
    palavra = input("Informe a palavra secreta").lower();
    contador +- 1;
    
    if palavra == palavraSecreta:
      print("Você acertou a palavra!");
      break;
    if(palavra != palavraSecreta and contador > 7):
      print("Voce atingiu o limite de tentativas!");

# 7 - utlilizando um loop "white", inverta uma string digitada pelo usuario




# 8 - utlilizando um loop "for", # verifique se uma palavra digitada pelo usuario 
# é um palíndromo(lê-se da mesma forma de tras para frente).



#9 - utlilizando um loop "while", encontre o menor numeros inteiro cujo quadrado seja
#maior do que 100. 



# 10 - utlilizando um loop "for", imprima os elementos de uma lista em ordem inversa 

