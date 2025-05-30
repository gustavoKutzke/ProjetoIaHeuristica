
def exibir_mapa(mapa):
    for linha in mapa:
        print(' '.join(linha))  
    print()  
# Função que localiza uma célula específica no mapa ('I', 'D', etc.)
def encontrar(mapa, alvo):
    for i in range(len(mapa)):         
        for j in range(len(mapa[0])):   
            if mapa[i][j] == alvo:
                return (i, j)           
    return None                         

# Função que calcula o custo total de um caminho
# Cada célula normal custa 1, e células com trânsito ('T') custam 2
def calcular_custo(mapa, caminho):
    custo = 0
    for pos in caminho[1:]:            
        i, j = pos
        custo += 2 if mapa[i][j] == 'T' else 1
    return custo
