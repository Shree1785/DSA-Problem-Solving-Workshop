
#Tower Of Hanoi

# Simple Rules To Play Game?

# 1.We can move only one disk at a time
# 2.We have to pick upper disk from any one pipe
# 3.We have to place on top of any disk
# 4.We can not place any large disk on top of smaller disk


# Tower of Hanoi
# import time

# class Tower:

#     def __init__(self):
#         print("WELCOME TO TOWER OF HANOI GAME")
#         print()

#         print("Given problem:")
#         print("A =", [3, 2, 1], "   B =", [], "   C =", [])
#         print()

#         print("Expected Output:")
#         print("A =", [], "   B =", [], "   C =", [3, 2, 1])
#         print()

#         # initialize rods
#         self.A = [3, 2, 1]
#         self.B = []
#         self.C = []

#     # Insert item into A
#     def tower(self, item):
#         self.A.append(item)
#         time.sleep(1)
#         print("A =", self.A)
#         print("Items in Tower A\n")

#     # Pass 1
#     def pass1(self):
#         self.temp = self.A.pop(2)   # remove 1
#         self.C.append(self.temp)
#         time.sleep(1)
#         print("A =", self.A, " B =", self.B, " C =", self.C)
#         print("Pass One Completed\n")

#     # Pass 2
#     def pass2(self):
#         self.temp = self.A.pop(1)   # remove 2
#         self.B.append(self.temp)
#         time.sleep(1)
#         print("A =", self.A, " B =", self.B, " C =", self.C)
#         print("Pass Two Completed\n")

#     # Pass 3
#     def pass3(self):
#         self.temp = self.C.pop(0)   # move 1
#         self.B.append(self.temp)
#         time.sleep(1)
#         print("A =", self.A, " B =", self.B, " C =", self.C)
#         print("Pass Three Completed\n")

#     # Pass 4
#     def pass4(self):
#         self.temp = self.A.pop(0)   # move 3
#         self.C.append(self.temp)
#         time.sleep(1)
#         print("A =", self.A, " B =", self.B, " C =", self.C)
#         print("Pass Four Completed\n")

#     # Pass 5
#     def pass5(self):
#         self.temp = self.B.pop(1)   # move 1
#         self.A.append(self.temp)
#         time.sleep(1)
#         print("A =", self.A, " B =", self.B, " C =", self.C)
#         print("Pass Five Completed\n")

#     # Pass 6
#     def pass6(self):
#         self.temp = self.B.pop(0)   # move 2
#         self.C.append(self.temp)
#         time.sleep(1)
#         print("A =", self.A, " B =", self.B, " C =", self.C)
#         print("Pass Six Completed\n")

#     # Pass 7
#     def pass7(self):
#         self.temp = self.A.pop(0)   # move 1
#         self.C.append(self.temp)
#         time.sleep(1)
#         print("A =", self.A, " B =", self.B, " C =", self.C)
#         print("Pass Seven Completed\n")


# # main execution
# t = Tower()

# t.pass1()
# t.pass2()
# t.pass3()
# t.pass4()
# t.pass5()
# t.pass6()
# t.pass7()