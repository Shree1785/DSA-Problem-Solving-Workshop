# n = int(input())
# k = int(input())

# prices = list(map(int, input().split()))

# prices.sort()

# total = 0
# count = 0

# for price in prices:
#     if total + price <= k:
#         total += price
#         count += 1
#     else:
#         break

# print(count)






# class Node:             #creating node
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# class BinaryTree:
#     def __init__(self):
#         self.root = None

#     def insert(self, value):
#         if self.root == None:
#             self.root = Node(value)

#     def insertNode(self, rootNode, value):
#         if value < rootNode.value:
#             if rootNode.left is None:
#                 rootNode.left = Node(value) 
#             else:
#                 self.insertNode(rootNode.left, value)         #recursive call
#         else:
#             if rootNode.right is None:
#                 rootNode.right = Node(value)
#             else:
#                 self.insertNode(rootNode.right, value) 

#     def search(self,value):
#         return self.searchNode(self.root, value)

#     def searchNode(self, rootNode, value):
#         if rootNode is None:
#             return False
#         if rootNode == value:
#             return True
#         elif value < rootNode.value:
#             return self.searchNode(rootNode.left, value )
#         else:
#             return self.searchNode(rootNode.right, value )        


#     def deleteTree(self):
#         #delete entire tree
#         self.root = None
                    

    

        
# # btObj = BinaryTree()
# # btObj.insert(50)
# # btObj.insert(30)
# # btObj.insert(70)
# # print(btObj)


# btObj = BinaryTree()
# btObj.insert(50)
# btObj.insertNode(btObj.root, 30)
# btObj.insertNode(btObj.root, 70)

# # print values
# print(btObj.root.value)
# print(btObj.root.left.value)
# print(btObj.root.right.value)






# class BSTNode:
#     def __init__(self, data):
#         self.data = data
#         self.leftChild = None
#         self.rightChild = None


# # INSERT
# def insertNode(rootNode, nodeValue):
#     if rootNode.data is None:
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


# # SEARCH
# def searchNode(rootNode, value):
#     if rootNode is None:
#         return False

#     if rootNode.data == value:
#         return True

#     elif value < rootNode.data:
#         return searchNode(rootNode.leftChild, value)

#     else:
#         return searchNode(rootNode.rightChild, value)


# # FIND MIN
# def minValueNode(rootNode):
#     current = rootNode
#     while current.leftChild is not None:
#         current = current.leftChild
#     return current


# # DELETE
# def deleteNode(rootNode, value):
#     if rootNode is None:
#         return rootNode

#     if value < rootNode.data:
#         rootNode.leftChild = deleteNode(rootNode.leftChild, value)

#     elif value > rootNode.data:
#         rootNode.rightChild = deleteNode(rootNode.rightChild, value)

#     else:
#         if rootNode.leftChild is None and rootNode.rightChild is None:
#             return None

#         elif rootNode.leftChild is None:
#             return rootNode.rightChild
#         elif rootNode.rightChild is None:
#             return rootNode.leftChild

#         temp = minValueNode(rootNode.rightChild)
#         rootNode.data = temp.data
#         rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)

#     return rootNode


# # INORDER
# def inorderTraversal(rootNode):
#     if rootNode:
#         inorderTraversal(rootNode.leftChild)
#         print(rootNode.data, end=" ")
#         inorderTraversal(rootNode.rightChild)


# # PREORDER
# def preorderTraversal(rootNode):
#     if rootNode:
#         print(rootNode.data, end=" ")
#         preorderTraversal(rootNode.leftChild)
#         preorderTraversal(rootNode.rightChild)


# # POSTORDER
# def postorderTraversal(rootNode):
#     if rootNode:
#         postorderTraversal(rootNode.leftChild)
#         postorderTraversal(rootNode.rightChild)
#         print(rootNode.data, end=" ")


# # LEVEL ORDER (NEW)
# def levelOrderTraversal(rootNode):
#     if rootNode is None:
#         return

#     from collections import deque
#     queue = deque([rootNode])

#     while queue:
#         node = queue.popleft()
#         print(node.data, end=" ")

#         if node.leftChild:
#             queue.append(node.leftChild)

#         if node.rightChild:
#             queue.append(node.rightChild)


# # ---------------- MAIN ----------------

# newBST = BSTNode(None)

# insertNode(newBST, 50)
# insertNode(newBST, 30)
# insertNode(newBST, 70)
# insertNode(newBST, 20)
# insertNode(newBST, 40)
# insertNode(newBST, 60)
# insertNode(newBST, 80)

# print("Inorder:")
# inorderTraversal(newBST)

# print("\nPreorder:")
# preorderTraversal(newBST)

# print("\nPostorder:")
# postorderTraversal(newBST)

# print("\nLevel Order:")
# levelOrderTraversal(newBST)

# # SEARCH
# value = int(input("\nEnter value to search: "))
# print("Value found" if searchNode(newBST, value) else "Value NOT found")

# # DELETE
# delValue = int(input("Enter value to delete: "))
# newBST = deleteNode(newBST, delValue)

# print("\nAfter Deletion (Level Order):")
# levelOrderTraversal(newBST)





##Check for Prime Numbers in a Range


#Question: Write a function to find and return all prime numbers within a given range.
#Logic: Define a function that iterates through the range and checks for prime numbers.
#Sample Input: Range: 1 to 20
#Expected Output: List of Prime Numbers: [2, 3, 5, 7, 11, 13, 17, 19]


# def find_primes(start, end):
#     primes = []
    
#     for num in range(start, end + 1):
#         if num > 1:
#             is_prime = True
#             for i in range(2, int(num ** 0.5) + 1):
#                 if num % i == 0:
#                     is_prime = False
#                     break
#             if is_prime:
#                 primes.append(num)
    
#     return primes

# start = 1
# end = 20

# print("List of Prime Numbers:", find_primes(start, end))




##Calculate Compound Interest


#Question: Write a function to calculate the compound interest for a principal amount, rate, and time.
#Logic: Define a function that uses a loop to calculate compound interest based on the formula.
#Sample Input: Principal amount = 1000
#                          Rate = 5%
#                          Time = 3 years
#Expected Output: 157.63


# def compound_interest(principal, rate, time):
#     amount = principal
    
#     for i in range(time):
#         amount = amount * (1 + rate / 100)
    
#     ci = amount - principal
#     return round(ci, 2)

# principal = 1000
# rate = 5
# time = 3

# print("Compound Interest:", compound_interest(principal, rate, time))
