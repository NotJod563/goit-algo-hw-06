import networkx as nx
import matplotlib.pyplot as plt

# Створюємо граф із вагою для ребер
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

# Використовуємо алгоритм Дейкстри для знаходження найкоротших шляхів
shortest_paths = dict(nx.all_pairs_dijkstra_path(G))
shortest_distances = dict(nx.all_pairs_dijkstra_path_length(G))

# Візуалізація графу з вагами ребер
pos = nx.spring_layout(G)  # Автоматичне розташування графа
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold")
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()

# Виведення результатів алгоритму Дейкстри
for source in shortest_paths:
    print(f"Найкоротші шляхи від {source}:")
    for target in shortest_paths[source]:
        print(f" - до {target}: шлях {shortest_paths[source][target]}, довжина {shortest_distances[source][target]}")
    print("\n")
