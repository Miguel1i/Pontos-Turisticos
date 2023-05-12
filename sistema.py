from pontointeresse import Ponto
from doublenode import LinkedList


class Sistema:
    def __init__(self):
        """
        Método construtor da classe Sistema
        """
        self.pontos_interesse: LinkedList = LinkedList()

    def adicionar_ponto(self, ponto: Ponto) -> None:
        """
        Permite adicionar um novo ponto de interesse turísti
        :return: None
        """
        self.pontos_interesse.add(ponto)

    def alterar_ponto(self, _id: int, categoria: str, acess) -> None:
        """
        Permite alterar as categorias e acessibilidade de um ponto de interesse turístico
        :return: None
        """
        self.pontos_interesse.altera(_id, categoria, acess)

    def pesquisar_pontos(self, categoria: str):
        """
        Permite pesquisar pontos de interesse turísticos por categorias.
        :return:
        """
        self.pontos_interesse.pesquisa_por_categoria(categoria)

    def listar_pontos(self):
        self.pontos_interesse.print_lista()

    def assinalar_avaliar_ponto(self, _id: int, avaliacao: int):
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
        self.pontos_interesse.consultar_estatisticas()

    def obter_sugestoes(self, latitude: float, longitude: float):
        """
        Sugere pontos de interesse turístico para visitar, considerando a proximidade a uma localização geográfica.
        :return:
        """
        self.pontos_interesse.obter_sugestoes(latitude, longitude)

    def get_last_id(self):
        return self.pontos_interesse.get_last_id()

    def grava(self):
        self.pontos_interesse.grava()
