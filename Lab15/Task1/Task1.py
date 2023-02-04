class Stack():
    def __init__(self):
        self.__lst = []

    def push(self, item):
        self.__lst.append(item)

    def pop(self):
        return self.__lst.pop()
    def __len__(self):
        return len(self.__lst)

file = open("formula.txt", "w")
file.write("((((1+2)-4*(a-3)/(2-7+6))))")
file.close()
file = open("formula.txt", "r")
text = file.read()
file.close()
brackets = Stack()
isBalanced = True
positions = []
for i in range(len(text)):
    if text[i]=="(":
        brackets.push("(")
    elif text[i] == ")":
        if len(brackets) == 0:
            isBalanced = False
        else:
            brackets.pop()
            positions.append(i)
if isBalanced and len(brackets) == 0:
    print("Збалансоване")
    print("Позиції закриваючих дужок")
    for item in positions:
        print(f"{item}", end=" | ")
    print()
else:
    print("Не збалансоване")
