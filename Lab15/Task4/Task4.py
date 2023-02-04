from Graph import Graph
import os


def clean_console(): return os.system('cls')


clean_console()

graphCont = Graph()
cont = [[1, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0, 1],
        [1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]]
graphCont.CreateContiguity(cont)
graphCont.PrintІncidence()

print("*"*100)

graphInd = Graph()
inde = [[2,  1, -1, 0,  0,  0, -1,  0,  0,  0],
        [0,  0,  1, 2,  1,  1,  0,  0,  0,  0],
        [0,  0,  0, 0,  0,  0,  1,  1,  1,  0],
        [0,  0,  0, 0,  0, -1,  0,  0, -1,  1],
        [0,  0,  0, 0,  0,  0,  0, -1,  0, -1],
        [0, -1,  0, 0, -1,  0,  0,  0,  0,  0]]
graphInd.CreateІncidence(inde)
graphInd.PrintVectors()

print("*"*100)

graphVec = Graph()
vector = {"a": ["a", "f"], "b": ["a", "b", "d", "f"],
          "c": ["a", "d", "e"], "d": ["e"]}
graphVec.CreateVectors(vector)
graphVec.PrintContiguity()
