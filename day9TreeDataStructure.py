


# class Tree:
#     def __init__(self, data):
#         self.data = data #instance variable (create separate memory for each object)
#         self.children = []


#     def addChild(self, child):
#         self.children.append(child)
        
    
#     def __str__(self, level=0):
#         ret = " " * level + str(self.data) + "\n"
#         for child in self.children:
#             ret += child.__str__(level+1)  # recursion
#         return ret


# #object creation
# rootNode = Tree("Drinks")
# hot = Tree("Hot")
# cold = Tree("Cold")
# tea = Tree("Tea")
# coffee = Tree("Coffee")
# nonAlcoholic = Tree("NonAlcoholic")
# alcoholic = Tree("Alcoholic")


# #add child nodes in tree
# rootNode.addChild(hot)
# rootNode.addChild(cold)
# hot.addChild(tea)
# hot.addChild(coffee)
# cold.addChild(nonAlcoholic)
# cold.addChild(alcoholic)


# print(rootNode)



##Binary Tree

#1. Full Binary Tree

# -Each node has either 0 or 2 children
# -No node has a single child


#2. Complete Binary Tree

# -All levels except possibly the last are completely filled
# -Nodes in the last level are filled from left to right


#3. Perfect Binary Tree

# -All internal nodes have exactly two nodes
# -All leaf nodes are at the same level


#4. Balanced Binary Tree

# -
# -


# Creation of Tree
# Insertion of a node
# Deletion of a node
# Search for a value
# Traverse all nodes
# Deletion of tree



# Creation of Tree


# class Tree:
#     def __init__(self, data):
#         self.data = data
#         self.children = []

#     def addChild(self, child):
#         self.children.append(child)

#     def __str__(self, level=0):
#         ret = " " * level + str(self.data) + "\n"
#         for child in self.children:
#             ret += child.__str__(level+1)
#         return ret


# # object creation
# n1 = Tree("n1")
# n2 = Tree("n2")
# n3 = Tree("n3")
# n4 = Tree("n4")
# n5 = Tree("n5")
# n6 = Tree("n6")
# n7 = Tree("n7")
# n8 = Tree("n8")
# n9 = Tree("n9")

# # building tree structure
# n1.addChild(n2)
# n1.addChild(n3)

# n2.addChild(n4)
# n2.addChild(n5)

# n3.addChild(n6)
# n3.addChild(n7)

# n4.addChild(n8)
# n4.addChild(n9)

# # print tree
# print(n1)




# class BSTNode:
#     def __init__(self, data):
#         self.data = data
#         self.leftChild = None
#         self.rightChild = None


# def insertNode(rootNode, nodeValue):
#     if rootNode.data == None:
#         rootNode.data = nodeValue

#     elif nodeValue <= rootNode.data:
#         if rootNode.leftChild is None:
#             rootNode.leftChild = BSTNode(nodeValue)
#         else:
#             insertNode(rootNode.leftChild, nodeValue)

#     else:
#         if rootNode.rightChild is None:
#             rootNode.rightChild = BSTNode(nodeValue)
#         else:
#             insertNode(rootNode.rightChild, nodeValue)

#     return "The node has been successfully inserted"


# # Level Order Traversal
# def levelOrderTraversal(rootNode):
#     if not rootNode:
#         return
#     queue = []
#     queue.append(rootNode)

#     while queue:
#         root = queue.pop(0)
#         print(root.data)

#         if root.leftChild is not None:
#             queue.append(root.leftChild)

#         if root.rightChild is not None:
#             queue.append(root.rightChild)


# # Delete whole BST
# def deleteBST(rootNode):
#     rootNode.data = None
#     rootNode.leftChild = None
#     rootNode.rightChild = None
#     return "The BST has been successfully deleted"


# # Creating BST
# newBST = BSTNode(None)
# insertNode(newBST, 70)
# insertNode(newBST, 50)
# insertNode(newBST, 90)
# insertNode(newBST, 30)
# insertNode(newBST, 60)
# insertNode(newBST, 80)
# insertNode(newBST, 100)
# insertNode(newBST, 20)
# insertNode(newBST, 40)

# print(deleteBST(newBST))
# levelOrderTraversal(newBST)




# class Node:
#     # create a node in the tree
#     def __init__(self, value):
#         self.value = value  # value
#         self.left = None
#         self.right = None


# class BinaryTree:
#     def __init__(self):
#         self.root = None

#     def insert(self, value):
#         # insert root node in if block if there is no root node
#         if self.root is None:
#             self.root = Node(value)
#         else:
#             self._insert(self.root, value)

#     def _insert(self, current, value):
#         if value < current.value:
#             if current.left is None:
#                 current.left = Node(value)
#             else:
#                 self._insert(current.left, value)
#         else:
#             if current.right is None:
#                 current.right = Node(value)
#             else:
#                 self._insert(current.right, value)

#     # inorder traversal
#     def inorder(self, node):
#         if node:
#             self.inorder(node.left)
#             print(node.value, end=" ")
#             self.inorder(node.right)

#     # preorder traversal
#     def preorder(self, node):
#         if node:
#             print(node.value, end=" ")
#             self.preorder(node.left)
#             self.preorder(node.right)

#     # postorder traversal
#     def postorder(self, node):
#         if node:
#             self.postorder(node.left)
#             self.postorder(node.right)
#             print(node.value, end=" ")


# # creating tree
# bt = BinaryTree()

# bt.insert(50)
# bt.insert(30)
# bt.insert(70)
# bt.insert(20)
# bt.insert(40)
# bt.insert(60)
# bt.insert(80)

# print("Inorder Traversal:")
# bt.inorder(bt.root)

# print("\nPreorder Traversal:")
# bt.preorder(bt.root)

# print("\nPostorder Traversal:")
# bt.postorder(bt.root) 