# Python Tutorial: Tree Data Structures

## Introduction to Trees
"""
A tree data structure simulates a hierarchical tree structure with a set of connected nodes.

Each node contains a value and references to its child nodes. 

Node: The fundamental unit of a tree.
Root: The top node of the tree.
Parent: A node that has child nodes.
Child: A node derived from another node (parent).
Leaf: A node with no children.
Edge: The connection between two nodes.
Height: The number of edges on the longest path from the root to a leaf.
Depth: The number of edges from the root to a specific node.
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []  # List to hold child nodes

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return str(self.value)

root = TreeNode("Root")
child1 = TreeNode("Child 1")
child2 = TreeNode("Child 2")
root.add_child(child1)
root.add_child(child2)

# Add grandchildren
child1.add_child(TreeNode("Grandchild 1.1"))
child1.add_child(TreeNode("Grandchild 1.2"))
child2.add_child(TreeNode("Grandchild 2.1"))

# Display the tree structure
print(f"Root: {root}")
print(f"Children of root: {root.children}")


def preorder_traversal(node):
    if node:
        print(node.value)
        for child in node.children:
            preorder_traversal(child)  #recursion
preorder_traversal(root)

def postorder_traversal(node):
    if node:
        for child in node.children:
            postorder_traversal(child) # recursion
        print(node.value)

postorder_traversal(root)

#### Breadth-First Search (BFS)

from collections import deque

def breadth_first_traversal(root):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value)
        queue.extend(node.children)

print("Breadth-First Traversal:")
breadth_first_traversal(root)

### Implementing a Binary Tree Node
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None  # Left child
        self.right = None  # Right child

    def __repr__(self):
        return str(self.value)

### Binary Tree Traversals
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value)
        inorder_traversal(node.right)

# Example Binary Tree
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)

print("Inorder Traversal:")
inorder_traversal(root)

# Applications of Binary Trees: Binary Search Trees, Heaps, Syntax Trees

# AVL Trees


# Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

# Example
trie = Trie()
trie.insert("hello")
trie.insert("world")
print(trie.search("hello"))  # Output: True
print(trie.search("hell"))   # Output: False
