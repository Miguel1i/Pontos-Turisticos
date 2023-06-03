MENU = """──────────── MENU ────────────

1:  Adicionar ponto de interesse
2:  Alterar ponto de interesse
3:  Pesquisar ponto de interesse
4:  Assinalar e Avaliar ponto de interesse
5:  Consultar estatisticas das visistas aos ponto de interesse
6:  Obter sugestões de visitas a pontos de interesse
7:  Gerir rede de circulação
8:  Consultar rede de circulação
9:  Consultar pontos criticos da via de circulação
10: Interromper via de circulação
11: Obter itinerário
12: Consultar rotas para percursos de carro
0: Sair

──────────── END ────────────
"""

R = 6371

FICHEIRO_JSON = "../pontos-interesse.json"

OPCAO = "\nOp > "
ERRO = "\nIntroduza uma opção válida\n"
MENU_ALT = """────── Alterações ──────

1: Alterar categorias
2: Alterar acessibilidade
0: Voltar

────────── END  ────────"""

MENU_CAT = """────────── Categoria ──────────

1: Adicionar categoria
2: Remover categoria
0: Voltar

──────────    END    ──────────"""
MENU_ACESS = """────────── Acessibilidade ──────────

1: Adicionar acessibilidade
2: Remover acessibilidade
0: Voltar

──────────      END       ──────────"""


MENU_REDE = """────────── REDE ──────────

1: Gerir Arestas
2: Gerir Vertices
0: Voltar

──────────      END       ──────────"""

MENU_ARESTAS = """────────── ARESTAS ──────────

1: Adicionar Aresta
2: Consultar Aresta
3: Remover Aresta
0: Voltar

──────────      END       ──────────"""

MENU_VERTICE = """────────── VERTICES ──────────

1: Adicionar Vertice
2: Consultar Vertice
3: Remover Vertice
0: Voltar

──────────      END       ──────────"""