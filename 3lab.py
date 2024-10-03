import sys

message = "beep boop beer!"
print(f"Изначальное сообщение: {message}")


freq = {} # словарь для частот встречания
for char in message:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print(freq)

class Node: #класс для узлов
    def __init__(self, char, freq, left, right):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    def __str__(self):
        return f"Node(char='{self.char}', freq='{self.freq}', left={str(self.left)}, right='{str(self.right)}')"

tree = [] #массив для узлов
for char, freq_char in freq.items():
    tree.append(Node(char, freq_char, None, None))

for tree_part in tree:
    print(tree_part)

while len(tree) > 1:
  min1 = min(tree, key=lambda node: node.freq)
  tree.remove(min1) #нахождение двух минимальных и удаление их
  min2 = min(tree, key=lambda node: node.freq)
  tree.remove(min2)

  parent = Node(None, min1.freq + min2.freq, min1, min2) #новый узл

  tree.append(parent) #добавление нового узла

new_tree = tree[0] # Корень дерева
print(f"Новое дерево: {new_tree}")


codes = {} #словарь для кодов

def recursive(node, code):
    if node is None:
        return
    if node.char is not None:
        codes[node.char] = code
    recursive(node.left, code + "0")
    recursive(node.right, code + "1")

recursive(new_tree, "")

print(f"Коды символов: {codes}")


coded_message = ""
for char in message:
    coded_message += codes[char]
print(coded_message)

decoded_message = ""
current = new_tree
for i in coded_message:
    if i == "0":
      current = current.left
    else:
      current = current.right
    if current.char is not None:
      decoded_message += current.char
      current = new_tree

print(f"Раскодированное сообщение: {decoded_message}")
original_size = len(message) * sys.getsizeof(message[0])
print(f"Размер исходного сообщения: {original_size} бит")

# Размер закодированного сообщения
coded_size = len(coded_message)
print(f"Размер закодированного сообщения: {coded_size} бит")

# Сравнение
compression = original_size / coded_size
print(f"Степень сжатия: {compression: .2f}")
