from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from termcolor import colored, cprint

class Produto:
    def __init__(self, nome, adquirido_por, adquirido_em,passivel_de_troca):
        self._nome = nome
        self._adquirido_por = adquirido_por
        self._adquirido_em = adquirido_em
        self._passivel_de_troca = passivel_de_troca
    
    def verificar_passivel_de_troca(self):
        if self._passivel_de_troca:
            return
        else:
            decisao = input("Digite '1' se o produto for não passível de troca, devolução ou cancelamento\nDigite '2' o produto não for passível de troca por defeito: ")
            if decisao == '1':
                decisao = input("Digite '1' se o produto foi adquirido em promoções como Black Friday, por exemplo\nDigite '2' se seu produto foi adquirido em uma loja física\nDigite '3' se é um cartão exclusivo (Xbox Live, PSN, etc...)")
                if decisao == '1':
                    print("Esse produto não é passível de devolução, sendo sua troca efetuada apenas por defeito e pelo mesmo produto.")
                if decisao == '2':
                    print("Esse produto não pode ser devolvido, apenas trocado.")
                if decisao == '3':
                    print("Esse produto não pode ser devolvido/trocado/reembolsado.")
                decisao = 13
            if decisao == '2':
                decisao = input("Digite '1' se o produto está dentre estes: Bicicletas, puericultura pesada (carrinhos, banheiras, cadeirinhas, etc), games, miniveículos e miniveículos elétricos\nDigite '2' se o produto está dentre estes: Lego, playmobil, quebra-cabeças e jogos\nDigite '3' se o produto está dentre estes: Produtos surpresa\nDigite '4' se o produto está dentre estes: Puericultura leve (bico de chupeta ou mamadeira, mamadeira, chupeta, mordedor, etc), papelaria, e vestuário\nDigite '5' se o produto está dentre estes: Brinquedos eletrônicos\nDigite '6' se o produto está dentre estes: Fantasias.")
                if decisao == '1':
                    print("Será necessário o acionamento da assistência técnica")
                if decisao == '2':
                    print("Será necessário acionar o fabricante, após isso as peças faltantes serão repostas")
                if decisao == '3':
                    print("Será necessário acionar o fabricante para análise")
                if decisao == '4':
                    print("Não há troca por defeito")
                if decisao == '5':
                    print("Será necessário acionar a assistência técnica")
                if decisao == '6':
                    print("Em lojas físicas, a troca de fantasias só podem ser feitas por outras fantasias. Já pelo site, a troca não é permitida, apenas a devolução do produto com estorno do valor.")
            exit()


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
        self._fluxo.realizar_troca()


class Fluxo_de_Troca(ABC):
    def __init__(self, produto: Produto):
        self._produto = produto
        
    @abstractmethod
    def realizar_troca(self):
        pass
    
    @abstractmethod
    def printaCondicoes(self):
        pass
    
class Troca_Loja_Fisica(Fluxo_de_Troca):
    def realizar_troca(self):
        cprint("================= Começo Troca Loja Física =================", 'red', 'on_cyan')
        self.printaCondicoes()
        decisao = input("Digite '1' se seu produto atende a todas as condições e você deseja a troca pelo mesmo produto.\nDigite '2' se seu produto atende a todas as condições e você deseja a troca por outro produto.\nDigite '3' se ele não atende a todas as condições: ")
        if decisao == '1':
            print("Realizando troca em loja física para o produto '{}'" .format(self._produto._nome))
        if decisao == '2':
            novoProduto = input("Digite o nome do produto desejado: ")
            print("Realizando troca em loja física do produto '{}' para o produto '{}'".format(self._produto._nome, novoProduto))
        if decisao == '3':
            print("Infelizmente a troca em loja física para o produto '{}' não é possível de ser realizada" .format(self._produto._nome))
        cprint("================= Fim Troca Loja Física =================", 'red', 'on_cyan')
        pass
    
    def printaCondicoes(self):
        condicoes = []
        condicoes.append("90 dias corridos já se passaram a partir da compra?")
        condicoes.append("A embalagem é a original, sem uso e com a etiqueta de identificação fixada?")
        condicoes.append("Possui a nota fiscal do produto?")
        condicoes.append("Seu produto é de valor igual ou maior do que o desejado?")
        condicoes.append("Se o produto desejado for de valor maior, você dejeja completar o valor faltante?")
        condicoes.append("Seu produto foi comprado em uma loja física?")
        condicoes.append("O produto desejado faz parte dessa loja?")
        for i in condicoes:
            cprint(i, 'green', 'on_red')
        
    
class Troca_Marketplace(Fluxo_de_Troca):
    def realizar_troca(self):
        cprint("================= Começo Troca Marketplace =================", 'red', 'on_cyan')
        print("Produto acordado com o parceiro, realizando troca em marketplace para o produto:", self._produto._nome)
        cprint("================= Fim Troca Marketplace =================", 'red', 'on_cyan')
        pass
    def printaCondicoes(self):
        return super().printaCondicoes()

class Troca_Site_Whatsapp(Fluxo_de_Troca):
    def realizar_troca(self):
        cprint("================= Começo Troca Site/Whatsapp =================", 'red', 'on_cyan')
        decisao = input("Digite '1' para Devolução/Arrependimento ou Insatisfação com o Produto\nDigite '2' para Troca por defeito: ")
        if decisao == '1':
            self.printaCondicoes("Troca_Site_Whatsapp_1")
            decisao = input("Digite '1' se seu produto atende a todas as condições e você deseja o reembolso e '2' se você não deseja: ")
            if decisao == '2':
                print("Infelizmente o reembolso para o produto '{}' não é possível de ser realizado" .format(self._produto._nome))
            if decisao == '1':
                print("Realizando reembolso para o produto {}, confira seu e-mail" .format(self._produto._nome))
            decisao = 13
        if decisao == '2':
            decisao = input("Para realizar a Troca/Reembolso pela loja física, digite '1'\nPelos Correios, digite '2': ")
            if decisao == '1':
                self.printaCondicoes("Troca_Loja_Fisica")
                decisao = input("Digite '1' se seu produto atende a todas as condições e você deseja a troca pelo mesmo produto.\nDigite '2' se seu produto atende a todas as condições e você deseja a troca por outro produto.\nDigite '3' se ele não atende a todas as condições: ")
                if decisao == '1':
                    print("Realizando troca em loja física para o produto '{}'" .format(self._produto._nome))
                if decisao == '2':
                    novoProduto = input("Digite o nome do produto desejado: ")
                    print("Realizando troca em loja física do produto '{}' para o produto '{}'".format(self._produto._nome, novoProduto))
                if decisao == '3':
                    print("Infelizmente a troca em loja física para o produto '{}' não é possível de ser realizada" .format(self._produto._nome))
                decisao = 13
            if decisao == '2':
                self.printaCondicoes("Troca_Site_Whatsapp_2")
                decisao = input("Digite '1' se seu produto atende a todas as condições e você deseja o reembolso e '2' se você não deseja: ")
                if decisao == '2':
                    print("Infelizmente o reembolso para o produto '{}' não é possível de ser realizado" .format(self._produto._nome))
                if decisao == '1':
                    print("Realizando reembolso para o produto {}, confira seu e-mail" .format(self._produto._nome))
        cprint("================= Fim Troca Site/Whatsapp =================", 'red', 'on_cyan')
        pass
    
    def printaCondicoes(self, qualTroca):
        if qualTroca =="Troca_Loja_Fisica":
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
            
    

print("Bem vindo ao fluxo de troca da riHappy, por favor digite o nome do produto que deseja trocar")

nome_produto = input("Nome do produto:\n")
adquirido_por_numero = input("Como o produto foi adquirido? Digite 1 para Site/Whatsapp, 2 para marketplace e 3 para loja física\n")
adquirido_por = ""
if(adquirido_por_numero == "1"):
    adquirido_por = "site/whatsapp"
elif(adquirido_por_numero == "2"):
    adquirido_por = "marketplace"
elif(adquirido_por_numero == "3"):
    adquirido_por = "loja_fisica"
else:
    raise Exception("Resposta inválida, encerrando fluxo")
    
adquirido_em = input("Qual a data que o produto foi adquirido? (dd/mm/yyyy)\n")
passivel_de_troca=False
print("Produtos não passíveis de troca:\n")
print("Cartões conteúdos como Google Play, Xbox Live, Playstation, etc \n")
print('''Lego, playmobil, quebra-cabeças e jogos, produtos surpresa,
      bicicletas, puericultura pesada (carrinhos, banheiras, cadeirinhas, etc),
      games, miniveículos e miniveículos elétricos,
      Puericultura leve (bico de chupeta ou mamadeira, mamadeira, chupeta, mordedor, etc),
      papelaria, e vestuário,
      Brinquedos eletrônicos,
      Fantasias.
      \n''')
passivel_de_troca_str = input("Seu produto está incluido nessa lista? Digite 's' para sim e 'n' para não\n")
if passivel_de_troca_str == 's':
    passivel_de_troca = False
elif passivel_de_troca_str == 'n':
    passivel_de_troca = True
else:
    raise Exception("Resposta inválida, encerrando fluxo")
    
produto = Produto(nome_produto, adquirido_por, adquirido_em, passivel_de_troca)
if produto._passivel_de_troca == False:
    print('Produto não passível de troca')
    produto.verificar_passivel_de_troca()
elif produto._adquirido_por == "loja_fisica":
    print('Decisor está configurado para troca em loja física')
    decisor = Decisor(Troca_Loja_Fisica(produto))
elif produto._adquirido_por == "site/whatsapp":
    print('Decisor trocando para troca em Site/Whatsapp')
    decisor = Decisor(Troca_Site_Whatsapp(produto))
elif produto._adquirido_por == "marketplace":
    print('Decisor trocando para troca em marketplace')
    decisor = Decisor(Troca_Marketplace(produto))

decisor.realizar_troca()