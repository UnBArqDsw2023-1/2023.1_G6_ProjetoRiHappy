from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Decisor():
    def __init__(self, fluxo):
        self._fluxo = fluxo
        
    @property
    def fluxo(self):
        return self._fluxo
    
    @fluxo.setter
    def fluxo(self, fluxo):
        self._fluxo = fluxo
        
    def realizar_troca(self):
        print('inicio do context')
        self._fluxo.realizar_troca()
        print('fim do contexto')


class Fluxo_de_Troca(ABC):
    def __init__(self, produto, motivo_da_troca):
        self._produto = produto
        self._motivo_da_troca = motivo_da_troca
        
    @abstractmethod
    def realizar_troca(self):
        pass
    
class Troca_Loja_Fisica(Fluxo_de_Troca):
    def realizar_troca(self):
        print("trocando dentro da classe de loja fisica")
        pass
    
class Troca_Marketplace(Fluxo_de_Troca):
    def realizar_troca(self):
        print("trocando dentro do marketplace")
        pass


produto = 'banana'
motivo = 'estragada'
decisor = Decisor(Troca_Loja_Fisica(produto,motivo))
print('decisor está setado para troca de loja fisica')
decisor.realizar_troca()
print('decisor trocando para troca marketplace')
decisor.fluxo = Troca_Marketplace(produto,motivo)
decisor.realizar_troca()

        