tupla1 = (1,2,3,4,5,6);
tupla2 = ('a','b', 'c');
tupla3 = (1, 'hello', True);
tupla4 = 1, 2, 3, 4;
print(tupla1);
print(tupla2);
print(type(tupla3));
print(type(tupla4));

#acessando itens individualmente em tuplas.
print(tupla2[1]);
#tupla2[1] = "d";

#fatiamento de itens na tupla
print(tupla1[1:4]);

#concatenando tuplas
tupla5 = 1, 2, 3;
tupla6 = 4, 5, 6;
tupla7 = tupla5 + tupla6;
print(tupla7);

#criando variaveis novas com os valores de uma tupla
a, b, c = tupla6;
a = tupla6[0];

print();
print("Valores das variáveis ");
print(a);
print(b);
print(c);
