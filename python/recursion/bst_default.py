class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def print_recursive(root):
    if root is None:
        return

    print_recursive(root.left)
    print(root.val)
    print_recursive(root.right)


def print_iterative(root):
    stack = []  # Initialize an empty stack
    current = root  # Start with the root node

    while current is not None or stack:
        # Reach the leftmost node of the current node
        while current is not None:
            stack.append(current)  # Add current node to the stack
            current = current.left  # Move to the left child

        # Current must be None at this point, so we pop from the stack
        current = stack.pop()
        print(current.val)  # Print the value of the node

        # We have visited the node and now move to its right subtree
        current = current.right


# Приклад використання:
#        50
#       /  \
#     30    70
#    /  \   /  \
#   20  40 60  80

#Правила бінарного дерева пошуку (BST):
#Кожен вузол має не більше двох нащадків — лівий і правий.
#Значення у лівому піддереві кожного вузла менше, ніж значення у самому вузлі.
#Значення у правому піддереві кожного вузла більше, ніж значення у самому вузлі.
#Немає дублювання значень: кожне значення в дереві є унікальним.

root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

print_recursive(root)
print("---------------------------")
print_iterative(root)