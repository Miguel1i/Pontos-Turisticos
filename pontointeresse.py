from coordenada import Coordenada
from typing import Optional


class Ponto:

    def __init__(self, id_ponto: int, desigancao: str, morada: str, latitude: float, longitude: float, categoria: str,
                 acessibilidade: Optional['list'], visitas: int, avaliacao: list, geografica=None, sugestoes=None, ):
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
        """
        Retorna o id do ponto
        :return:
        """
        return self._id_ponto

    def get_designacao(self) -> str:
        """
        Retorna a designação do ponto
        :return:
        """
        return self._desgignacao

    def get_morada(self) -> str:
        """
        Retorna a morada do ponto
        :return:
        """
        return self._morada

    def get_acessibilidade(self) -> list:
        """
        Retorna os tipos de acesso ao ponto de interesse
        :return:
        """
        return self._acessibilidade

    def get_categoria(self) -> str:
        """
        Retorna a categoria que o ponto se encontra
        :return:
        """
        return self._categoria

    def set_acessibilidade(self, item: str) -> None:
        self._acessibilidade.append(item)

    def set_categoria(self, categoria: str) -> None:
        self._categoria = categoria

    def set_morada(self, morada: str) -> None:
        """

        :param morada:
        :return:
        """
        self._morada = morada

    def set_coordenada(self, latitude, longitude) -> None:
        """
        Cria uma nova coordenada no ponto
        :param latitude:
        :param longitude:
        :return:
        """
        self._coordenada = Coordenada(latitude, longitude)

    def get_coordenadas(self) -> Coordenada:
        """
        Retorna a coordenada do ponto de interesse
        :return:
        """
        return self._coordenada

    def get_visitas(self) -> int:
        """
        Retorna o numero de vezes que o ponto de interesse foi visitado
        :return:
        """
        return self._visitas

    def get_avaliacao(self) -> list:
        """
        Retorna as avalicações do ponto de interesse
        :return:
        """
        return self._avaliacao

    def set_avaliacao(self, avaliacao: int) -> None:
        """
        Adiciona uma avaliação ao ponto de interesse
        :param avaliacao:
        :return:
        """
        self._avaliacao.append(avaliacao)

    def set_visitas(self, valor=1) -> None:
        """
        Incrementa 1 ao valor das visitas quando este é visitado
        :param valor:
        :return:
        """
        self._visitas += valor

    def get_sugestoes(self) -> list:
        """
        Retorna as sugestões do ponto de interesse
        :return:
        """
        return self._sugestoes

    def get_geo(self) -> list:
        """
        Retorna os meios que se pode visitar o ponto de interesse
        :return list:
        """
        return self._geografica

    def set_acess(self, acess: str) -> None:
        """
        Adiciona um acesso ao ponto de interesse
        :param acess:
        :return None:
        """
        self._acessibilidade.append(acess)

    def __str__(self) -> str:
        """
        Retorna o ponto de interesse
        :return:
        """
        return f'\nID: {self._id_ponto} \nDesignação: {self._desgignacao} \nCategoria: {self._categoria}' \
               f' \nMorada: {self._morada}' \
               f' \nCoordenadas: {self._coordenada} \nAcessibilidade: {str(self._acessibilidade)}' \
               f' \ngeografica: {str(self._geografica)} \nSugestoes: {str(self._sugestoes)}' \
               f'\nAvaliação: {str(self._avaliacao)} \nVisitas: {self._visitas}\n'
