def verifica_strings(txt: str) -> str:
    """
    Pede ao utilizador para inserir uma designação e só termina quando esta for válida.
    :return: Designacao: str
    """
    while True:
        op = str(input(txt))
        if op == '':
            print('\nIntroduza uma designacão válida.\n')
        else:
            break

    return op

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


def verifica_floats(txt: str)-> float:
    """
    Pede ao utilizador para introduzir uma latitude e só termina quando esta for válida.
    :return: Latitude: float
    """
    while True:
        try:
            op = float(input(txt))
            break
        except ValueError:
            print('\nIntroduza uma latitude válida.\n')

    return op
