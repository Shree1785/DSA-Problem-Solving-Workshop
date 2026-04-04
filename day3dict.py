## dict Datatype

mydict={
    101: "prashant",
    102:"ashish",
    "103":"mohini",
    "104":"trivani",
    101: "ashish",
    104: "ashish"
}
print(mydict)

##With the help of key we have to print values
# a= mydict[102]
# print(a)

##We will replace old valueby new value
# mydict[102]="peter"
# print(mydict)

##Only print key x=0,1
# for x in mydict:
#     print(x)
    
##Only print values
# for x in mydict.values():
#     print(x)

##Printing Key and Values both
# for x,y in mydict.items():
#     print(x,y)

##If i have to add new key and value pair in my dictionary
# mydict["mobile_no"]=4646463738
# print(mydict)


#####mcq questions what will be the output of the code#####

# a={(1,2):1,(2,3):2,(4,5):3}
# print(a[4,5])

# a={"a":1,"b":2,"c":3}
# print(a["a","b"])

# arr={}
# arr[1]=1
# arr['1']=2
# arr[1]+=1
# print(arr)
# sum=0
# for k in arr:
#     sum+=arr[k]
# print(sum)


# my_dict={}
# my_dict[1]=1
# my_dict['1']=2
# my_dict[1.0]=4

# sum=0
# for k in my_dict:
#     sum +=my_dict[k]
# print(sum)

# my_dict={}
# my_dict[(1,2,4)]=8
# my_dict[(4,2,1)]=10
# my_dict[(1,2)]=12
# sum=0
# for k in my_dict:
#     sum +=my_dict[k]
# print(sum)
# print(my_dict)


# box={}
# jars={}
# crates={}
# box['biscuit']=1
# box['cake']=3
# box['jam']=4
# crates['box']=box
# crates['jars']=jars
# print(len(crates[box]))


# dict={'c':97, 'a':96, 'b':98}
# for _ in sorted(dict):
#     print(dict[_])


# rec={"Name": "Python","Age": "20"}
# r=rec.copy()
# print(id(r) == id(rec))
# print(id(r))
# print(id(rec))


# rec={"Name": "Python", "Age": "20", "Addr": "NJ", "Country": "USA"}
# id1=id(rec)
# print(id(id1))
# del rec
# rec={"Name": "Python", "Age": "20", "Addr": "NJ", "Country": "USA"}
# id2=id(rec)
# print(id(id2))
# print(id1 == id2)


##Find the Key with the Minimum Value in a Dictionary:
##Question- Write a function to find the key with the minimum value in a dictionary
##Logic- Iterate through the dictionary and keep track of the key with the minimum value
##Sample Input: {"X":20, "Y":10, "Z":30}
##Expected Output: "Y"

# data = {"X": 20, "Y": 10, "Z": 30}

# min_key = None
# min_value = float('inf')

# for key in data:
#     if data[key] < min_value:
#         min_value = data[key]
#         min_key = key

# print(min_key)


##imp: If we want to represent binary data like images,videos

# mydict={
#     101:"prashant",
#     "professional":"developer",
#     "empid":1001
# }

# mydict.pop(101)
# print(mydict)


##Nested for loop

#(i,j)= (2,3),

# for i in range(1,4): #outer loop-rows
#          for j in range(1,4):#innerloop-columns
#              print(i,end="  ")
#          print()


# n=int(input("Enter the number of rows:"))#n=5
# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print(j,end=" ")
#     print()


# n=int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print(chr(64+i),end=" ")
#     print()


# n=int(input("Enter the number of rows:"))#n=5
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print("*",end=" ")
#     print()


# n=int(input("Enter the number of rows:"))#5
# for i in range(1,n+1):
#      for j in range(1,n+2-i):
#          print(chr(64+j),end=" ")
#      print()



# import time
# n=int(input("Enter the number of rows:"))#5
# for i in range(1,n+1):
#      for j in range(1,n+2-i):
#          time.sleep(2)
#          print(n+1-i,end=" ")
#      print()



import time
n=int(input("Enter the number of rows:"))#5
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1, i+1):
         time.sleep(2)
         print("*",end=" ")
    print()                    