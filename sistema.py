from pontointeresse import Ponto
import json
from doublenode import LinkedList


class Sistema:
    def __init__(self):
        """
        Inicializa uma nova instância da classe Sistema com uma lista encadeada vazia para armazenar
        os pontos de interesse.
        """
        self.pontos_interesse = LinkedList()

    def adicionar_ponto(self, ponto: Ponto) -> None:
        """
        Permite adicionar um novo ponto de interesse.
        :return: None.
        """
        self.pontos_interesse.add(ponto)

    def alterar_ponto(self, _id, categoria, acess) -> None:
        """
        Permite alterar as categorias e acessibilidade de um ponto de interesse.
        :return: None.
        """
        self.pontos_interesse.altera(_id, categoria, acess)

    def pesquisar_pontos(self, categoria: str) -> None:
        """
        Permite pesquisar pontos de interesse turísticos por categorias e
        imprime na tela os pontos de interesse que correspondem à categoria especificada.
        :return: None.
        """
        self.pontos_interesse.pesquisa_por_categoria(categoria)

    def listar_pontos(self) -> None:
        """
        Imprime na tela todos os pontos de interesse.
        :return: None.
        """
        self.pontos_interesse.print_lista()

    def assinalar_avaliar_ponto(self, _id, avaliacao: int) -> None:
        """
        Permite incrementar numa unidade o contador de visitas de um ponto de interesse e atualizar as
        classificações da experiência da visita nesse ponto.
        :return: None.
        """
        self.pontos_interesse.assinala_avalia(_id, avaliacao)

    def consultar_estatisticas(self) -> None:
        """
        Imprime na tela os pontos de interesse, indicando o número de visitantes e a classificação média que
        foi atribuída.
        :return: None.
        """
        self.pontos_interesse.consultar_estatisticas()

    def obter_sugestoes(self, latitude: float, longitude: float) -> None:
        """
        Imprime na tela sugestões de pontos de interesse para visitar, considerando a proximidade a uma
        localização geográfica.
        :return: None.
        """
        self.pontos_interesse.obter_sugestoes(latitude, longitude)

    def get_last_id(self) -> int:
        """
        Método de obtenção do último ‘ID’ atribuído a um ponto de interesse.
        :return: O último ‘ID’ atribuído a um ponto de interesse.
        """
        return self.pontos_interesse.get_last_id()

    def grava(self) -> None:
        """
        Salva a lista que contém os pontos de interesse num ficheiro json.
        :return: None.
        """
        self.pontos_interesse.grava()
