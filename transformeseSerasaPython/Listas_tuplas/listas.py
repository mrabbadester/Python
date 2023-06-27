listaNumeros = [1,2,3,4,5];
listaStrings = ['e', 'f', 'c', 'd'];
listaMista = [1, 'a', 3.14, True]
print(listaNumeros);
print(listaStrings);
print(listaMista);
print();

frutas = ["maça", "banana", "morango"];

print(frutas[0]);
print();

frutas[1] = "laranja";
print("Tamanho 1: ", len(frutas));
frutas.append("abacaxi");
print(frutas);

print("tamanho 2: ", len(frutas));
print();

listaNova = [1, ["a", "b"]];
print(listaNova[1][0]);
print();

lista1 = [1,2,3];
lista2 = [4,5,6];

lista_concatenada = lista1 + lista2;
print(lista_concatenada);
print();

listaRepetida = [0] * 3;
print(listaRepetida);
print();

numeros = [1,2,3,4];
sublista = numeros[1:4];
print(sublista);
print();


numeros = ["a","b","c","d"];
sublista = numeros[1:4];
print(sublista);
print();


letras = ["a","b","c","d"];
sublista = letras[1:4];
print(sublista);
print();


frutas = ["maça", "banana", "laranja"];
frutas.append("morango");
print(frutas);
print();

frutas.insert(1,  "abacaxi");
print(frutas);
print();

frutaRemovida = frutas.remove("banana");
frutaRemovida = frutas.pop(2);
print(frutas);
print(frutaRemovida);
print();

frutas.sort();
print("Embaralhado: ", frutas);

from random import shuuffle
shuuffle(frutas);
print(frutas);
