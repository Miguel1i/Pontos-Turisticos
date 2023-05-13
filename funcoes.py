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
