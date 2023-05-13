from pontointeresse import Ponto
from constantes import menu as m
from os import system
from funcoes import verifica_categoria, verifica_latitude, verifica_sugestao, verifica_access, \
    verifica_designacao, verifica_geografica, verifica_morada, verifica_longitude, verifica_avaliacao

from sistema import Sistema

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
                sistema.alterar(_id)
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
