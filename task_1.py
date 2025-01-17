import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Створення графа транспортної мережі Дубая
G = nx.Graph()

# Додавання вершин (районів або станцій)
nodes = ["Downtown", "Deira", "Marina", "Bur Dubai", "Al Barsha", "JLT", "Palm Jumeirah", "Dubai Creek"]
G.add_nodes_from(nodes)

# Додавання ребер (доріг або метро) з вагами (відстань у км)
edges = [
    ("Downtown", "Deira", 8),
    ("Downtown", "Marina", 15),
    ("Downtown", "Bur Dubai", 5),
    ("Deira", "Dubai Creek", 3),
    ("Bur Dubai", "Dubai Creek", 4),
    ("Bur Dubai", "Al Barsha", 10),
    ("Al Barsha", "JLT", 6),
    ("JLT", "Marina", 2),
    ("Marina", "Palm Jumeirah", 7),
]
G.add_weighted_edges_from(edges)

# Візуалізація графа
pos = nx.spring_layout(G, seed=42)  # Фіксоване розташування вершин
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=3000, font_size=10)
edge_labels = {(u, v): d for u, v, d in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Транспортна мережа Дубая")
plt.show()

# Аналіз характеристик графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_centrality = dict(G.degree())

# Формування таблиці з характеристиками графа
df = pd.DataFrame({
    "Вершина": list(degree_centrality.keys()),
    "Ступінь вершини": list(degree_centrality.values())
})

# Вивід у консоль
print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь вершин:")
print(df.to_string(index=False))
