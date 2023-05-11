from pontointeresse import Ponto
import json


class Sistema:
    def __init__(self):
        """
        Método construtor da classe Sistema
        """
        self.pontos_interesse = None
        with open("pontos-interesse.json", "r") as f:
            data = json.load(f)
            for p in data:
                ponto = Ponto(data[p]['designacao'], data[p]['morada'], data[p]['latitude'], data[p]['longitude'], data[p]['categoria'], data[p]['acess'])

    def adicionar_ponto(self, ponto: Ponto) -> None:
        """
        Permite adicionar um novo ponto de interesse turístico.
        :return: None
        """
        pass

    def alterar_ponto(self) -> None:
        """
        Permite alterar as categorias e acessibilidade de um ponto de interesse turístico
        :return: None
        """
        pass

    def pesquisar_pontos(self):
        """
        Permite pesquisar pontos de interesse turísticos por categorias.
        :return:
        """

        pass

    def assinalar_avaliar_ponto(self):
        """
        Permite incrementar numa unidade o contador de visitas de um ponto de interesse turístico e atualizar as
        classificações da experiência da visita nesse ponto.
        :return:
        """
        pass

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
