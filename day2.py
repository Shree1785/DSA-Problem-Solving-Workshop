# name="prashantjha"
# #indexing=012345678910
# print(name[0]) #p
# print(name[1]) #r
# print(name[-1]) #a
# #print(name[15]) Error string index out of range
# print(name[0:5]) # end-1,5-1=4 prash
# print(name[1:])#rashantjha
# print(name[:5])#5-1=4 prash
# print(name[:])
# print(name[1:8:2])# 8-1=7 rsat
# print(name[::-1])







# s = "Python is a High level programming language"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())



# print('Subject Marks:')
# phy=50
# chem=60
# math=70
# print("physics={} chemistry={} math{}".format(phy, chem, math))
# print("physics={0} chemistry={1} math{2}".format(phy, chem, math))
# print("physics={x} chemistry={y} math{z}".format(x=phy, y=chem, z=math))
# total=phy+chem+math
# print("Total marks",f"{total}")
# print("Roll no=","7".zfill(4))


#for(initialization; condition; inc/dec)
# for i in range(5): #i=5
#     print(i)
    
# for i in range(1,5): #i=2
#     print(i)
    
# for i in range(1,11,2): #i=5
#     print(i)

# for i in range(1,11):
#     print(i*2)

# for i in range(1,11):
#     print(i*2,"",i*3,"",i*4,"",i*5,"",i*6,"",i*7,"",i*8,"",i*9,"",i*10)
    
# print()

# for i in range(1,11):
#     print(i*11,"",i*12,"",i*13,i*14,"",i*15,"",i*16,"",i*17,"",i*18,"",i*19,"",i*20)

# print()

# name="racear"
#       #012345
      
# for i in name: #i=1:
#     print(i)

##WAP to remove duplicates using for loop

# name = "racear"
# newname = "" #race
# for i in name:
#     if i not in newname:
#         newname += i
        
# print(name)
# print(newname)

# for i in range(5,0,-1):
#     print(i)
    
##print to 10 to 1 at the difference of 2

# for i in range(10,0,-2):
#     print(i)
    
##WAP to  reverse the string using for loop

# name="Mumbai"
# n=len(name)
# print(n) #n=6
# newname=""

# name="Mumbai"
#      #012345     
# newname=""
# n=len(name) #n=6
# for i in range(n-1,-1,-1): #i=5
#     newname += name[i] #name[5]
# print(newname)
    
    
##Check for Palindrome
##Question: WAP to check if a given string is a palindrome

# name="racecar"
# print(name)
# print(name[::-1])

# if name==name[::-1]:
#     print("palindrome string")
# else:
#     print("Not palindrome string")


## Python Collection Data Type