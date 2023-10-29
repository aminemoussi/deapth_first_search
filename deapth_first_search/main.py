import networkx as nx
import matplotlib.pyplot as plt
import time
from collections import deque

def dfs_with_stack(g, root, marked):

    stack = deque()
    visited_preorder = set()
    visited_postorder = set()
    stack.append(root)

    while len(stack) > 0:
        v = stack.pop()
        if not marked[v]:
            visited_preorder.add(v)
            marked[v] = True
            for i in g.neighbors(v):
                if not marked[i]:
                    stack.append(i)
                visited_postorder.add(v)

    print("All the elements reachable from the node \"",root,"\" of your tree are: \n")
    print("Preorder nodes: ", visited_preorder)
    print("Postorder nodes: ", visited_postorder)




g = nx.Graph()

g.add_nodes_from([0, 1, 2, 3, 4])
g.add_edges_from([
    (0, 1),
    (0, 2),
    (0, 3),
    (2, 3),
    (1, 3),
    (3, 4)
])

pos = nx.spring_layout(g)
nx.draw(g, pos, with_labels=True, node_size = 2000, node_color = "skyblue", font_size = 20, font_weight = "bold")
plt.title("Graph visualization.")
plt.show()

print("Applying deapth first search to go through all the nodes starting from node 0.")
time.sleep(2)


marked = [False] * g.size()

dfs_with_stack(g, 0, marked)