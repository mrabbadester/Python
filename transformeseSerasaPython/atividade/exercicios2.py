#1 - Crie uma lista chamada "frutas" contendo as seguintes frutas : 
# maçã, banana, laranja, abacaxi e melancia. Em seguida, exiba a lista completa na tela.
frutas = ["maça", "banana", "laranja", "abacaxi", "melancia"];
print("Listas frutas: ", frutas);
print();

#2 - Adicione a fruta "uva" à lista "frutas" utilizando o método append(). Exiba a lista atualizada na tela.
frutas.append("uva");
print("Adicionado atualizado, fruta a uva: ", frutas);
print();

#3 - remova a fruta "banana" da lista "frutas" utilizando o método remove(). Exiba a lista atualizada na tela.
frutas.remove("banana");
print("Remove, fruta a banana: ", frutas);
print();
 
#4 - Acesse o segundo elemento da lista "frutas" e armazene-o em uma variável chamada "fruta_selecionada". 
# Em seguida, exiba o valor armazenado na variável. 
frutas_selecionada = (frutas[2]);
print("Fruta de selecionada elemento a lista: ", frutas_selecionada);
print();

5# - Crie uma tupla chamada "cores" contendo as seguintes cores: 
#vermelho, azul, verde, amarelo e roxo. em seguida, exiba a tupla completa na tela.
tuplaCores = ["vermelho", "azul", "verde", "amarelo", "roxo"];
print("Listas de cores: ", tuplaCores);
print();

6# - Acesse o terceiro elemento da tupla "cores" e armazene-o em uma varivel chamada "cor_selecionada".
#em seguida, exiba o valor armazendado na variavel. 
cores_selecionada = (tuplaCores[2]);
print("Terceiro elemento, cores de selecionada: ", tuplaCores[2]);
print();

7# - tente adicionar a cor "laranja" â tupla "cores" e observe o resultado. 
#Explique o motivo pelo qual ocorreu um erro fazendo um comentario no codigo. 
tuplaCores.append("laranja");
print("encontro os cores um sim ou nao: ", tuplaCores);
print();


8# - Crie um dicionario chamado "aluno" contendo as seguindes informações: nome, idade e cidade. 
#ultilize as chaves "nome", "idade", e "cidade" para representar cada informação. em seguida, 
# exiba o dicionario completa tela.
aluno = {"nome": "Marlus", "Idade": 31 , "Cidade" : "Capão da canoa - RS"};
print("Representar cadas informação: ", aluno);
print()

9# - Acesse a idade do aluno no dicionario "aluno" e armazene-o em um variavel chamada "idade_aluno".
# em seguida, exiba o valor armazenado na variavel. 
idade_aluno = (aluno["Idade"]);
print("Idade do aluno no dicionário: ", aluno["Idade"]);
print();


10# - Adicione a informação do gÊnero do aluno ao dicionario "aluno" ultilzando a chave "genero" e o valor correspondente.
#exiba o dicionario atualizado na tela. 
generoAluno = ["Masculino"];
print("Gênero: ", generoAluno);
print()


11# - Remova a informação da cidade do dicionario "aluno" ultizando o método pop() e a chave correspondente.
#exiba o dicionario atualizado na tela. 
alunoRemovida = aluno.pop("Cidade");
print("Remova a informação da cidade do dicionário: ", alunoRemovida);
print();

