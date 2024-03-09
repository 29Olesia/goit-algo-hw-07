import networkx as nx
import matplotlib.pyplot as plt

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

def visualize_avl_tree(root):
    G = nx.Graph()

    def add_edges(node, parent=None):
        if node:
            G.add_node(node.key)
            if parent:
                G.add_edge(parent.key, node.key)
            add_edges(node.left, node)
            add_edges(node.right, node)

    add_edges(root)

    pos = nx.spring_layout(G)
    labels = {node: str(node) for node in G.nodes()}

    nx.draw(G, pos, with_labels=True, labels=labels, node_size=700, node_color="skyblue", font_size=8, font_color="black", font_weight="bold", font_family="sans-serif")
    plt.show()

def get_height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def left_rotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

def right_rotate(y):
    x = y.left
    T3 = x.right

    x.right = y
    y.left = T3

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x

def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def insert(root, key):
    if not root:
        return AVLNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1:
        if key < root.left.key:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if key > root.right.key:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root

def find_sum_values(node):
    if not node:
        return 0
    return node.key + find_sum_values(node.left) + find_sum_values(node.right)

root = None
keys = [10, 20, 30, 25, 28, 27, -1]

for key in keys:
    root = insert(root, key)
    print("Вставлено:", key)
    print("AVL-Дерево:")
    visualize_avl_tree(root)

sum_all_values = find_sum_values(root)
print("Сума всіх значень у AVL-дереві:", sum_all_values)
