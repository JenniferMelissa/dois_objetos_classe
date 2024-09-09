#Crie um programa que cria dois objetos da mesma classe (Pessoa), e mostre uma conversa amigável entre os dois objetos.

#NOTE: Criar classe
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self, pessoa1):
        return f'Olá, {pessoa1.nome}! Como vai?'
    
    def responder(self, pessoa2):
        return f'Estou bem! E você, {pessoa2.nome}?'
    
    def responder2(self, pessoa1):
        return f'Estou bem! Quantos anos você tem, {pessoa1.nome}?'
    
    def responder3(self,pessoa2):
        return f'Tenho {pessoa2.idade} anos. E você {pessoa1.nome}?'
    
    def responder4(self, pessoa1):
        return f'Tenho {pessoa1.idade} anos, {pessoa2.nome}.'
    
    def responder5(self,pessoa2):
        return f'Preciso ir agora, {pessoa1.nome}, depois nos falamos, tchau!'

# Criando dois objetos da classe Pessoa
pessoa1 = Pessoa(nome='Alice', idade=30)
pessoa2 = Pessoa(nome='Bob', idade=25)

# conversa
print(pessoa1.cumprimentar(pessoa2))
print(pessoa2.responder(pessoa1))
print(pessoa1.responder2(pessoa2))
print(pessoa2.responder3(pessoa1))
print(pessoa1.responder4(pessoa2))
print(pessoa1.responder5(pessoa1))
