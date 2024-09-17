import networkx as nx
from matplotlib import pyplot as plt

G = nx.grid_2d_graph(5, 5)
plt.figure(figsize=(6,6))
pos = {(x,y):(y,-x) for x,y in G.nodes()}
nx.draw(G, pos=pos, 
        node_color='lightgreen', 
        with_labels=True,
        node_size=600)

plt.show()
