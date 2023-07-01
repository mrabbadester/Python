# 1 - Escreva um programa que solicite ao usurário dois números inteiros e 
# exiba a soma, subtração, multiplicação e divisão entre esse numeros.

numero1 = int(input("digite o PRIMEIRO número: "));
numero2 = int(input("digite o SEGUNDO número: "));

soma            = numero1 + numero2;
subtracao       = numero1 - numero2;
multiplicacao   = numero1 * numero2;
divisao         = numero1 / numero2;

print("soma: ", soma);
print("subtração: ", subtracao);
print("multiplacação: ", multiplicacao);
print("divisão: ", divisao);

# 2 - Escrev uma programa que solicite ao usurário uma temperatura em grau Celsius
# e verifique se ela está acima do ponto de ebulição da água (100ºc).
# Caso positivo, exiba a mensagem "A água está fervendo!".

temperatura = int(input("digite temperatura em graus celsius: "));

if temperatura > 100:
    print("a água está fervendo!");
    
print();

# 3 - Escreva um programa que solicite ao usuário um número inteiro e 
# verifique se ele é par ou ímpar. 
numero = int(input("digite um número inteiro: "));

if numero % 2 == 0:
  print("esse número é par. ");
else:
    print("esse número é impar. ");
    
print();

# 4 - Escreva um programa que solicite uma senha ao usuário e
# verifique se a senha está correta.
# Considere a senha correta como "123456".

senha = input("digite sua senha: ");

senha_correta = "123456";

if senha == senha_correta:
    print("usuário logado com sucesso!");
else:
    print("senha incorreta!");
    
print();

# 5 - Escreva um programa que solicite ao usuário uma idade e 
# verifique se ela está entre 18 e 30 anos (inclusive).
idade = int(input("digite sua idade: "));

if (idade >= 18) and (idade <= 30):
    print("a idade está entre 18 e 30 anos");
else:
    print("a idade não está entre 18 e 30 anos");
    
print();


# 6 - Escreva um programa que solicite ao usuário três números inteiros e
# verifique se pelo menos um deles é positivo.
numero1 = int(input("digite o primeiro número inteiro: "));
numero2 = int(input("digite o segundo número inteiro: "));
numero3 = int(input("digite o terceiro número inteiro: "));

if (numero1 > 0) or (numero2 > 0) or (numero3 > 0):
    print("um dos números é positivo.");
else:
    print("nenhum dos números é positivo.");
    
print();


# 7 - Escreva um programa que solicite ao usuário uma letra e
# verifique se ela é uma vogal (a, e, i, o, u). 
letra = input("digite uma letra: ");

if letra.lower() in ['a','e','i','o','u']:
    print("é uma vogal");
else:
    print("não é vogal");

print();


# 8 - Escreva um programa que solicite ao usuário um número inteiro e
# verifique se ele é positivo, negativo ou zero.
numero = int(input("digite o primeiro número inteiro: "));

if numero > 0:
    print("número é positivo.");
elif numero < 0:
    print("número é negativo.");
else:
    print("número é zero.");

print();


# 9 - Escreva um programa que solicite ao usuário três números e 
# verifique se eles estão em ordem crescente.
numero1 = float(input("digite 1º Número: "));
numero2 = float(input("digite 2º Número: "));
numero3 = float(input("digite 3º Número: "));

if (numero1 < numero2 < numero3):
    print("os números estão em ordem crescente.");
else:
    print("os números não estão em ordem crescente.");

print();

# 10 - Escreva um programa que solicite ao usuário um número inteiro e 
# verifique # se ele é um múltiplo de 3 e 5 ao mesmo tempo.

numero = int(input("digite um número inteiro: "));

if (numero % 3 == 0) and (numero % 5 == 0):
    print("número é um múltiplo de 3 e 5 ao mesmo tempo.");
else:
    print("número não é um múltiplo de 3 e 5 ao mesmo tempo.");

print();
 