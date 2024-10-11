class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def search_recursive(root, key):
    # Базовий випадок: якщо дерево порожнє або ключ знаходиться в корені
    if root is None or root.val == key:
        return root

    # Якщо шукане значення менше, ніж значення в корені, йдемо в ліве піддерево
    if key < root.val:
        return search_recursive(root.left, key)

    # Якщо шукане значення більше, йдемо в праве піддерево
    return search_recursive(root.right, key)


def search_iterative(root, key):
    # Поки не досягнемо кінця дерева або не знайдемо шукане значення
    while root is not None and root.val != key:
        if key < root.val:
            root = root.left  # Йдемо в ліве піддерево, якщо ключ менший
        else:
            root = root.right  # Йдемо в праве піддерево, якщо ключ більший

    return root  # Повертаємо вузол, де знайшли ключ, або None


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

result = search_recursive(root, 40)
if result:
    print(f"Значення знайдено: {result.val}")
else:
    print("Значення не знайдено")