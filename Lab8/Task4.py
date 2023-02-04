import re

text1 = "computer: CPU, laptop mouse, disk port"
text2 = "GPU; mouse! keyboard_laptop"
print("Перший текст:\n\t" + text1)
print("Другий текст:\n\t" + text2)
arr2 = re.split(r"[\ \.\,\:\;\-\_\!\?]", text2)
for el in arr2:
    reg = reg = re.compile('(' +el + ')')
    text1 = re.sub(reg, "", text1)
print(text1)
