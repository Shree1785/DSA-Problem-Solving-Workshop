

##Graph consists of a finite set of Vertices (or nodes) and a set of Edges which connect a part of nodes.
##Eg- Map


# Vertices : Vertices are the nodes of the graph

# Edge : The edge is the line that connects pairs of vertices

# Unweighted graph : A graph which does not have a weight associated with any edge

# Weighted graph : A graph which has a weight associated with any edge

# Undirected graph : In case the edges of the graph do not have a direction associated with them

# Directed graph : If the edges in a graph have a direction associated with them


# If a graph is complete or almost complete we should use Adjacency Matrix

# If the number of edges are few then we should use Adjacency List


#       A  B  C  D  E
# A     0  1  1  1  0
# B     1  0  0  0  1
# C     1  0  0  1  0
# D     1  0  1  0  1
# E     0  1  0  1  0


# A → B → C → D
# D → A → E
# C → A → D
# D → A → C → E
# E → B → D




# class Graph:
#     def __init__(self):
#         self.adjacency_list = {}
        
#     def add_vertex(self, vertex):
#         if vertex not in self.adjacency_list.keys():
#             self.adjacency_list[vertex] = []
#             return True
#         return False


#     def add_edge(self, vertex1, vertex2):
#         if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
#             self.adjacency_list[vertex1].append(vertex2)
#             # self.adjacency_list[vertex2].append(vertex1)
#             return True
#         return False
    
#     def print_graph(self):
#         for vertex in self.adjacency_list:
#             print(vertex, ":", self.adjacency_list[vertex])


# my_graph = Graph()
# my_graph.add_vertex("A")
# my_graph.add_vertex("B")
# my_graph.add_vertex("C")
# my_graph.add_vertex("D")
# my_graph.add_vertex("E")


# my_graph.add_edge("A", "B")
# my_graph.add_edge("A", "C")
# my_graph.add_edge("A", "D")
# my_graph.add_edge("B", "A")
# my_graph.add_edge("B", "E")
# my_graph.add_edge("C", "D")
# my_graph.add_edge("D", "A")
# my_graph.add_edge("D", "C")
# my_graph.add_edge("D", "E")
# my_graph.add_edge("E", "B")
# my_graph.add_edge("E", "D")

# my_graph.print_graph()




# class Graph:
#     def __init__(self):
#         self.adjacency_list = {}
        
#     def add_vertex(self, vertex):
#         if vertex not in self.adjacency_list:
#             self.adjacency_list[vertex] = []
#             return True
#         return False

#     def add_edge(self, vertex1, vertex2):
#         if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
#             self.adjacency_list[vertex1].append(vertex2)
#             return True
#         return False
    
#     def print_graph(self):
#         for vertex in self.adjacency_list:
#             print(vertex, ":", self.adjacency_list[vertex])


# # Create graph
# my_graph = Graph()

# # Add vertices
# my_graph.add_vertex("A")
# my_graph.add_vertex("B")
# my_graph.add_vertex("C")
# my_graph.add_vertex("D")
# my_graph.add_vertex("E")
# my_graph.add_vertex("F")

# # Add edges (both directions for undirected graph)

# # A connections
# my_graph.add_edge("A", "B")
# my_graph.add_edge("A", "C")

# # B connections
# my_graph.add_edge("B", "A")
# my_graph.add_edge("B", "D")
# my_graph.add_edge("B", "E")

# # C connections
# my_graph.add_edge("C", "A")
# my_graph.add_edge("C", "E")

# # D connections
# my_graph.add_edge("D", "B")
# my_graph.add_edge("D", "E")
# my_graph.add_edge("D", "F")

# # E connections
# my_graph.add_edge("E", "C")
# my_graph.add_edge("E", "D")
# my_graph.add_edge("E", "F")

# # F connections
# my_graph.add_edge("F", "D")
# my_graph.add_edge("F", "E")

# # Print graph
# my_graph.print_graph()



# import datetime

# date = datetime.datetime.now()
# print("Today's date: {:%d/%m/%Y %H:%M:%S}".format(date))



# a = [i*i for i in range(1,11)]  # 1 to 5
# print(a)

# # a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# val = [2*i for i in range(1,6)]  # i = 1,2,3,4,5
# print(val)

# val2 = [i for i in a if i%2==0]
# print(val2)




# Dictionary Comprehension:

# squares = {x: x*x for x in range(1,6)}
# print(squares)

# doubles = {x: 2*x for x in range(1,6)}
# print(doubles)