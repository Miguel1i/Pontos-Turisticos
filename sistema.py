from pontointeresse import Ponto
import json
from doublenode import LinkedList


class Sistema:
    def __init__(self):
        """
        Método construtor da classe Sistema
        """
        self.pontos_interesse = LinkedList()

    def adicionar_ponto(self, ponto: Ponto) -> None:
        """
        Permite adicionar um novo ponto de interesse turísti
        :return: None
        """
        self.pontos_interesse.add(ponto)

    def alterar_ponto(self, _id, categoria, acess) -> None:
        """
        Permite alterar as categorias e acessibilidade de um ponto de interesse turístico
        :return: None
        """
        self.pontos_interesse.altera(_id, categoria, acess)

    def pesquisar_pontos(self):
        """
        Permite pesquisar pontos de interesse turísticos por categorias.
        :return:
        """
        self.pontos_interesse.print_lista()

    def assinalar_avaliar_ponto(self, _id, avaliacao: int):
        """
        Permite incrementar numa unidade o contador de visitas de um ponto de interesse turístico e atualizar as
        classificações da experiência da visita nesse ponto.
        :return:
        """
        self.pontos_interesse.assinala_avalia(_id, avaliacao)

    def consultar_estatisticas(self):
        """
        Mostra os pontos de interesse turísticos, indicando o número de visitantes e a classificação média que foi
        atribuída.
        :return:
        """
        pass

    def obter_sugestoes(self):
        """
        Sugere pontos de interesse turístico para visitar, considerando a proximidade a uma localização geográfica.
        :return:
        """
        pass


    def get_last_id(self):
        return self.pontos_interesse.get_last_id()