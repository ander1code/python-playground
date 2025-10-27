import datetime

class Pessoa(object):
    #private:
    __codigo = 123
    __dataNasc = datetime.date(1981,11,12)
    __renda = 5653.32
    __sexo = 'M'

    def __Metodo(self):
        print('Metodo da Pessoa.')

    #public:
    nome = 'Anderson'

  
#Utilizando a classe:
pes = Pessoa()
pes.nome = 'Mara'
print(pes.nome)


#Tentando acessar um método private:
#    pes.Metodo()
#    AttributeError: 'Pessoa' object has no attribute 'Metodo'
#pes.Metodo()

