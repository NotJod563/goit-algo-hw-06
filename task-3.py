import networkx as nx
import matplotlib.pyplot as plt

# Створення графа з вагами
G = nx.Graph()

# Додаємо вершини і ребра з вагою відповідно до вихідного графу
edges = [
    ('Station A', 'Station B', 4),
    ('Station A', 'Station C', 2),
    ('Station B', 'Station C', 1),
    ('Station B', 'Station D', 5),
    ('Station C', 'Station D', 8),
    ('Station B', 'Station E', 3),
    ('Station D', 'Station E', 2),
    ('Station E', 'Station F', 3),
]

G.add_weighted_edges_from(edges)

# Функція для візуалізації графа
def draw_graph_with_weights(G):
    pos = {
        'Station A': (0, 0),
        'Station B': (1, 1),
        'Station C': (1, -1),
        'Station D': (2, 0),
        'Station E': (3, 1),
        'Station F': (4, 0)
    }
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

# Реалізація алгоритму Дейкстри для знаходження найкоротшого шляху
def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph.nodes}
    distances[start] = 0
    unvisited = list(graph.nodes)

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        # Оновлення відстаней для сусідів
        for neighbor in graph.neighbors(current_vertex):
            weight = graph[current_vertex][neighbor]['weight']
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances

# Виклик функції для кожної вершини
start_node = 'Station A'
distances_from_start = dijkstra(G, start_node)

# Виведення результатів
print(f"Найкоротші відстані від вершини {start_node}:")
for node, distance in distances_from_start.items():
    print(f"{start_node} -> {node}: {distance}")

# Візуалізація графа з вагами
draw_graph_with_weights(G)
