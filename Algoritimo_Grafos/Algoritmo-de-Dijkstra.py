import heapq

def dijkstra(grafo, inicio):
    distancias = {vertice: float('inf') for vertice in grafo}
    distancias[inicio] = 0
    fila = [(0, inicio)]

    while fila:
        distancia_atual, vertice_atual = heapq.heappop(fila)

        if distancia_atual > distancias[vertice_atual]:
            continue

        for vizinho, peso in grafo[vertice_atual].items():
            distancia = distancia_atual + peso
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                heapq.heappush(fila, (distancia, vizinho))

    return distancias

"""
mas qual é a ideia principal deste algoritimo? 
Este algotimo mede os pesos dos SEGMENTOS, segmentos estes que será os pssivel caminhos percorridos
"""

# Exemplo de uso:
grafo = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 3, 'B': 2, 'D': 4, 'E': 2},
    'D': {'B': 1, 'C': 4, 'E': 1},
    'E': {'C': 2, 'D': 1}
}

inicio = 'A'
print(dijkstra(grafo, inicio))
