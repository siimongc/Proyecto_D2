import networkx as nx
import matplotlib.pyplot as plt


def dijkstra(graph, start):
    # Inicializar el diccionario de distancias con infinito para todos los nodos excepto el nodo de inicio
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Crear un conjunto para almacenar los nodos visitados
    visited = set()

    while visited != set(graph):
        # Buscar el nodo con la distancia más corta en el conjunto de nodos no visitados
        current_node = min(
            (node for node in graph if node not in visited), key=lambda n: distances[n])

        # Marcar el nodo actual como visitado
        visited.add(current_node)

        # Actualizar las distancias de los nodos vecinos si se encuentra un camino más corto
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                distance = distances[current_node] + graph[current_node][neighbor]['weight']
                if distance < distances[neighbor]:
                    distances[neighbor] = distance

    return distances


def plot_graph(graph, path):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_size=500, node_color='skyblue')

    edge_labels = {(u, v): graph[u][v]['weight'] for u, v in graph.edges}
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_color='red')

    path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='red', width=2)

    plt.show()


# Crear el grafo de ejemplo
graph = nx.Graph()
graph.add_edge('A', 'B', weight=4)
graph.add_edge('A', 'C', weight=2)
graph.add_edge('B', 'C', weight=1)
graph.add_edge('B', 'D', weight=5)
graph.add_edge('C', 'D', weight=8)
graph.add_edge('C', 'E', weight=10)
graph.add_edge('D', 'E', weight=2)
graph.add_edge('D', 'F', weight=6)
graph.add_edge('E', 'F', weight=2)

# Encontrar el camino más corto usando Dijkstra
start_node = 'A'
distances = dijkstra(graph, start_node)

# Imprimir las distancias mínimas desde el nodo de inicio
print("Distancias mínimas desde el nodo de inicio:")
for node, distance in distances.items():
    print(f"{node}: {distance}")

# Obtener el camino más corto desde el nodo de inicio al nodo 'F'
end_node = 'F'
path = nx.shortest_path(graph, start_node, end_node, weight='weight')

# Imprimir el camino más corto
print("Camino más corto:", ' -> '.join(path))

# Graficar el grafo y el camino más corto
plot_graph(graph, path)