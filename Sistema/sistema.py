import json
from pontos.pontointeresse import Ponto
from ViaCirculacao.ViaCirculacao import ViaCirculacao
from Estruturas.Grafos.grafo import Grafo
from Estruturas.DoubleNode.doublenode import LinkedList
from constantes.constantes import FICHEIRO_JSON, R, MENU_CAT, MENU_ACESS, MENU_ALT, ERRO, OPCAO, MENU_ARESTAS, \
    MENU_REDE, MENU_VERTICE, FICHEIRO_REDE
from Funções.funcoes import verifica_strings, verifica_floats
import math as m


class Sistema:
    def __init__(self):
        """
        Inicializa uma nova instância da classe Sistema com uma lista encadeada vazia para armazenar
        os pontos de interesse.
        """
        self.pontos_interesse = LinkedList()
        self._categorias = ('natureza', 'gastronomia', 'lazer', 'cultura')
        self.rede_circulacao = Grafo()

    # Pontos
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
        for i in self.ordena_pesquisa(pontos):
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
        for i in self.ordena_sugestoes(pontos):
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

    def verifica_ponto(self, txt: str):
        while True:
            try:
                ponto = str(input(txt))
                if not self.pontos_interesse.pesquisa_designacao(ponto):
                    print("Introduza um Ponto válido")
                else:
                    break
            except ValueError:
                print('\nIntroduza uma latitude válida.\n')
        return ponto

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
                    categoria = verifica_strings("Categoria > ")
                    nova_categoria = list(ponto.get_categoria())
                    if categoria.lower() not in ponto.get_categoria():
                        nova_categoria.append(categoria)
                        ponto.set_categoria(tuple(nova_categoria))
                case '2':
                    categoria = verifica_strings("Categoria > ")
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
                    acess = verifica_strings("Acesso > ").lower()
                    if acess not in ponto.get_acessibilidade():
                        ponto.set_acess(acess)
                case '2':
                    acess = verifica_strings("Acesso > ").lower()
                    lista = ponto.get_acessibilidade()
                    if acess in lista:
                        lista.remove(acess)
                    else:
                        print("\nNão existe esse acesso que deseja remover\n")
                case '0':
                    break
                case _:
                    print("\nIntroduza uma opção válida\n")

    # Rede Circulacao
    def consultar_rede_circulacao(self) -> None:
        """
        
        :return:
        """
        self.rede_circulacao.draw_graph()

    def verifica_vertices(self, txt: str) -> str:
        """
        Função de input que vertifica se o ponto introduzido se encontra na Rede
        :param txt:
        :return:
        """
        while True:
            try:
                ponto = str(input(txt))
                if ponto not in self.rede_circulacao.get_vertices():
                    print("Introduza um Ponto válido")
                else:
                    break
            except ValueError:
                print('\nIntroduza uma latitude válida.\n')

        return ponto

    def interromper_via_circulacao(self, from_label: str, to_label: str, Origem: str, Destino: str) -> None:
        """
        Interrompe uma via na rede e tenta encontrar um caminho sem passar pela a aresta eliminada
        :param from_label:
        :param to_label:
        :param Origem:
        :param Destino:
        :return:
        """
        self.rede_circulacao.remover_aresta(from_label, to_label)
        print(self.rede_circulacao.caminhos_possiveis(Origem, Destino))

        return None

    def obter_itinerario(self, from_label: str, to_label: str):
        """
        Calcula e mostra o caminho mais curto na rede apartir de 2 pontos
        :param from_label:
        :param to_label:
        :return:
        """
        print(self.rede_circulacao.calcula_caminho(from_label, to_label))

    def gerir_rede_circulacao(self):
        """
        Menu para gerir a rede -> Arestas / Vertices
        :return:
        """
        while True:
            print(MENU_REDE)
            op = str(input(OPCAO))
            match op:
                case '1':
                    self.gerir_arestas()
                case '2':
                    self.gerir_vertices()
                case '0':
                    break

    def gerir_arestas(self) -> None:
        """
        Menu para gerir arestas da Rede -> Adicionar / Consultar / Remover
        :return:
        """
        while True:
            print(MENU_ARESTAS)
            op = str(input(OPCAO))
            match op:
                case '1':
                    self.listar_pontos()
                    from_label = verifica_strings("Vertice Principal")
                    to_label = verifica_strings("Vertice Adjacente")
                    velocidade_min = verifica_floats("Velocidade minima da via")
                    velocidade_max = verifica_floats("Velocidade max da via")
                    distancia = verifica_floats("Distancia da via")
                    via = ViaCirculacao(distancia, velocidade_min, velocidade_max)
                    self.rede_circulacao.adicionar_aresta(from_label, to_label, via)
                case '2':
                    print(self.rede_circulacao.get_edges())
                case '3':
                    print(str(self.rede_circulacao))
                    from_label = self.verifica_vertices("Vertice principal > ")
                    to_label = self.verifica_vertices("Vertice adjacente > ")
                    print(self.rede_circulacao.remover_aresta(from_label, to_label))
                case '0':
                    break
        return None

    def gerir_vertices(self) -> None:
        """
        Menu para gerir vertices da Rede -> Adicionar / Consultar / Remover
        :return:
        """
        while True:
            print(MENU_VERTICE)
            op = str(input(OPCAO))
            match op:
                case '1':
                    print("Designações > ", self.pontos_interesse.get_designacoes())
                    label = self.verifica_ponto("Ponto a adicionar > ")
                    print(self.rede_circulacao.adicionar_vertice(label))
                case '2':
                    print(self.rede_circulacao.get_vertices())
                case '3':
                    print(str(self.rede_circulacao))
                    label = self.verifica_vertices("Vertice a remover > ")
                    print(self.rede_circulacao.remover_vertice(label))
                case '0':
                    break
        return None

    def consultar_pontos_criticos(self):
        print(self.rede_circulacao.ponto_maios_saidas())
        print(self.rede_circulacao.ponto_mais_entradas())

    def startup(self) -> None:
        """
        É Chamada quando se cria o sistema para importar pontos de interesse e a rede
        :return:
        """
        self.importa_pontos()
        self.importa_rede()
        return None

    def importa_pontos(self):
        """
        Importa pontos de interesse pré-criados do ficheiro pontos-interesse.json
        :return:
        """
        with open(FICHEIRO_JSON, "r") as f:
            data = json.load(f)
            for p in data:
                ponto = Ponto(data[p]["id"], data[p]["designacao"], data[p]["Morada"], data[p]["Latitude"],
                              data[p]["Longitude"], data[p]["categoria"], data[p]["acess"], data[p]["visitas"],
                              data[p]["avaliacao"], data[p]["geo"],
                              data[p]["Suges"])
                self.pontos_interesse.add(ponto)

    def importa_rede(self) -> None:
        """
        Importa vertices e arestas do Json e cria ligações entre esses pontos
        :return:
        """
        with open(FICHEIRO_REDE, "r") as f:
            data = json.load(f)
            for p in data:
                self.rede_circulacao.adicionar_vertice(data[p]["Origem"])
                self.rede_circulacao.adicionar_vertice(data[p]["Destino"])
                via = ViaCirculacao(data[p]["Distancia"], data[p]["Velocidade_min"], data[p]["Velocidade_max"])
                self.rede_circulacao.adicionar_aresta(data[p]["Origem"], data[p]["Destino"], via)
        return None

    def consultar_rotas(self, Origem: str):
        """
        Mostra as rotas disponiveis entre 2 pontos da Rede
        :param Origem:
        :return:
        """
        print(self.rede_circulacao.arvore(Origem))

    def ordena_pesquisa(self, lista_de_pontos: list) -> list:
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

    def ordena_sugestoes(self, lista_de_pontos: list) -> list:
        """
        Ordena uma lista de objetos Ponto com base no número de visitas.
        :param lista_de_pontos: List: lista de objetos Ponto a ser ordenada.
        :return: List: lista de objetos Ponto ordenada pelo número de visitas.
        """
        if len(lista_de_pontos) > 1:

            pivo = len(lista_de_pontos) // 2
            direita = lista_de_pontos[:pivo]
            esquerda = lista_de_pontos[pivo:]

            self.ordena_sugestoes(direita)
            self.ordena_sugestoes(esquerda)

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
