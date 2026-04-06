
##Class

# class Student:
#     roll_no=101
    
#     def studentData(self):
#         print("Student information")
        
# obj = Student()
# print(obj.roll_no)
# obj.studentData()


##Constructor

# class Demo:
#     def __init__(self):
#         print("I am constructor")
        
#     def msg(self):
#         print("Hello Class !")

# obj1=Demo()

# class Demo:
#     def __init__(self):
#         print("I am constructor")
        
#     def msg(self):
#         print("Hello Class !")

# obj1=Demo()
# # print(obj1)
# obj2=Demo()
# obj1.msg()



# class Hod:
#     def __init__(self):
#         self.name='Bhagyashree'
#         self.age=21
#         self.empid=1001
#     def info(self):
#         print("my name is: ",self.name)
#         print("my age: ",self.age)
#         print("my emp id: ",self.empid)
# obj = Hod()
# obj.info()


# class Hod:
#     def __init__(self,name ,age, rollno):  
#         self.name=name
#         self.age=age
#         self.rollno =rollno

#     def show(self):
#         print("my name is: ",self.name)
#         print("my age: ",self.age)
#         print("my rollno: ",self.rollno)
# obj = Hod('arjun', 45,101)
# obj.show()



##Instance Variable

# class New:
#     def __init__(self):
#         self.a=10
        
# obj1=New()
# obj2=New()
# obj3=New()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
# obj1.a=20
# print()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

##Where we can declare the instance variable

##declaring instance variable outside a class by using object


# class Student:
#     def __init__(self): #constructor
#         self.s_name="Bhagyashree"
#         self.s_rollno=101 #declaring a instance var inside a constructor
        
#     def getdata(self):
#         self.s_mb =2828282828282 # declaring a instance var inside a instance method
        
# obj=Student()
# obj.getdata()
# del obj.s_mb #delete the instance variable using obj
# obj.s_branch="CE" # adding instance variable by using object
# print(obj.__dict__)      



##Static Variable

###static varaible-it is not dependent on object,it depends on class.
##delcared outside the class
##one static memory is dependent on one memory

# class New:
#     a = 10  #static var
#     def __init__(self):
#         self.name="Bhagyashree"   #instance var
# Obj1 = New()
# Obj2 = New()
# Obj3 = New()
# print(Obj1.a)
# print(Obj2.a)
# print(Obj3.a)
# New.a=50
# print(Obj1.a)
# print(Obj2.a)
# print(Obj3.a)


#CRUD Operations


# class Student:
#     def __init__(self, sid, roll, name, city):
#         self.sid = sid
#         self.roll = roll
#         self.name = name
#         self.city = city


# class CRUD:
#     def __init__(self):
#         self.students = []

#     # CREATE
#     def add_student(self):
#         sid = input("Enter Student ID: ")
#         roll = input("Enter Roll No: ")
#         name = input("Enter Name: ")
#         city = input("Enter City: ")

#         student = Student(sid, roll, name, city)
#         self.students.append(student)
#         print("✅ Student added successfully!")

#     # READ
#     def show_students(self):
#         if not self.students:
#             print("⚠ No student records found!")
#             return

#         print("\n----- Student List -----")
#         for s in self.students:
#             print(f"ID: {s.sid}, Roll No: {s.roll}, Name: {s.name}, City: {s.city}")

#     # UPDATE
#     def update_student(self):
#         sid = input("Enter Student ID to update: ")

#         for s in self.students:
#             if s.sid == sid:
#                 s.roll = input("Enter new Roll No: ")
#                 s.name = input("Enter new Name: ")
#                 s.city = input("Enter new City: ")
#                 print("✅ Student updated successfully!")
#                 return

#         print("❌ Student not found!")

#     # DELETE
#     def delete_student(self):
#         sid = input("Enter Student ID to delete: ")

#         for s in self.students:
#             if s.sid == sid:
#                 self.students.remove(s)
#                 print("✅ Student deleted successfully!")
#                 return

#         print("❌ Student not found!")


# # MAIN PROGRAM
# obj = CRUD()

# while True:
#     print("\n===== Student Management System =====")
#     print("1. Add Student")
#     print("2. Show Students")
#     print("3. Update Student")
#     print("4. Delete Student")
#     print("5. Exit")

#     choice = input("Enter your choice: ")

#     if choice == '1':
#         obj.add_student()
#     elif choice == '2':
#         obj.show_students()
#     elif choice == '3':
#         obj.update_student()
#     elif choice == '4':
#         obj.delete_student()
#     elif choice == '5':
#         print("👋 Exiting program...")
#         break
#     else:
#         print("❌ Invalid choice! Please try again.")


##Methods

##Instance Method 

# class Student:
#     def __init__(self, name, rollno, mob):   
#         self.name = name
#         self.rollno = rollno
#         self.mob = mob

#     def display(self):
#         print(self.name, self.rollno, self.mob)


# stud = Student("Prashant", 100, 5647354636)
# stud.display()
        
        
##Static Method


# class Student:
#     #by using class name we can access static method
#     @staticmethod #decorator
#     def get_personal_detail(firstname,lastname):
#         print("your personal detail=",firstname,lastname)
        
#     @staticmethod
#     def contact_detail(mobile_no,rollno):
#         print("your contact detail=",mobile_no,rollno)
        
# Student.get_personal_detail("prashant","jha")
# Student.contact_detail(565647655647,1001)

# Where we can declare static variable?
# Inside a class but outside of method
# In a constructor by using class name
# In an instance method by using class name
# In a class method using class name or cls variable
# In static method by using class name


# How do we access static variable?
# Inside instance method using self or class name
# In a constructor using self or class name
# In a class method using cls variable or class name
# In a static method using class name
# Outside of the class using object or class name


# How do we delete the static variable?
# del classname.staticvariablename
# Inside class method we can use cls variable:
# del cls.staticvariablename