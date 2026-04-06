# Extending property from one class to another class is called inheritance.

# Directly we are getting here reusability concept.

# Base class: A class which inherits its property to another is called base class or parent class.
# Derived class: A class in which properties are inherited is called derived class or child class.

# Types of inheritance:

# 1.Single inheritance
# 2.Multilevel inheritance
# 3.Multiple inheritance


# # 1.Single level inheritance

# class College: #parent class
#     def college_name(self): #member function of college
#         print("Modern College")
        
# class Student(College): #child class
#     def student_info(self): #member function
#         print("Name: Prashant Jha")
#         print("Branch: Mechanical")
        
# obj=Student() #object create child class
# obj.college_name()
# obj.student_info()


# 2.Multilevel inheritance

# class College: #first class first-level
#     def college_name(self):
#         print("Modern College")
        
# class Student(College): #second class second-level
#     def student_info(self):
#         print("Name: Prashant Jha")
#         print("Branch: Mechanical")
        
# class Exam(Student): #child class
#     def subject(self):
#         print("Subject1: Design Engineering")
#         print("Subject2: Math")
#         print("Subject3: C-Language")
        
# obj=Exam()
# obj.college_name()
# obj.student_info()
# obj.subject()



# 3.Multiple inheritance

# class SubMarks:   # class-1
#     math = int(input("Enter paper marks of math :"))
#     DE = int(input("Enter paper marks of designing engineering :"))
#     C = int(input("Enter paper marks of c language :"))
#     english = int(input("Enter paper marks of english :"))


# # ===================== parent class -1 =====================

# class PractMarks:   # class
#     cprac = int(input("Enter practicals marks of c language :"))


# # ===================== parent class -2 =====================

# class Result(SubMarks, PractMarks):   # child class
#     print("if student pass in both subject and practical paper then pass")

#     def total(self):
#         if self.math >= 40 and self.DE >= 40 and self.C >= 40 and self.english >= 40 and self.cprac >= 20:
#             print("pass")
#         else:
#             print("fail")


# obj = Result()
# obj.total()