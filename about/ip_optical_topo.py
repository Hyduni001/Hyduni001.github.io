import networkx as nx
import matplotlib.pyplot as plt

# 创建一个空图
G = nx.MultiGraph()

# 创建4个节点
G.add_node(1, layer='Physical')
G.add_node(2, layer='Physical')
G.add_node(3, layer='Physical')
G.add_node(4, layer='Physical')

# 创建光层边
G.add_edge(1, 2, layer='Optical', weight=1)
G.add_edge(2, 3, layer='Optical', weight=2)
G.add_edge(3, 4, layer='Optical', weight=3)

# 创建IP层边
G.add_edge(1, 4, layer='IP', weight=4)

# 绘制图形
pos = nx.spring_layout(G)

# 绘制光层图形
optical_edges = [(u, v) for (u, v, d) in G.edges(data=True) if d['layer']=='Optical']
nx.draw_networkx_edges(G, pos, edgelist=optical_edges, edge_color='r', alpha=0.5)

# 绘制IP层图形
ip_edges = [(u, v) for (u, v, d) in G.edges(data=True) if d['layer']=='IP']
nx.draw_networkx_edges(G, pos, edgelist=ip_edges, edge_color='b', alpha=0.5)

# 绘制节点
nx.draw_networkx_nodes(G, pos)
plt.show()