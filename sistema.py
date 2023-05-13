from pontointeresse import Ponto
import json
from doublenode import LinkedList
from constantes import ficheiro_json, R
import math as m


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
        cursor = self.pontos_interesse.get_head()
        pontos = []

        while cursor is not None:
            pontos.append(cursor.get_data())
            cursor = cursor.get_next()

        self.pontos_interesse.set_head(None)
        for i in ordena_pesquisa(pontos):
            self.pontos_interesse.add(i)

        cursor = self.pontos_interesse.get_head()
        flag = 1
        while cursor is not None:
            if categoria.lower() in cursor.get_data().get_categoria():
                print(cursor.get_data())
                flag += 1
            cursor = cursor.get_next()

        if flag == 1:
            print('\nNão existe nenhum Ponto de Interesse com esta categoria.\n')

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
        ponto = self.pontos_interesse.pesquisa(_id)
        ponto.set_avaliacao(avaliacao)
        ponto.set_visitas()

    def verifica_id(self, _id: int):
        ponto = self.pontos_interesse.pesquisa(_id)

        if ponto is not None:
            return True
        else:
            return False

    def consultar_estatisticas(self) -> None:
        """
        Imprime na tela os pontos de interesse, indicando o número de visitantes e a classificação média que
        foi atribuída.
        :return: None.
        """
        cursor = self.pontos_interesse.get_head()
        while cursor is not None:
            ponto = cursor.get_data()
            if len(cursor.get_data().get_avaliacao()) > 0:
                media = sum(cursor.get_data().get_avaliacao()) / len(cursor.get_data().get_avaliacao())
                print(
                    f'\nID: {ponto.get_id()} \nDesignação: {ponto.get_designacao()} \nMorada: {ponto.get_morada()}'
                    f' \nSugestoes: {str(ponto.get_sugestoes())} '
                    f'\nMédia: {media} \nVisitas: {ponto.get_visitas()}\n')
            else:
                print(
                    f'\nID: {ponto.get_id()} \nDesignação: {ponto.get_designacao()} \nMorada: {ponto.get_morada()}'
                    f' \nSugestoes: {str(ponto.get_sugestoes())} '
                    f'\nMédia: {0} \nVisitas: {ponto.get_visitas()}\n')
            cursor = cursor.get_next()

    def obter_sugestoes(self, latitude: float, longitude: float) -> None:
        """
        Imprime na tela sugestões de pontos de interesse para visitar, considerando a proximidade a uma
        localização geográfica.
        :return: None.
        """
        cursor = self.pontos_interesse.get_head()
        pontos = []

        while cursor is not None:
            pontos.append(cursor.get_data())
            cursor = cursor.get_next()

        self.pontos_interesse.set_head(None)
        for i in ordena_sugestoes(pontos):
            self.pontos_interesse.add(i)

        cursor = self.pontos_interesse.get_head()
        flag = 1
        while cursor is not None:
            ponto = cursor.get_data().get_coordenadas()
            lat_diference = m.radians(latitude - ponto.get_latitude())
            lon_diference = m.radians(longitude - ponto.get_longitude())
            lat1 = m.radians(latitude)
            lat2 = m.radians(ponto.get_latitude())
            a = m.sin(lat_diference / 2) ** 2 + m.cos(lat1) * m.cos(lat2) * m.sin(lon_diference / 2) ** 2
            c = 2 * m.asin(m.sqrt(a))
            d = R * c

            if d <= 50:
                print(cursor.get_data())
                flag += 1

            cursor = cursor.get_next()

        if flag == 1:
            print('Não existe nenhum Ponto de Interesse perto.')

    def get_last_id(self) -> int:
        """
        Método de obtenção do último ‘ID’ atribuído a um ponto de interesse.
        :return: O último ‘ID’ atribuído a um ponto de interesse.
        """
        return self.pontos_interesse.get_last_id()

    def grava(self):
        cursor = self.pontos_interesse.get_head()
        with open(ficheiro_json, "r") as f:
            data = json.load(f)
            while cursor is not None:
                data.update({str(cursor.get_data().get_id()): {"id": int(cursor.get_data().get_id()),
                                                               "designacao": str(cursor.get_data().get_designacao()),
                                                               "Morada": str(cursor.get_data().get_morada()),
                                                               "Latitude": float(
                                                                   cursor.get_data().get_coordenadas().get_latitude()),
                                                               "Longitude": float(
                                                                   cursor.get_data().get_coordenadas().get_longitude()),
                                                               "categoria": str(cursor.get_data().get_categoria()),
                                                               "acess": cursor.get_data().get_acessibilidade(),
                                                               "geo": cursor.get_data().get_geo(),
                                                               "Suges": cursor.get_data().get_sugestoes(),
                                                               "avaliacao": cursor.get_data().get_avaliacao(),
                                                               "visitas": cursor.get_data().get_visitas()}})
                cursor = cursor.get_next()

        with open(ficheiro_json, "w") as file:
            json.dump(data, file, indent=2)


def ordena_pesquisa(lista_de_pontos: list) -> list:
    """
    Ordena a lista de objetos Ponto por ordem alfabética da designação.
    :param lista_de_pontos: List: lista de objetos Ponto a ser ordenada.
    :return: List: Lista ordenada por ordem alfabética da designação.
    """
    for i in range(1, len(lista_de_pontos)):
        key = lista_de_pontos[i]

        j = i - 1

        while j >= 0 and key.get_designacao() < lista_de_pontos[j].get_designacao():
            lista_de_pontos[j + 1] = lista_de_pontos[j]
            j = j - 1

        lista_de_pontos[j + 1] = key

    return lista_de_pontos


def ordena_sugestoes(lista_de_pontos: list) -> list:
    """
    Ordena uma lista de objetos Ponto com base no número de visitas.
    :param lista_de_pontos: List: lista de objetos Ponto a ser ordenada.
    :return: List: lista de objetos Ponto ordenada pelo número de visitas.
    """

    if len(lista_de_pontos) > 1:

        pivo = len(lista_de_pontos) // 2
        direita = lista_de_pontos[:pivo]
        esquerda = lista_de_pontos[pivo:]

        ordena_sugestoes(direita)
        ordena_sugestoes(esquerda)

        i = j = k = 0

        while i < len(direita) and j < len(esquerda):
            if direita[i].get_visitas() > esquerda[j].get_visitas():
                lista_de_pontos[k] = direita[i]
                i += 1
            else:
                lista_de_pontos[k] = esquerda[j]
                j += 1
            k += 1

        while i < len(direita):
            lista_de_pontos[k] = direita[i]
            i += 1
            k += 1

        while j < len(esquerda):
            lista_de_pontos[k] = esquerda[j]
            j += 1
            k += 1

    return lista_de_pontos
