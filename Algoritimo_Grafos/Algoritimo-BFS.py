from collections import deque
"""
A caracteristica principal deste algoritimo é que para checar a distancia,
e o menor caminho a ser perccorido, o numero de segmentos tem que ser minimo possivel
Resumindo: quantos menos segmentos a serem percoridos de A ate B, melhor o caminho.
"""

def bfs(graph, start):
    # Cria uma fila para armazenar os nós a serem visitados 
    queue = deque([start])
    # Conjunto para armazenar os nós visitados
    visited = set([start])
    
    while queue:
        # Remove o nó da frente da fila
        node = queue.popleft()
        print(node)  # Processa o nó (neste caso, apenas imprime)

        # Itera sobre os vizinhos do nó atual
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)  # Marca o vizinho como visitado
                queue.append(neighbor)  # Adiciona o vizinho à fila

# Exemplo de uso
if __name__ == "__main__":
    # Representação do grafo como um dicionário
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    print("Percurso BFS a partir do nó A:")
    bfs(graph, 'A')
