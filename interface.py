from pontointeresse import Ponto
from sistema import Sistema
from constantes import menu as m
from os import system


def menu(sistema: Sistema):
    while True:
        system('cls')
        print(m)
        ans = str(input('Escolha a opção >> '))
        match ans:
            case '1':
                system('cls')
                _id = sistema.get_last_id() + 1
                designacao = verifica_designacao()
                morada = verifica_morada()
                latitude = verifica_latitude()
                longitude = verifica_longitude()
                categoria = verifica_categoria()
                access = verifica_access()
                geo = verifica_geografica()
                sugestao = verifica_sugestao()
                ponto = Ponto(_id, designacao, morada, latitude, longitude, categoria, [access], 0, [], [geo],
                              [sugestao])
                sistema.adicionar_ponto(ponto)
                system('cls')
            case '2':
                system('cls')
                sistema.listar_pontos()
                _id = int(input('ID: '))
                categoria = verifica_categoria()
                access = verifica_access()
                sistema.alterar_ponto(_id, categoria, access)
                system('cls')
            case '3':
                system('cls')
                categoria = verifica_categoria()
                sistema.pesquisar_pontos(categoria)
            case '4':
                system('cls')
                sistema.listar_pontos()
                _id = int(input("id: "))
                avaliacao = verifica_avaliacao()
                sistema.assinalar_avaliar_ponto(_id, avaliacao)
                system('cls')
            case '5':
                system('cls')
                sistema.consultar_estatisticas()
            case '6':
                system('cls')
                latitude = verifica_latitude()
                longitude = verifica_longitude()
                sistema.obter_sugestoes(latitude, longitude)
            case '0':
                sistema.grava()
                break
            case _:
                system('cls')
                print("\nOpção inválida!\n")


def verifica_designacao() -> str:
    """
    Pede ao utilizador para inserir uma designação e só termina quando esta for válida.
    :return: Designacao: str
    """
    while True:
        designacao = str(input("Designacao > "))
        if designacao == '':
            print('\nIntroduza uma designacão válida.\n')
        else:
            break

    return designacao


def verifica_categoria() -> str:
    """
    Pede ao utilizador para inserir uma categoria e só termina quando esta for válida.
    :return: Categoria: str
    """
    while True:
        categoria = str(input("Categoria > "))
        if categoria == '':
            print('\nIntroduza uma categoria válida.\n')
        else:
            break
    return categoria


def verifica_avaliacao() -> int:
    """
    Pede ao utilizador para introduzir uma avaliaçao e só termina quando esta for 1, 2, 3 ou 4.
    :return: Avalicao: int
    """
    while True:
        try:
            avaliacao = int(input('Avaliação [1-4] > '))
            if avaliacao in [1, 2, 3, 4]:
                break
        except ValueError:
            print('\nIntroduza uma avaliação válida.\n')

    return avaliacao


def verifica_latitude() -> float:
    """
    Pede ao utilizador para introduzir uma latitude e só termina quando esta for válida.
    :return: Latitude: float
    """
    while True:
        try:
            latitude = float(input('Latitude > '))
            break
        except ValueError:
            print('\nIntroduza uma latitude válida.\n')

    return latitude


def verifica_longitude() -> float:
    """
    Pede ao utilizador para introduzir uma longitude e só termina quando esta for válida.
    :return: Longitude: float
    """
    while True:
        try:
            longitude = float(input('Longitude > '))
            break
        except ValueError:
            print('\nIntroduza uma longitude válida.\n')

    return longitude


def verifica_access() -> str:
    """
    Pede ao utilizador para introduzir um acesso e só termina quando esta for válida.
    :return: Acesso: str
    """
    while True:
        access = str(input('Acesso > '))
        if access == '':
            print('\nIntroduza um acesso válido.\n')
        else:
            break

    return access


def verifica_morada() -> str:
    """
    Pede ao utilizador para introduzir uma morada e só termina quando esta for válida.
    :return: Morada: str
    """
    while True:
        morada = str(input('Morada > '))
        if morada == '':
            print('\nIntroduza uma morada válida.\n')
        else:
            break

    return morada


def verifica_sugestao() -> str:
    """
    Pede ao utilizador para introduzir uma sugestão e só termina quando esta for válida.
    :return: Sugestao: str
    """
    while True:
        sugestao = str(input('Sugestão > '))
        if sugestao == '':
            print('\nIntroduza uma sugestão válida.\n')
        else:
            break

    return sugestao


def verifica_geografica() -> str:
    """
    Pede ao utilizador para introduzir uma geografica e só termina quando esta for válida.
    :return: Geo: str
    """
    while True:
        geo = str(input("Geografica > "))
        if geo == '':
            print('\nIntroduza uma geografia válida.\n')
        else:
            break

    return geo
