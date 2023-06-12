from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from termcolor import colored, cprint

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
        cprint("================= Começo Troca Loja Física =================", 'red', 'on_cyan')
        printaCondicoes("Troca_Loja_Fisica")
        decisao = input("Digite '1' se seu produto atende a todas as condições e você deseja a troca pelo mesmo produto.\nDigite '2' se seu produto atende a todas as condições e você deseja a troca por outro produto.\nDigite '3' se ele não atende a todas as condições: ")
        if decisao == '1':
            print("Realizando troca em loja física para o produto '{}'" .format(self._produto.nome))
        if decisao == '2':
            novoProduto = input("Digite o nome do produto desejado: ")
            print("Realizando troca em loja física do produto '{}' para o produto '{}'".format(self._produto.nome, novoProduto))
        if decisao == '3':
            print("Infelizmente a troca em loja física para o produto '{}' não é possível de ser realizada" .format(self._produto.nome))
        cprint("================= Fim Troca Loja Física =================", 'red', 'on_cyan')
        pass
    
class Troca_Marketplace(Fluxo_de_Troca):
    def realizar_troca(self):
        cprint("================= Começo Troca Marketplace =================", 'red', 'on_cyan')
        print("Produto acordado com o parceiro, realizando troca em marketplace para o produto:", self._produto.nome)
        cprint("================= Fim Troca Marketplace =================", 'red', 'on_cyan')
        pass

class Troca_Site_Whatsapp(Fluxo_de_Troca):
    def realizar_troca(self):
        cprint("================= Começo Troca Site/Whatsapp =================", 'red', 'on_cyan')
        decisao = input("Digite '1' para Devolução/Arrependimento ou Insatisfação com o Produto\nDigite '2' para Troca por defeito: ")
        if decisao == '1':
            printaCondicoes("Troca_Site_Whatsapp_1")
            decisao = input("Digite '1' se seu produto atende a todas as condições e você deseja o reembolso e '2' se você não deseja: ")
            if decisao == '1':
                print("Infelizmente o reembolso para o produto '{}' não é possível de ser realizado" .format(self._produto.nome))
            if decisao == '2':
                print("Realizando reembolso para o produto {}, confira seu e-mail" .format(self._produto.nome))
            decisao = 13
        if decisao == '2':
            decisao = input("Para realizar a Troca/Reembolso pela loja física, digite '1'\nPelos Correios, digite '2': ")
            if decisao == '1':
                printaCondicoes("Troca_Loja_Fisica")
                decisao = input("Digite '1' se seu produto atende a todas as condições e você deseja a troca pelo mesmo produto.\nDigite '2' se seu produto atende a todas as condições e você deseja a troca por outro produto.\nDigite '3' se ele não atende a todas as condições: ")
                if decisao == '1':
                    print("Realizando troca em loja física para o produto '{}'" .format(self._produto.nome))
                if decisao == '2':
                    novoProduto = input("Digite o nome do produto desejado: ")
                    print("Realizando troca em loja física do produto '{}' para o produto '{}'".format(self._produto.nome, novoProduto))
                if decisao == '3':
                    print("Infelizmente a troca em loja física para o produto '{}' não é possível de ser realizada" .format(self._produto.nome))
                decisao = 13
            if decisao == '2':
                printaCondicoes("Troca_Site_Whatsapp_2")
                decisao = input("Digite '1' se seu produto atende a todas as condições e você deseja o reembolso e '2' se você não deseja: ")
                if decisao == '1':
                    print("Infelizmente o reembolso para o produto '{}' não é possível de ser realizado" .format(self._produto.nome))
                if decisao == '2':
                    print("Realizando reembolso para o produto {}, confira seu e-mail" .format(self._produto.nome))
        cprint("================= Fim Troca Site/Whatsapp =================", 'red', 'on_cyan')
        pass

def printaCondicoes(qualTroca):
    if qualTroca == "Troca_Loja_Fisica":
        condicoes = []
        condicoes.append("90 dias corridos já se passaram a partir da compra?")
        condicoes.append("A embalagem é a original, sem uso e com a etiqueta de identificação fixada?")
        condicoes.append("Possui a nota fiscal do produto?")
        condicoes.append("Seu produto é de valor igual ou maior do que o desejado?")
        condicoes.append("Se o produto desejado for de valor maior, você dejeja completar o valor faltante?")
        condicoes.append("Seu produto foi comprado em uma loja física?")
        condicoes.append("O produto desejado faz parte dessa loja?")

    if qualTroca == "Troca_Site_Whatsapp_1":
        condicoes = []
        condicoes.append("07 dias corridos a partir da entrega já passaram?")
        condicoes.append("O cancelamento e reembolso da compra será efetuado somente após o recebimento e conferência do produto em nosso centro de distribuição")
        condicoes.append("A postagem deverá ser feita em uma agência, com código fornecido após preenchimento de um formulário e, após isso, poderá ser escolhida a forma de reembolso")
        condicoes.append("Devolução pode ser parcial (sem frete) ou total (com frete incluso)")
    
    if qualTroca == "Troca_Site_Whatsapp_2":
        condicoes = []
        condicoes.append("90 dias corridos já se passaram a partir da compra?")
        condicoes.append("A embalagem é a original, sem uso e com a etiqueta de identificação fixada?")
        condicoes.append("Possui a nota fiscal do produto?")
        condicoes.append("Seu produto é de valor igual ou maior do que o desejado?")
        condicoes.append("Se o produto desejado for de valor maior, você dejeja completar o valor faltante?")
        condicoes.append("Seu produto foi comprado em uma loja física?")
        condicoes.append("O produto desejado faz parte dessa loja?")
        condicoes.append("Em casa de defeito no produto, será necessário o envio de imagens que comprovem tal situação")
        
    for i in condicoes:
        cprint(i, 'green', 'on_red')

produto = Produto('banana', 'fulano', '11/06/2023', True, True)
motivo = 'estragada'
decisor = Decisor(Troca_Loja_Fisica(produto, motivo))
print('Decisor está configurado para troca em loja física')
decisor.realizar_troca()
print('Decisor trocando para troca em marketplace')
decisor.fluxo = Troca_Marketplace(produto, motivo)
decisor.realizar_troca()
print('Decisor trocando para troca em Site/Whatsapp')
decisor.fluxo = Troca_Site_Whatsapp(produto, motivo)
decisor.realizar_troca()