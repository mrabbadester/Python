frase  = "Olá, mundo!"

print("String original: ")
print(frase);
print();

#Acessando caracteres individuais. 
print("Acessando caracteres individuais: ");
print("Frase: ", frase)
print("Primeiro caractere: ", frase[0]); 
print("Último caractere: ", frase[-1]); 

#Utilizando o input para pegar um nome informado pelo usuário. 
nome = input("nome ");
print(nome);
print();

#Inserindo as variáveis no print com f.
sobreNome = input("Sobrenome: ");
print(f"Bem-vindo, {nome} {sobreNome}");
print("Bem-vindo, {} {}".format(nome, sobreNome));

#Concatenando strings.
print("Concatenando strings: ");
outraFrase = " Bem-vindo " ;
fraseCompleta = frase + outraFrase;
print(fraseCompleta);
print();

#Tamanho da string
tamanho = len(frase);
print("tamanho: ", tamanho);
print();

#Divindo uma string em sub strings.
print("Divindo a string ");
palavras = fraseCompleta.split();
print(palavras);

#Substituindo partes das string.
print("Substituindo partes das strings: ");
novaFrase = frase.replace("mundo", "Python");
print(novaFrase);
print();

#Convertendo para letras Maiúsculas e Minúsculas.
print("Convertendo para letras maiúsculas e minúsculas ");
print("Maiúsculas: ", frase.upper());
print("Minúsculas: ", frase.lower());

