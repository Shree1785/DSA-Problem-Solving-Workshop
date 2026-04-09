# import sys
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class Linkedlist:
#     def __init__(self):
#         self.head = None
#         self.tail = None


#     def AddNode(self, value):
#         node = Node(value)
#         if self.head is None:
#             self.head = node
#             self.tail = node
#         else:
#             self.tail.next = node
#             self. tail = node


#     def display(self):
        
#         current = self.head  #temp pointing
#         if current is None:
#             print("Linked list is empty")
#             return
#         while current:
            
#             print("|", current.data, "|", end=" -> ")
#             current = current.next
        
#         print("None")
                
#     def AddAtbeginning(self, value) :
#         node = Node(value)
#         if self.head is None:
#             self.head = node
#             self.tail = node
#         else:
#             node.next = self.head
#             self.head = node   


#     def AddInBetween(Self, value):
#         node = Node(value)









#     def AddAtEnd(self, value):
#         node = Node(value)
#         if self.head is None:
#             self.head = node
#             self.tail = node

#         else:
#             self.tail.next = node
#             self.tail = node    



# if __name__ == "__main__":
#     object = Linkedlist()

#     while True:
#         print("1.Add node in linked list: ")
#         print("2.Add node at beginning: ")
#         print("3.Add node in between: ")
#         print("4.Add node at end: ")
#         print("5.Display linked list: ")
#         print("6.Exit: ")

#         choice = int(input("enter your choice: "))

#         if choice == 1:
#             value = int(input("enter value here: "))
#             object.AddNode(value)
        

#         elif choice == 2:
#             value = int(input("enter value here: "))
#             object.AddAtbeginning(value)

#         elif choice == 3:
#             value = int(input("enter value here: "))
#             object.AddInBetween(value)

#         elif choice == 4:
#             value = int(input("enter value here"))
#             object.AddAtEnd(value)   

#         elif choice == 5:
#             object.display()

#         else:
#             sys.exit()



