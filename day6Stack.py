
##2.Stack implementation with size limit


#operation== push,pop,isempty, isfull, delete

#stack with size 


#operation== push,pop,isempty, isfull, delete


# import sys
# class Stack:
#     def __init__(self, stacksize):   #parameterize constructor
#         self.stackList = []
#         self.stacksize = stacksize

#     def isFull(self):
#         if len(self.stackList) == self.stacksize:
#             return True
#         else:
#             return False    

#     def push(self,value):
#         if self.isFull():
#             print("stack is full")
#         else:
#             self.stackList.append(value)
               


    
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


# size = int(input("enter the size of stack "))
# stackobj=Stack(size)  #stack obj has created            

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