# Lecture 04 

# Dictionary 

#    1. Criar um dicionário com dados de tipos diversos, inclusive contendo 
#       listas e tuplas, com chaves que podem conter, como dados, também 
#       dicionários aninhados. 

from datetime import date

datas = {   
            "id": 123, 
            "name": "Anderson", 
            "gender": 'M', 
            "birthday": date(1980,1,1), 
            "status": True,
            "address": {
                "street": "Street 01", 
                "district": "District 01", 
                "number": 59, 
                "state": "RJ", 
                "city": "Rio de Janeiro", 
                "complement": {
                    "street": "Alameda", 
                    "number": 3}
                },
            "functions": ["Programmer","Analyst","DBA"]
        }

#    2.  Criar um código que exemplifique a impressão desse dicionário de 
#       dados. 

print(datas)

#    3. Criar um código que exemplifique a impressão, por meio de sua chave, 
#       de algum dado do dicionário de dados anteriormente criado, seja esse 
#       dado não aninhado ou aninhado. 

print(datas["name"])
print(datas["address"]["complement"]["street"])
print(datas["address"]["complement"]["number"])


#    4.  Criar um código que exemplifique a alteração de algum dado do 
#       dicionário anteriormente criado. 

datas["address"]["complement"]["street"] = "Alameda das Paisagens"
print(datas)


#    5. Criar um código que exemplifique a impressão dos seguintes dados do 
#       dicionário anteriormente criado: chaves, valores e items. 

print(datas.keys())
print(datas.values())

for x in datas.values():
    if x is dict:
        dict_copy = x.copy()
        for y in dict_copy:
            print(y)
    if x is list:
        list_copy = x.copy()
        for y in list_copy:
            print(y)
    print(x)

#    6. Criar um código que exemplifique a impressão de um dado do 
#       dicionário de dados anteriormente criado, usando a chave desse dado e 
#       a função get(). 

print(datas.get("name"))

#    7. Criar um código que exemplifique a alteração de dados do dicionário 
#       utilizando update(). 

datas.update({"name": "Anderson C."})
print(datas)

# Set 

#    1. Criar um set de números. 

nums = {6,5,7,4,8,3,9,2,0,1} # SET
print(type(nums))

#    2.  Criar um código que exemplifique a execução de operações no set 
#       criado anteriormente, com os seguintes métodos: 

#       ●add(), remove(), pop() e clear(). 

nums.add(15252)
print(nums)

nums.remove(15252)
print(nums)

nums.pop() # remove o primeiro
print(nums)

nums.clear()
print(nums)

#    3. Criar dois sets de números e executar as seguintes funções: 

#       ●union() e intersection(). 

set1 = {3,9,2,5,0,1,6} 
set2 = {2,6,5,7,4,9,8}
print(len(set1), len(set2))

set_union = set1.union(set2)
print(len(set_union), set_union) # elimina os repetidos, porem, mostra 

set_inter = set1.intersection(set2)
print(len(set_inter), set_inter)  # mostra só os que são unicos entre ambos.

#    4.  Criar um set com um número inteiro e, em seguida, inserir o mesmo 
#       número, porém em ponto flutuante, e imprimi-lo. 

myset = {1, 1.0}
print(myset) # imprime só 1

myset = {1, 1.5}
print(myset) # imprime só 1 e 1.5