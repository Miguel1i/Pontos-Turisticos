from pontos.pontointeresse import Ponto
from constantes.constantes import MENU
from os import system
from Funções.funcoes import verifica_strings, verifica_avaliacao, verifica_floats
import time
from Sistema.sistema import Sistema

def menu(sistema: Sistema):
    while True:
        print(MENU)
        ans = str(input('Escolha a opção >> '))
        match ans:
            case '1':
                system('cls')
                _id: int = sistema.get_last_id() + 1
                designacao: str = verifica_strings("Designação > ")
                morada: str = verifica_strings("Morada > ")
                latitude: float = verifica_floats("Latitude > ")
                longitude: float = verifica_floats("Longitude > ")
                categoria: str = verifica_strings("Categoria > ")
                access: str = verifica_strings("Acesso > ")
                geo: str = verifica_strings("Geografica >  ")
                sugestao: str = verifica_strings("Sugestão > ")
                ponto: Ponto = Ponto(_id, designacao, morada, latitude, longitude, [categoria], [access], 0, [], [geo],
                                     [sugestao])
                sistema.adicionar_ponto(ponto)
                print('\nPonto de interesse adicionado!\n')
                time.sleep(1)
                system('cls')
            case '2':
                system('cls')
                sistema.listar_pontos()
                _id = verifica_id(sistema)
                sistema.alterar(_id)
            case '3':
                system('cls')
                categoria = verifica_strings("Categoria > ")
                sistema.pesquisar_pontos(categoria)
            case '4':
                system('cls')
                sistema.listar_pontos()
                _id = verifica_id(sistema)
                avaliacao = verifica_avaliacao()
                sistema.assinalar_avaliar_ponto(_id, avaliacao)
                print('\nPonto de interesse avaliado!\n')
                time.sleep(1)
                system('cls')
            case '5':
                system('cls')
                sistema.consultar_estatisticas()
            case '6':
                system('cls')
                latitude = verifica_floats("Latitude > ")
                longitude = verifica_floats("Longitude > ")
                sistema.obter_sugestoes(latitude, longitude)
            case '0':
                sistema.grava()
                break
            case _:
                system('cls')
                print("\nOpção inválida!\n")


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
