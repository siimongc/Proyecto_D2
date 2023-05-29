import networkx as nx
import matplotlib.pyplot as plt


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    visited = set()

    while visited != set(graph):
        current_node = min(
            (node for node in graph if node not in visited), key=lambda n: distances[n])

        visited.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                distance = distances[current_node] + graph[current_node][neighbor]['weight']
                if distance < distances[neighbor]:
                    distances[neighbor] = distance

    return distances


def plot_graph(graph, shortest_path=None):
    plt.figure(figsize=(10, 8))  
    pos = nx.spring_layout(graph, k=0.3)  

    nx.draw_networkx_nodes(graph, pos, node_size=500, node_color="lightblue")

    nx.draw_networkx_edges(graph, pos)

    nx.draw_networkx_labels(graph, pos, font_size=10, font_weight="bold")

    if shortest_path:
        path_edges = [(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)]
        nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color="red", width=2.0)

    plt.axis("off")  
    plt.show()


datos = [
    ['Medellín', 24, 1495, 'Turismo urbano, visitas a museos y parques, recorridos gastronómicos, entre otros.', 0, 33,
     83, 18, 13],
    ['Guatapé', 24, 2135,
     'Visitar la Piedra del Peñol, paseos en bote por el embalse, disfrutar de la gastronomía local, entre otros.', 79,
     43, 144, 71, 53],
    ['Santa Fe de Antioquia', 24, 537,
     'Turismo histórico, visitas a museos y sitios arqueológicos, paseos en bote por el río Cauca, entre otros.', 63, 92,
     0, 67, 23],
    ['Rionegro', 24, 2125, 'Turismo religioso, visitas a sitios históricos, recorridos gastronómicos, entre otros.', 28,
     0, 92, 50, 23],
    ['Barbosa', 24, 1525, 'Turismo de naturaleza, visitas a sitios históricos, recorridos gastronómicos, entre otros.',
     18, 50, 67, 0, 30],
    ['Itagüí', 24, 1556, 'Turismo urbano, visitas a centros comerciales y sitios culturales, entre otros.', 9, 38, 97, 22,
     17],
    ['Envigado', 24, 1670, 'Turismo urbano, visitas a parques y sitios culturales, entre otros.', 10, 43, 93, 26, 19],
    ['Cocorná', 24, 640, 'Turismo de naturaleza, visitas a cascadas y sitios históricos, entre otros.', 65, 25, 133, 80,
     67],
    ['El Peñol', 24, 2150,
     'Turismo de naturaleza, visita al Peñol de Guatapé, paseos en bote por la represa, entre otros.', 79, 42, 149,
     104, 58],
    ['Sonsón', 24, 1525, 'Turismo de naturaleza, visitas a sitios históricos y culturales, entre otros.', 86, 57, 130,
     112, 41]
]

graph = nx.Graph()

for dato in datos:
    municipio = dato[0]
    graph.add_node(municipio)

for i, dato in enumerate(datos):
    municipio = dato[0]
    distancias = dato[4:]
    for j, distancia in enumerate(distancias):
        if distancia != 0:
            otro_municipio = datos[j][0]
            graph.add_edge(municipio, otro_municipio, weight=distancia)

lugar_gustado = input("Ingrese el lugar que le haya gustado: ")

if lugar_gustado not in graph:
    print("El lugar ingresado no existe en los datos proporcionados.")
else:
    shortest_paths = dijkstra(graph, lugar_gustado)

    destinos_recomendados = sorted(shortest_paths.items(), key=lambda x: x[1])

    print(f"Recomendaciones de destinos a partir de {lugar_gustado}:")
    for destino, distancia in destinos_recomendados:
        if destino != lugar_gustado:
            print(f"- {destino} (Distancia: {distancia} km)")

    destino_cercano = destinos_recomendados[1][0]

    shortest_path = nx.shortest_path(graph, lugar_gustado, destino_cercano)

    print(f"\nCamino más corto desde {lugar_gustado} hasta {destino_cercano}:")
    for i, lugar in enumerate(shortest_path):
        print(f"{i + 1}. {lugar}")

    plot_graph(graph, shortest_path)

    print(f"\nLugares recomendados basados en la similitud de información:")
    for i, (destino, distancia) in enumerate(destinos_recomendados):
        if destino != lugar_gustado:
            datos_destino = next((dato for dato in datos if dato[0] == destino), None)
            temperatura = datos_destino[1]
            altura = datos_destino[2]
            actividades = datos_destino[3]
            print(f"{i+1}. {destino} (Distancia: {distancia} km)")
            print(f"   - Temperatura: {temperatura} °C")
            print(f"   - Altura sobre el nivel del mar: {altura} metros")
            print(f"   - Actividades: {actividades}")
            print()