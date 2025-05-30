
from gerador_mapa import gerar_mapa                  
from utils import exibir_mapa, encontrar, calcular_custo  
from algoritmos import bfs, a_estrela              


cenarios = [
    ("Cenário 1: Sem obstáculos e sem trânsito", False, False),
    ("Cenário 2: Obstáculo padrão (1) sem trânsito", True, False),
    ("Cenário 3: Obstáculo padrão com trânsito", True, True),
    ("Cenário 4: Obstáculos aleatórios sem trânsito", True, False),
    ("Cenário 5: Obstáculos aleatórios com trânsito", True, True)
]


def simular_entregas():
  
    print("LEGENDA DO MAPA: I = Início | D = Destino | . = Livre | # = Obstáculo | T = Trânsito (custo maior)\n")

    
    for i, (nome, obstaculos, transito) in enumerate(cenarios, start=1):
        print(f"--- Simulação {i} ---")
        print(nome)

        # Gera um mapa conforme o cenário atual (com/sem obstáculos e trânsito)
        mapa = gerar_mapa(com_obstaculos=obstaculos, com_transito=transito)

       
        exibir_mapa(mapa)

       
        inicio = encontrar(mapa, 'I')
        destino = encontrar(mapa, 'D')

        # Execução e resultados do algoritmo BFS
        print("Resultado com BFS:")
        caminho_bfs = bfs(mapa, inicio, destino)
        print("Caminho:", caminho_bfs)
        print("Passos:", len(caminho_bfs))
        print("Custo total:", calcular_custo(mapa, caminho_bfs))

        # Execução e resultados do algoritmo A*
        print("\nResultado com A*:")
        caminho_astar = a_estrela(mapa, inicio, destino)
        print("Caminho:", caminho_astar)
        print("Passos:", len(caminho_astar))
        print("Custo total:", calcular_custo(mapa, caminho_astar))

        print("\n" + "="*50 + "\n") 


if __name__ == '__main__':
    simular_entregas()
