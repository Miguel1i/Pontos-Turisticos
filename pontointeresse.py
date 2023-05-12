from coordenada import Coordenada


class Ponto:

    def __init__(self, id_ponto: int, desigancao: str, morada: str, latitude: float, longitude: float, categoria: str, acessibilidade=None):
        self._id_ponto = id_ponto
        self._desgignacao: str = desigancao
        self._morada: str = morada
        self._coordenada: Coordenada = Coordenada(latitude, longitude)
        self._categoria: str = categoria
        self._acessibilidade = acessibilidade
        self._avaliacao = []
        self._visitas = 0

    def get_designacao(self):
        return self._desgignacao

    def get_morada(self) -> str:
        return self._morada

    def get_acessibilidade(self) -> list:
        return self._acessibilidade

    def get_categoria(self) -> str:
        return self._categoria

    def set_acessibilidade(self, item: str) -> None:
        self._acessibilidade.append(item)

    def set_categoria(self, categoria: str):
        self._categoria = categoria

    def set_morada(self, morada: str):
        self._morada = morada

    def set_coordenada(self, latitude, longitude):
        self._coordenada = Coordenada(latitude, longitude)

    def get_coordenadas(self):
        return str(self._coordenada)

    def __str__(self):
        return f'Categoria: {self._categoria} \nMorada: {self._morada} \nCoordenadas: {self._coordenada} \nAcessibilidade: {self._acessibilidade}'
