import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Створення графа (використовуємо той самий граф з Завдання 1)
G = nx.Graph()

stations = ['Station A', 'Station B', 'Station C', 'Station D', 'Station E', 'Station F']
G.add_nodes_from(stations)

routes = [('Station A', 'Station B'), ('Station A', 'Station C'),
          ('Station B', 'Station D'), ('Station C', 'Station D'),
          ('Station D', 'Station E'), ('Station E', 'Station F'),
          ('Station B', 'Station E')]
G.add_edges_from(routes)

# Реалізація DFS
def dfs(graph, start, goal, path=None):
    if path is None:
        path = []
    path.append(start)
    
    if start == goal:
        return path
    
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            result = dfs(graph, neighbor, goal, path.copy())
            if result:
                return result
    return None

# Реалізація BFS
def bfs(graph, start, goal):
    queue = deque([[start]])
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node == goal:
            return path
        
        for neighbor in graph.neighbors(node):
            if neighbor not in path:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None

# Порівняння результатів DFS і BFS
start_node = 'Station A'
goal_node = 'Station F'

dfs_path = dfs(G, start_node, goal_node)
bfs_path = bfs(G, start_node, goal_node)

print(f"Шлях за допомогою DFS: {dfs_path}")
print(f"Шлях за допомогою BFS: {bfs_path}")

# Візуалізація графа
plt.figure(figsize=(8, 6))
pos = {
    'Station A': (0, 0),
    'Station B': (1, 1),
    'Station C': (1, -1),
    'Station D': (2, 0),
    'Station E': (3, 1),
    'Station F': (4, 0)
}

nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold')
plt.title('Transport Network Graph for DFS and BFS')
plt.show()

# Висновок:
# Алгоритм DFS шукає шлях, заглиблюючись у граф, що може призводити до довших шляхів,
# але він знайде один із можливих шляхів, який не обов'язково є найкоротшим.
# Алгоритм BFS, навпаки, досліджує граф рівнями, що гарантує знаходження найкоротшого шляху
# (за кількістю ребер) у незважених графах. Тому BFS у цьому випадку знаходить коротший шлях.
