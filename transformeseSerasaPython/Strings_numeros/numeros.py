
#Matemática 
num1 = 10;
num2 = 5;

soma = num1 + num2;
subtracao = num1 - num2;
multiplicacao = num1 * num2;
divisao = num1 / num2;
resto = num1 % num2;
potencia = num1 ** num2;

print("Operações matemáticas básica: ");
print("Soma: ", soma);
print("subtracao: ", subtracao);
print("multiplicacao", multiplicacao);
print("divisao: ", divisao);
print("resto: ", resto);
print("potencia: ", potencia);

#Arredondamento de número.
numeroFloat = 3.14;
numeroArredondamento = round(numeroFloat);
print("Arredondamento: ", numeroArredondamento);

#Funções matemáticas da biblioteca math.
import math

num = 4.7;
print("Funcções matemáticas: ");
print("valor absoluto: ", abs(-4.7));
print("Arredonadamento pra cima", math.ceil(num));
print("Arredonadamento pra baixo", math.floor(num));

#Formatação de números.
numeroFormatado = 1234.56789;
print("Formatação de numeros: ");
print(f"Número com 2 casas decimais {numeroFormatado:.2f}");
print("Numero formatado com 2 casas decimais {:.2f}".format(numeroFormatado));
