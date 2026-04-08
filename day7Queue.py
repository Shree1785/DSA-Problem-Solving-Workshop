# import sys

# class Queue:
#     def __init__(self, queuesize):   # parameterized constructor
#         self.queueList = []
#         self.queuesize = queuesize

#     def isFull(self):
#         return len(self.queueList) == self.queuesize

#     def Enqueue(self, value):
#         if self.queueList is None:
#             print("Queue is deleted. Create a new queue first.")
#         elif self.isFull():
#             print("Queue is Full")
#         else:
#             self.queueList.append(value)   # append method

#     def displayQueue(self):
#         print("-----------------")
#         print(self.queueList)
#         print("-----------------")

#     def isEmpty(self):
#         if self.queueList is None or self.queueList == []:
#             return True
#         else:
#             return False

#     def Dequeue(self):
#         if self.isEmpty():
#             return "Queue is Empty"
#         else:
#             return self.queueList.pop(0)

#     def deleteQueue(self):
#         self.queueList = None
#         return "Queue Deleted"

#     def peek(self):
#         if self.isEmpty():
#             return "Queue is Empty"
#         else:
#             return self.queueList[0]


# size = int(input("Enter the size of Queue: "))
# queueobj = Queue(size)

# while True:
#     print("\n1. Enqueue element in Queue")
#     print("2. Display Queue Elements")
#     print("3. Check Queue isEmpty")
#     print("4. Dequeue operation")
#     print("5. Delete Queue")
#     print("6. Peek operation")
#     print("7. Exit")

#     try:
#         choice = int(input("Enter your choice: "))
#     except ValueError:
#         print("Invalid input. Enter a number.")
#         continue

#     if choice == 1:
#         val = int(input("Enter the value for queue: "))
#         queueobj.Enqueue(val)

#     elif choice == 2:
#         queueobj.displayQueue()

#     elif choice == 3:
#         print(queueobj.isEmpty())

#     elif choice == 4:
#         print(queueobj.Dequeue())

#     elif choice == 5:
#         print(queueobj.deleteQueue())

#         # Ask user to create new queue
#         while True:
#             ans = input("Do you want to create a new Queue? (y/n): ").lower()

#             if ans == 'y':
#                 size = int(input("Enter new queue size: "))
#                 queueobj = Queue(size)
#                 print("New Queue Created")
#                 break
#             elif ans == 'n':
#                 print("Queue operations stopped.")
#                 sys.exit()
#             else:
#                 print("Invalid input. Please enter y or n.")

#     elif choice == 6:
#         print(queueobj.peek())

#     elif choice == 7:
#         sys.exit()

#     else:
#         print("Invalid choice")