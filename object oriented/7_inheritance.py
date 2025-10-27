class Pessoa(object):
    
    def __init__(self, **kwargs):
        self.codigo = kwargs['codigo']
        self.nome = kwargs['nome']
        self.email = kwargs['email']

    def Imprimir(self):
        print(self.codigo)
        print(self.nome)
        print(self.email)

    def Mensagem(self):
        print('Original.')


class PessoaFisica(Pessoa):
    
    #Construindo chamando constructor pai.
    def __init__(self, **kwargs):
        return super().__init__(**kwargs)

    #def __init__(self, **kwargs):
    #    self.nome = "Jurandir"
    #    self.codigo = 0
    #    self.email = 'outro@yyy.xxx'

    def Mensagem(self):
        print('Remanufaturado.')
    
    #Chamando o método da classe pai.
    def Mensagem(self):
       super(PessoaFisica, self).Mensagem()

pf = PessoaFisica(codigo = 123, nome = 'Anderson', email='andconc@gmail.com')
pf.Mensagem()
pf.Imprimir()

print(issubclass(Pessoa, PessoaFisica))
print(issubclass(PessoaFisica, Pessoa))

