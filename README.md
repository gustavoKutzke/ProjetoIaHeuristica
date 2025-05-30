# 📦 Projeto: Simulação de Entregas Urbanas com IA

Este projeto implementa um sistema **multiagente simples** que simula entregas em um ambiente urbano 4x4. Dois algoritmos de busca (BFS e A*) são utilizados para comparar o desempenho na busca pelo melhor caminho, levando em consideração obstáculos e trânsito.

## 🧠 Objetivo

Demonstrar a aplicação de técnicas de **Inteligência Artificial**, como algoritmos de busca e funções heurísticas, para otimizar entregas em mapas dinâmicos, simulando situações do mundo real.

## 🧩 Estrutura do Projeto

projeto_entregas_modular/
├── main.py # Arquivo principal da simulação
├── algoritmos.py # Implementação dos algoritmos BFS e A*
├── heuristicas.py # Funções heurísticas utilizadas (Manhattan)
├── gerador_mapa.py # Geração de mapas com ou sem obstáculos e trânsito
├── utils.py # Funções auxiliares (exibir mapa, calcular custo etc.)

## 🚦 Legenda do Mapa

| Símbolo | Significado                |
|---------|----------------------------|
| `I`     | Início da entrega          |
| `D`     | Destino da entrega         |
| `.`     | Rua livre (movimento livre)|
| `#`     | Obstáculo (bloqueado)      |
| `T`     | Trânsito (custo maior)     |

## 🔍 Algoritmos Implementados

- **BFS (Busca em Largura)**: Algoritmo não heurístico que explora o mapa nível por nível.
- **A* (A Estrela)**: Algoritmo heurístico que usa a distância de Manhattan para guiar a busca.

## 🧪 Simulações Executadas

5 cenários diferentes são testados automaticamente:

1. **Sem obstáculos nem trânsito**
2. **Com obstáculos simples, sem trânsito**
3. **Com obstáculos e trânsito**
4. **Obstáculos aleatórios, sem trânsito**
5. **Obstáculos aleatórios, com trânsito**

## 📊 Métricas Apresentadas

Para cada simulação são exibidos:

- Caminho encontrado
- Número de passos
- Custo total da entrega

## ▶️ Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/projeto-entregas-ia.git
   cd projeto-entregas-ia
2. Execute
   python main.py

