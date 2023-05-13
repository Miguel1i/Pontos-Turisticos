from pontointeresse import Ponto
from doublenode import LinkedList
from variable import json_file
import json


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
        """
        Esta função retorna sempre o ultimo id criado na lista, assim o utilizador nao se preocupa ao inserir um id já utilizado
        :return:
        """
        return self.pontos_interesse.get_last_id()

    def grava(self):
        """
        Grava no ficheiro JSON todas as alterações feitas nos pontos de interesse
        :return:
        """
        cursor = self.pontos_interesse.get_head()
        try:
            with open(json_file, "r") as f:
                data = json.load(f)
                while cursor is not None:
                    data.update({str(cursor.get_data().get_id()): {"id": int(cursor.get_data().get_id()),
                                                                   "designacao": str(
                                                                       cursor.get_data().get_designacao()),
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
        except:
            print("Algo correu mal")
            raise

        try:
            with open("pontos-interesse.json", "w") as file:
                json.dump(data, file, indent=2)
        except:
            print("Não foi possivel abrir o ficheiro")
            raise
