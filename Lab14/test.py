from Linked1 import Linked1

lst = Linked1()
lst.MyAddLast(11)
lst.MyAddLast(14)
lst.MyAddFirst(4)
print(f"Довжина: {len(lst)}")
for item in lst:
    print(item, end=" | ")