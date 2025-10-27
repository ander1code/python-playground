import datetime

class Pessoa(object):
    #private:
    
    def __init__(self, codigo, nome, dataNasc, renda, sexo):
        self.codigo = codigo
        self.nome = nome
        self.dataNasc = dataNasc
        self.renda = renda
        self.sexo = sexo

    def __str__(self):
        return '%i | %s | %s | %.2f | %s'%(self.codigo, self.nome, self.dataNasc, self.renda, self.sexo)

    def __add__(self, valor):
        self.renda += valor

    def __doc__(self):
        print('Classe pessoa para teste.')

    def __call__(self):
        print('Classe chamavel.')

  
#Utilizando a classe:
pes = Pessoa(123, 'Anderson', datetime.date(1981,11,12), 5653.32, 'M')
pes.__add__(3000)
pes.__call__
pes.__doc__
print(pes)

class Pai(object):
    pass
class Filho(Pai):
    pass
class Neto(Filho):
    pass

print(issubclass(Neto, Pai))
print(issubclass(Pai, Filho))
print(Pai.__bases__) #Herda de object.
print(Filho.__bases__)
print(Neto.__bases__)

print('callable(Pai) = %s' % (callable(Pai)))
print('callable(Pai) = %s' % (callable(Filho)))
print('callable(Neto) = %s' % (callable(Neto)))
print('callable(35) = %s' % (callable(35)))
