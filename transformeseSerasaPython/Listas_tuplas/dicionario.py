meudicionario = {
    "nome": "Marlus",
    "Sobrenome": "Abbade",
    "Idade" : 31
    };

print(meudicionario);
print();

frutasDicionario = { 
    "maça": 3, 
    "banana": 6,
    "uva": 8,                      
    };

print("Significado encontrado no dicionario: " , frutasDicionario["maça"]);
print();
frutasDicionario["maça"] = 5;
frutasDicionario["laranja"] = 10;

print("Nova quantidade de maça: ", frutasDicionario["maça"]);
print();
print(frutasDicionario);


print(frutasDicionario);
print();

animaisDicionario = {};
animaisDicionario["Gato"] = "tom";
print(animaisDicionario);

aluno = {
    "nome"    : "Marlus", 
    "idade"   : 40, 
    "hobbies" : ["jogar", "esportes"]
};
print(aluno);

frutasDicionario = {
    "maça"      :  3, 
    "banana"    :  6,
    "uva"       :  8,
    "laranja"   : 10
};

print();
print("Qualidade de maça: ", frutasDicionario.get("maça"));
print("Qualidade de banana: ", frutasDicionario.get("banana"));
print("Qualidade de morango: ", frutasDicionario.get("morango", "Não foi encontrado a definição de morango"));
print();

elementoRemovido = frutasDicionario.pop("laranja");
print(elementoRemovido);
print();
print("dicionario atualizado: ", frutasDicionario);


frutasDicionario = {
    "maça"      :  3, 
    "banana"    :  6,
    "uva"       :  8,
    "laranja"   : 10
};

print();
print("Chaves encontradas no dicionario: ", frutasDicionario.keys())
print("Valores encontrados no dicionario: ", frutasDicionario.values());
print(frutasDicionario.items());