from coordenada import Coordenada
from typing import Optional


class Ponto:

    def __init__(self, id_ponto: int, desigancao: str, morada: str, latitude: float, longitude: float, categoria: str,
                 acessibilidade: Optional['list'], visitas: int, avaliacao: list, geografica=None, sugestoes=None,):
        self._id_ponto = id_ponto
        self._desgignacao: str = desigancao
        self._morada: str = morada
        self._coordenada: Coordenada = Coordenada(latitude, longitude)
        self._categoria: str = categoria
        self._acessibilidade = acessibilidade
        self._geografica: list = geografica
        self._sugestoes: list = sugestoes
        self._avaliacao: list = avaliacao
        self._visitas: int = visitas

    def get_id(self) -> int:
        return self._id_ponto

    def get_designacao(self) -> str:
        return self._desgignacao

    def get_morada(self) -> str:
        return self._morada

    def get_acessibilidade(self) -> list:
        return self._acessibilidade

    def get_categoria(self) -> str:
        return self._categoria

    def set_acessibilidade(self, item: str) -> None:
        self._acessibilidade.append(item)

    def set_categoria(self, categoria: str) -> None:
        self._categoria = categoria

    def set_morada(self, morada: str) -> None:
        self._morada = morada

    def set_coordenada(self, latitude, longitude) -> None:
        self._coordenada = Coordenada(latitude, longitude)

    def get_coordenadas(self) -> Coordenada:
        return self._coordenada

    def get_visitas(self) -> int:
        return self._visitas

    def get_avaliacao(self) -> list:
        return self._avaliacao

    def set_avaliacao(self, avaliacao: int) -> None:
        self._avaliacao.append(avaliacao)

    def set_visitas(self) -> None:
        self._visitas += 1

    def get_sugestoes(self) -> list:
        return self._sugestoes

    def get_geo(self) -> list:
        return self._geografica

    def set_acess(self, acess: str) -> None:
        self._acessibilidade.append(acess)

    def __str__(self) -> str:
        return f'\nID: {self._id_ponto} \nDesignação: {self._desgignacao} \nCategoria: {self._categoria}' \
               f' \nMorada: {self._morada}' \
               f' \nCoordenadas: {self._coordenada} \nAcessibilidade: {str(self._acessibilidade)}' \
               f' \ngeografica: {str(self._geografica)} \nSugestoes: {str(self._sugestoes)}' \
               f'\nAvaliação: {str(self._avaliacao)} \nVisitas: {self._visitas}\n'
