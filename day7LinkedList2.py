# linked list data structure

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None


# class Linkedlist:
#     def __init__(self):
#         self.head = None


# linkobj = Linkedlist()


# # Step 1 : Add Node in Beginning
# def add_begin(value):
#     newnode = Node(value)
#     newnode.next = linkobj.head
#     linkobj.head = newnode


# # Step 2 : Add Node in Between
# def add_between(prev_value, value):
#     temp = linkobj.head

#     while temp != None:
#         if temp.data == prev_value:
#             newnode = Node(value)
#             newnode.next = temp.next
#             temp.next = newnode
#             return
#         temp = temp.next

#     print("Previous value not found")


# # Step 3 : Add Node in End
# def add_end(value):
#     newnode = Node(value)

#     if linkobj.head == None:
#         linkobj.head = newnode
#         return

#     temp = linkobj.head
#     while temp.next != None:
#         temp = temp.next

#     temp.next = newnode


# # Step 4 : Delete Node
# def delete_node(value):
#     temp = linkobj.head

#     if temp != None and temp.data == value:
#         linkobj.head = temp.next
#         return

#     prev = None
#     while temp != None and temp.data != value:
#         prev = temp
#         temp = temp.next

#     if temp == None:
#         print("Value not found")
#         return

#     prev.next = temp.next



# def display():
#     temp = linkobj.head

#     if temp == None:
#         print("List is empty")
#         return

#     while temp != None:
#         print("|", temp.data, "| -> ", end="")
#         temp = temp.next

#     print("None")



# while True:

#     print("\n--- Linked List Menu ---")
#     print("1 Add Node in Beginning")
#     print("2 Add Node in Between")
#     print("3 Add Node in End")
#     print("4 Delete Node")
#     print("5 Display")
#     print("6 Exit")

#     choice = int(input("Enter choice: "))

#     if choice == 1:
#         val = int(input("Enter value: "))
#         add_begin(val)

#     elif choice == 2:
#         prev = int(input("Enter previous value: "))
#         val = int(input("Enter new value: "))
#         add_between(prev,val)

#     elif choice == 3:
#         val = int(input("Enter value: "))
#         add_end(val)

#     elif choice == 4:
#         val = int(input("Enter value to delete: "))
#         delete_node(val)

#     elif choice == 5:
#         display()

#     elif choice == 6:
#         print("Program Ended")
#         break

#     else:
#         print("Invalid Choice")