
##File Handling

# f=open("myfile.txt","w")
# print("name of file:",f.name)
# print("file mode:",f.mode)
# print("readable:",f.readable())
# print("writable:",f.writable())
# print("file closed:",f.closed)
# f.close()
# print("file closed:",f.closed)


##performing write operation

# f=open("myfile.txt","w")
# f.write("\n Nagpur is a smart city")
# f.close()
# print("file operation is done")

# f=open("myfile.txt","a")
# f.write("\n Pune is a smart city")
# f.close()
# print("file operation is done")


##inserting list

# f=open("myfile.txt","w")
# mylist=["prashant","mahesh","suresh"]
# f.writelines(mylist)
# f.close()
# print("written work has done successfully")


# f = open("myfile.txt", "w")

# # List
# mylist = ["prashant", "mahesh", "suresh"]
# f.write("List Data:\n")
# for item in mylist:
#     f.write(item + "\n")

# # Tuple
# mytuple = ("apple", "banana", "cherry")
# f.write("\nTuple Data:\n")
# for item in mytuple:
#     f.write(item + "\n")

# # Dictionary
# mydict = {"name": "Prashant", "age": 22, "city": "Pune"}
# f.write("\nDictionary Data:\n")
# for key, value in mydict.items():
#     f.write(str(key) + " : " + str(value) + "\n")

# f.close()

# print("Written work has done successfully")



##reading data from a file

# f=open("myfile.txt","r")
# print(f.read())
# f.close()


# with open("myfile.txt","w") as f:
#     f.write("amit\n")
#     f.write("ashish\n")
#     f.write("prashant\n")
#     print("file closed:",f.closed)
# print("file closed:",f.closed)


# with open("myfile.txt","r") as f:
#     content=f.read()
#     print(content)


# f1=open("Guido.jpg","rb")
# f2=open("Rossom.jpg","wb")
# data=f1.read()
# f2.write(data)
# print("New Image is available with the name:")



##Operation with CSV file

# import csv
# f=open("student.csv","a",newline="")
# a=csv.writer(f) #here it will return cswriter object
# # a.writerow(["studentId", "rollno", "name", "mobileno"])

# studentId = int(input("Enter student id:"))
# rollno = int(input("Enter your roll no:"))
# name = (input("Enter your name:"))
# mobileno = int(input("Enter your mobile no:"))
# a.writerow([studentId, rollno, name, mobileno])
# print("student record has save")



##Generate code for

#["rollno","name","mobileno","p1","p2","p3","total","percentage","email","result"]

#"rollno","name","mobileno","p1","p2","p3" (you have accept)

#"total","percentage" (calculate)

#"result"(pass/fail)

#if user is pass in all subjects then pass else fail (passing score=40)


# import csv

# f = open("result.csv", "a", newline="")
# a = csv.writer(f)

# rollno = int(input("Enter roll no: "))
# name = input("Enter name: ")
# mobileno = input("Enter mobile no: ")   # keep as string
# p1 = int(input("Enter marks of subject 1: "))
# p2 = int(input("Enter marks of subject 2: "))
# p3 = int(input("Enter marks of subject 3: "))
# email = input("Enter email: ")

# total = p1 + p2 + p3
# percentage = total / 3

# if p1 >= 40 and p2 >= 40 and p3 >= 40:
#     result = "Pass"
# else:
#     result = "Fail"

# a.writerow([rollno, name, mobileno, p1, p2, p3, total, percentage, email, result])

# f.close()

# print("Student record has been saved successfully")