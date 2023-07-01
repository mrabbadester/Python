#verficiação de idade paara entrada em clube noturno

idade = int(input("Digite sua idade: "));

if idade >= 18:
    print("Parabéns, voce ja tem idade para tirar a sua carteira.")
else:
    print("nao posso seu idade o menos a carteira");
print();


#Verificar se um numero esta dentro de um intervalo dentro de um intervalo entre 10 e 20

numero = 15; 

if numero >= 10 and numero <= 20:
    print("O numero esta dentro do intervalo");
else:
    print("O numero esta fora do intervalo");
    print();
    
    
    #comparar o tamanho de duas listas
    lista1 = [1, 2, 3, 4, 5];
    lista2 = [5, 4, 3, 2, 'a'];
    
    if len(lista1) > len(lista2):
        print("A lista 1 é maior que a lista 2");
    elif len(lista2) > len(lista1):
        print("A lista 2 é maior que a 1");
    else:
        print("as listas tem o mesmo tamanho");
    print();
    
    #Verificacao de acesso um sistema
    senha = input("Digite sua senha:");
    
    senha_correta = "123456";
    
    if senha == senha_correta:
        print("usuario logado com sucesso");
    else:
        print("A senha informada esta errada!");
        