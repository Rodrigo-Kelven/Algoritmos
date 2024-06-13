def floyd_warshall(grafo):
  distancias = {}
  vertices = grafo.keys()

  # Inicialização da matriz de distâncias
  for u in vertices:
      distancias[u] = {}
      for v in vertices:
          if u == v:
              distancias[u][v] = 0
          elif v in grafo[u]:
              distancias[u][v] = grafo[u][v]
          else:
              distancias[u][v] = float('inf')

  # Algoritmo de Floyd-Warshall
  for k in vertices:
      for i in vertices:
          for j in vertices:
              distancias[i][j] = min(distancias[i][j], distancias[i][k] + distancias[k][j])

  return distancias

# Exemplo de uso:
grafo = {
  'A': {'B': 3, 'C': 8},
  'B': {'C': 1},
  'C': {'A': 4, 'B': 7}
}

resultado = floyd_warshall(grafo)
for origem in resultado:
  for destino in resultado[origem]:
      print(f"Caminho mais curto de {origem} para {destino}: {resultado[origem][destino]}")
