import random


def gerar_mapa(com_obstaculos=True, com_transito=True):
    
    mapa = [['.' for _ in range(4)] for _ in range(4)]
    
    
    mapa[random.randint(0,3)][random.randint(0,3)] = 'I'
    
  
    while True:
        x, y = random.randint(0,3), random.randint(0,3)
        if mapa[x][y] == '.':
            mapa[x][y] = 'D'
            break

   
    if com_obstaculos:
        for _ in range(3):
            x, y = random.randint(0,3), random.randint(0,3)
            if mapa[x][y] == '.':
                mapa[x][y] = '#'

    
    if com_transito:
        for _ in range(2):
            x, y = random.randint(0,3), random.randint(0,3)
            if mapa[x][y] == '.':
                mapa[x][y] = 'T'

   
    return mapa
