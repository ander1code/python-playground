import datetime

class Pessoa(object):
    codigo = 123
    nome = 'Anderson'
    dataNasc = datetime.date(1981,11,12)
    renda = 5653.32
    sexo = 'M'

#Utilizando a classe:

print(Pessoa.nome)
p = Pessoa()
print(p.nome)

if(id(Pessoa.nome) == id(p.nome)):
    print('IDs iguais!')

Pessoa.nome = 'João'
print(p.nome)
