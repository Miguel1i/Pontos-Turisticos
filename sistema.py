from pontointeresse import Ponto
import json
from doublenode import LinkedList
from constantes import FICHEIRO_JSON, R, MENU_CAT, MENU_ACESS, MENU_ALT, ERRO, OPCAO
from funcoes import verifica_access, verifica_categoria
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

    def alterar_ponto(self, _id: int) -> None:
        """
        Permite alterar as categorias e acessibilidade de um ponto de interesse.
        :return: None.
        """
        self.alterar(_id)

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

    def verifica_id(self, _id: int) -> bool:
        """
        verifica se existe o ID no sistema
        :param _id:
        :return : bool.
        """
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
                    f'\nSugestões: {str(ponto.get_sugestoes())} '
                    f'\nMédia: {media} \nVisitas: {ponto.get_visitas()}\n')
            else:
                print(
                    f'\nID: {ponto.get_id()} \nDesignação: {ponto.get_designacao()} \nMorada: {ponto.get_morada()}'
                    f' \nSugestões: {str(ponto.get_sugestoes())} '
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
        """
        Grava as alterações feitas aos pontos de interesse no ficheiro json
        :return:
        """
        cursor = self.pontos_interesse.get_head()
        with open(FICHEIRO_JSON, "r") as f:
            data = json.load(f)
            while cursor is not None:
                data.update({str(cursor.get_data().get_id()): {"id": int(cursor.get_data().get_id()),
                                                               "designacao": str(cursor.get_data().get_designacao()),
                                                               "Morada": str(cursor.get_data().get_morada()),
                                                               "Latitude": float(
                                                                   cursor.get_data().get_coordenadas().get_latitude()),
                                                               "Longitude": float(
                                                                   cursor.get_data().get_coordenadas().get_longitude()),
                                                               "categoria": list(cursor.get_data().get_categoria()),
                                                               "acess": cursor.get_data().get_acessibilidade(),
                                                               "geo": cursor.get_data().get_geo(),
                                                               "Suges": cursor.get_data().get_sugestoes(),
                                                               "avaliacao": cursor.get_data().get_avaliacao(),
                                                               "visitas": cursor.get_data().get_visitas()}})
                cursor = cursor.get_next()

        with open(FICHEIRO_JSON, "w") as file:
            json.dump(data, file, indent=2)

    def alterar(self, _id: int):
        """
        Menu de alterações do ponto de interesse que corresponde ao id em questão
        É possivel alterar as categorias e os meios de acesso
        :param _id:
        :return:
        """
        while True:
            print(MENU_ALT)
            op = str(input(OPCAO))
            match op:
                case '1':
                    self.alterar_cat(_id)
                case '2':
                    self.altera_acessibilidade(_id)
                case '0':
                    break
                case _:
                    print(ERRO)

    def alterar_cat(self, _id: int) -> None:
        """
        Menu de alteração de categorias
        :param _id:
        :return:
        """
        while True:
            print(MENU_CAT)
            op = str(input(OPCAO))
            ponto = self.pontos_interesse.pesquisa(_id)
            match op:
                case '1':
                    print("Categorias: ", ponto.get_categoria())
                    categoria = verifica_categoria()
                    nova_categoria = list(ponto.get_categoria())
                    if categoria.lower() not in ponto.get_categoria():
                        nova_categoria.append(categoria)
                        ponto.set_categoria(tuple(nova_categoria))
                case '2':
                    categoria = verifica_categoria()
                    nova_categoria = list(ponto.get_categoria())
                    if categoria.lower() in ponto.get_categoria():
                        nova_categoria.remove(categoria)
                        ponto.set_categoria(tuple(nova_categoria))
                    else:
                        print("\nNão existe essa Categoria que deseja remover\n")
                case '0':
                    break
                case _:
                    print("\nIntroduza uma opção válida\n")

    def altera_acessibilidade(self, _id: int) -> None:
        """
        Menu de alteração de acessos
        :param _id:
        :return:
        """
        while True:
            print(MENU_ACESS)
            op = str(input(OPCAO))
            ponto = self.pontos_interesse.pesquisa(_id)
            match op:
                case '1':
                    print("Acessos: ", ponto.get_acessibilidade())
                    acess = verifica_access().lower()
                    if acess not in ponto.get_acessibilidade():
                        ponto.set_acess(acess)
                case '2':
                    acess = verifica_access().lower()
                    lista = ponto.get_acessibilidade()
                    if acess in lista:
                        lista.remove(acess)
                    else:
                        print("\nNão existe esse acesso que deseja remover\n")
                case '0':
                    break
                case _:
                    print("\nIntroduza uma opção válida\n")

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
