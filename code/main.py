from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Produto:
    def __init__(self, nome, adquirido_por, adquirido_em, passivel_de_troca, integridade_fisica):
        self.nome = nome
        self.adquirido_por = adquirido_por
        self.adquirido_em = adquirido_em
        self.passivel_de_troca = passivel_de_troca
        self.integridade_fisica = integridade_fisica


class Decisor:
    def __init__(self, fluxo: Fluxo_de_Troca):
        self._fluxo = fluxo
        
    @property
    def fluxo(self) -> Fluxo_de_Troca:
        return self._fluxo
    
    @fluxo.setter
    def fluxo(self, fluxo: Fluxo_de_Troca):
        self._fluxo = fluxo
        
    def realizar_troca(self):
        print('Início do contexto')
        self._fluxo.realizar_troca()
        print('Fim do contexto')


class Fluxo_de_Troca(ABC):
    def __init__(self, produto: Produto, motivo_da_troca: str):
        self._produto = produto
        self._motivo_da_troca = motivo_da_troca
        
    @abstractmethod
    def realizar_troca(self):
        pass
    
class Troca_Loja_Fisica(Fluxo_de_Troca):
    def realizar_troca(self):
        printaCondicoes()
        decisao = input("Digite '1' se seu produto atende a todas as condições e você deseja a troca pelo mesmo produto.\nDigite '2' se seu produto atende a todas as condições e você deseja a troca por outro produto.\nDigite '3' se ele não atende a todas as condições.")
        if decisao == '1':
            print("Realizando troca em loja física para o produto '{}'" .format(self._produto.nome))
        if decisao == '2':
            novoProduto = input("Digite o nome do produto desejado: ")
            print("Realizando troca em loja física do produto '{}' para o produto '{}'".format(self._produto.nome, novoProduto))
        if decisao == '3':
            print("Infelizmente a troca em loja física para o produto '{}' não é possível de ser realizada" .format(self._produto.nome))
        pass
    
class Troca_Marketplace(Fluxo_de_Troca):
    def realizar_troca(self):
        print("Realizando troca em marketplace para o produto:", self._produto.nome)
        pass

def printaCondicoes():
    condicoes = []
    condicoes.append("90 dias corridos já se passaram a partir da compra?")
    condicoes.append("A embalagem é a original, sem uso e com a etiqueta de identificação fixada?")
    condicoes.append("Possui a nota fiscal do produto?")
    condicoes.append("Seu produto é de valor igual ou maior do que o desejado?")
    condicoes.append("Se o produto desejado for de valor maior, você dejeja completar o valor faltante?")
    condicoes.append("Seu produto foi comprado em uma loja física?")
    condicoes.append("O produto desejado faz parte dessa loja?")
    for i in condicoes:
        print(i)


produto = Produto('banana', 'fulano', '11/06/2023', True, True)
motivo = 'estragada'
decisor = Decisor(Troca_Loja_Fisica(produto, motivo))
print('Decisor está configurado para troca em loja física')
decisor.realizar_troca()
print('Decisor trocando para troca em marketplace')
decisor.fluxo = Troca_Marketplace(produto, motivo)
decisor.realizar_troca()
