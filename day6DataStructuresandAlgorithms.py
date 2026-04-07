
##Data Structures and Algoritms


##1.Stack implementation without size limit
##2.Stack implementation with size limit

# 1.Push
# 2.property
# 3.isEmpty()
# 4.isFull
# 5.Delete Stack
# 6.Display 
# 7.Exit

#stack with size 
#stack without size

#operation== push,pop,isempty, isfull, delete

#stack with size 
#stack without size

#operation== push,pop,isempty, isfull, delete
#stack with size 
#stack without size

#operation== push,pop,isempty, isfull, delete



#stack with size 
#stack without size

#operation== push,pop,isempty, isfull, delete
# import sys
# class Stack:
#     def __init__(self):
#         self.stackList = []

#     def push(self,value):
#         self.stackList.append(value)

#     def displayStack(self):
#         print("-----------------")
#         print(self.stackList) 
#         print("-----------------")
    
#     def isEmpty(self):
#         if self.stackList==[]:
#             return  True
#         else:
#             return False
        
#     def pop(self):
#         if self.isEmpty():
#             return "stack is empty"
#         else:
#             return self.stackList.pop()

#     def deleteStack(self):
#         self.stackList = None 
#         return "stack is delete"
    
#     def peek(self):
#         if self.isEmpty():
#             return "stack is empty"
#         else:
#             return self.stackList[-1]



# stackobj=Stack()             

# while True:
#     print("1. Push element in the stack: ")
#     print("2. display stack element ")
#     print("3. check isEmpty ")
#     print("4. Pop operation")
#     print("5. Delete stack")
#     print("6. peek operation")
#     print("7. exit")

#     choice = int(input("enter your choice: "))
#     if choice == 1:
#         val =int(input("enter the value for stack: "))
#         stackobj.push(val)
#     elif choice == 2:
#         stackobj.displayStack()   
#     elif choice == 3:
#         print(stackobj.isEmpty()) 
#     elif choice == 4:
#         print(stackobj.pop()) 
#     elif choice ==5:
#         print(stackobj.deleteStack())  
#     elif choice==6:
#         print(stackobj.peek())    
#     elif choice == 7:
#         sys.exit()