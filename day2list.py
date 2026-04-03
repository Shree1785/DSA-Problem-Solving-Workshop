# mylist=["Prashant","Ashish","komal","ankush","Ashish",77,"sandip",60.52,"prashant"]

# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:8:2])
# print(mylist[:])
# print(mylist[::-1])

##exchange indexing value
# mylist[2]="Akshay"
# print(mylist)

# if "ankush" in mylist:
#     print("yes ankush is available")
# else:
#     print("not available")


# mylist.append("harsh")
# mylist.append("laxman")
# print(mylist)


# mylist.insert(1,"sanket")
# print(mylist)

# mylist.remove('sandip')
# print(mylist)

# newlist=mylist.copy() #cloning
# print(mylist)
# print(newlist)


mylist=[["prashant","jha"],[85,56],[440022,"yyy"]]
# print("example of multidimensional list:")
# print(mylist)
# #print(mylist[row][col])
# print(mylist[0][0]) #"prashant"
# print(mylist[0][1]) #"jha"
# print(mylist[1][0]) #85,56
# print(mylist[2][0]) #44002
# print(mylist[2][1]) #"yyy"


# list1=["prashant","jha"]
# # print(list1*2)

# list2=[50,25,50]
# # print(list1+list2)

# list2=[50,25,50,"prashant"]
# del list2[2]
# print(list2)

# list2=[50,25,50,"prashant"]
# list2.clear()
# print(list2)

# name="prashant" #str
# print(name)
# myname=list(name)#typecasting
# print(myname)

# mylist=[40,30,20,10]
# mylist.reverse()
# print(mylist)

# #sorting example
# mylist=[44,24,77,0,9,88]  #0,9,22,44,77,88
# mylist.sort()#reverse=True
# print(mylist)


#list Alising
#Alising means assigning one variable reference to another variable
# mylist=[44,24,77,0,9,88]
# newlist=mylist #assigning the address
# print(id(mylist))
# print(id(newlist))
# mylist[0]="prashant"
# print(mylist)
# print(newlist)

#####mcq questions#####  to find output of the code

# arr=[[1,2,3,4],
#      [4,5,6,7],
#      [8,9,10,11],
#      [12,13,14,15]]
# for i in range(0,4):
#     print(arr[i].pop())



# arr=[1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1]=arr[i]
# for i in range(0,6):
#     print(arr[i], end="")



# fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]

# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kiwi'

# sum = 0

# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] == 'Kiwi':
#         sum += 20

# print(sum)


# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a)


# a=[1,2,3,4,5]
# print(a[3:0:-1])