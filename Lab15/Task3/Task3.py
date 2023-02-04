from MyTree import Node, Tree
import os


def clean_console(): return os.system('cls')


clean_console()

tree = Tree()
tree.add("4MyComputer")
tree.add("2C")
tree.add("5D")
tree.add("1ProgramFiles")
tree.add("3ProgramFiles(x86)")
tree.add("7University")
tree.add("6PKPZ")
tree.add("8VM")

tree.in_order()
print()
tree.pre_order()
print()
tree.post_order()
print()
print(tree.search("2C"))
print(tree.search("2E"))