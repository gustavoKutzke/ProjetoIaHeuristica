from collections import deque
from heapq import heappop, heappush
from heuristicas import manhattan  

# Algoritmo de Busca em Largura (BFS) - não heurístico
def bfs(mapa, inicio, destino):
    fila = deque([(inicio, [inicio])])  
    visitados = set()  

    while fila:
        atual, caminho = fila.popleft()

        if atual == destino:
            return caminho  

        if atual in visitados:
            continue

        visitados.add(atual)

       
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            ni, nj = atual[0] + dx, atual[1] + dy
           
            if 0 <= ni < 4 and 0 <= nj < 4 and mapa[ni][nj] != '#' and (ni,nj) not in visitados:
                fila.append(((ni, nj), caminho + [(ni, nj)]))

    return []  

# Algoritmo A* (A Estrela) - busca informada com heurística
def a_estrela(mapa, inicio, destino):
    
    fila = []
    heappush(fila, (manhattan(inicio, destino), 0, inicio, [inicio]))  # f(n) = g(n) + h(n)

    visitados = set()

    while fila:
        _, custo, atual, caminho = heappop(fila)

        if atual == destino:
            return caminho 

        if atual in visitados:
            continue

        visitados.add(atual)

        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            ni, nj = atual[0] + dx, atual[1] + dy

            if 0 <= ni < 4 and 0 <= nj < 4 and mapa[ni][nj] != '#' and (ni, nj) not in visitados:
                # Custo adicional se houver trânsito
                novo_custo = custo + (2 if mapa[ni][nj] == 'T' else 1)
                heuristica = manhattan((ni, nj), destino)
                f_total = novo_custo + heuristica  
                heappush(fila, (f_total, novo_custo, (ni, nj), caminho + [(ni, nj)]))

    return [] 
