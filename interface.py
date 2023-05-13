from pontointeresse import Ponto
from sistema import Sistema
from constantes import menu as m, menu_cat, menu_alterar, menu_acess, Opcao, ERRO
from os import system


def menu(sistema: Sistema):
    while True:
        print(m)
        ans = str(input('Escolha a opção >> '))
        match ans:
            case '1':
                system('cls')
                _id: int = sistema.get_last_id() + 1
                designacao: str = verifica_designacao()
                morada: str = verifica_morada().strip()
                latitude: float = verifica_latitude()
                longitude: float = verifica_longitude()
                categoria: str = verifica_categoria()
                access: str = verifica_access()
                geo: str = verifica_geografica()
                sugestao: str = verifica_sugestao()
                ponto: Ponto = Ponto(_id, designacao, morada, latitude, longitude, [categoria], [access], 0, [], [geo],
                                     [sugestao])
                sistema.adicionar_ponto(ponto)
                system('cls')
            case '2':
                system('cls')
                sistema.listar_pontos()
                _id = verifica_id(sistema)
                alterar(sistema, _id)
            case '3':
                system('cls')
                categoria = verifica_categoria()
                sistema.pesquisar_pontos(categoria)
            case '4':
                system('cls')
                sistema.listar_pontos()
                _id = verifica_id(sistema)
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

    return designacao.strip()


def verifica_categoria() -> str:
    """
    Pede ao utilizador para inserir uma categoria e só termina quando esta for válida.
    :return: Categoria: str
    """
    while True:
        categoria = str(input("Categoria > "))
        if not categoria:
            print('\nIntroduza uma categoria válida.\n')
        else:
            break
    return categoria.strip()


def verifica_avaliacao() -> int:
    """
    Pede ao utilizador para introduzir uma avaliaçao e só termina quando esta for 1, 2, 3 ou 4.
    :return: Avalicao: int
    """
    while True:
        try:
            avaliacao = int(input('Avaliação [1-4] > '))
            if avaliacao > 4 or avaliacao < 1:
                print('\nIntroduza um valor entre 1 e 4.\n')
            else:
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

    return access.strip()


def verifica_morada() -> str:
    """
    Pede ao utilizador para introduzir uma morada e só termina quando esta for válida.
    :return: Morada: str
    """
    while True:
        morada = str(input('Morada > '))
        if not morada:
            print('\nIntroduza uma morada válida.\n')
        else:
            break

    return morada.strip()


def verifica_sugestao() -> str:
    """
    Pede ao utilizador para introduzir uma sugestão e só termina quando esta for válida.
    :return: Sugestao: str
    """
    while True:
        sugestao = str(input('Sugestão > '))
        if not sugestao:
            print('\nIntroduza uma sugestão válida.\n')
        else:
            break

    return sugestao.strip()

def verifica_geografica() -> str:
    """
    Pede ao utilizador para introduzir uma geografica e só termina quando esta for válida.
    :return: Geo: str
    """
    while True:
        geo = str(input("Geografica > "))
        if not geo:
            print('\nIntroduza uma geografia válida.\n')
        else:
            break
    return geo.strip()

def verifica_id(_sistema: Sistema):
    while True:
        try:
            _id = int(input("ID > "))
            if _sistema.verifica_id(_id):
                return _id
            else:
                print('\nNão existe nenhum ponto de interesse com esse ID\n')
        except ValueError:
            print('\nIntroduza um número válido.\n')

def alterar(_sistema:  Sistema, _id):
    while True:
        print(menu_alterar)
        op = str(input(Opcao))
        match op:
            case '1':
                alterar_cat(_sistema, _id)
            case '2':
                altera_acessibilidade(_sistema, _id)
            case '0':
                break
            case _:
                print(ERRO)


def alterar_cat(_sistema: Sistema, _id: int) -> None:
    while True:
        print(menu_cat)
        op = str(input("Op > "))
        ponto = _sistema.pontos_interesse.pesquisa(_id)
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

def altera_acessibilidade(_sistema: Sistema, _id: int) -> None:
    while True:
        print(menu_acess)
        op = str(input("Op > "))
        ponto = _sistema.pontos_interesse.pesquisa(_id)
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
