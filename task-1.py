import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання станцій (вершин)
stations = ['Station A', 'Station B', 'Station C', 'Station D', 'Station E', 'Station F']
G.add_nodes_from(stations)

# Додавання маршрутів (ребер)
routes = [('Station A', 'Station B'), ('Station A', 'Station C'), 
          ('Station B', 'Station D'), ('Station C', 'Station D'),
          ('Station D', 'Station E'), ('Station E', 'Station F'),
          ('Station B', 'Station E')]  # Додали ребро між 'Station B' і 'Station E' для перетину
G.add_edges_from(routes)

# Аналіз графа
num_nodes = G.number_of_nodes()  # Кількість вершин
num_edges = G.number_of_edges()  # Кількість ребер
degrees = dict(G.degree())  # Ступінь кожної вершини

# Виведення основних характеристик графа
print("Основні характеристики графа:")
print(f"Кількість станцій (вершин): {num_nodes}")
print(f"Кількість маршрутів (ребер): {num_edges}")
print("Ступінь кожної станції:")
for station, degree in degrees.items():
    print(f"{station}: {degree}")

# Візуалізація графа з перетинами
plt.figure(figsize=(8, 6))
# Встановлюємо розташування вершин вручну, щоб були перетини ребер
pos = {
    'Station A': (0, 0),
    'Station B': (1, 1),
    'Station C': (1, -1),
    'Station D': (2, 0),
    'Station E': (3, 1),
    'Station F': (4, 0)
}

nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold')
plt.title('Transport Network Graph with Edge Crossings')
plt.show()
