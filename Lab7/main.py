import random

def set_array(size):
    arr = []
    for i in range(size):
        arr.append(random.randint(-49, 50))
    return arr

def print_2darray(arr):
    for subarray in arr:
        print(subarray)

def print_array(arr):
    i=0
    for elem in arr:
        print(str(elem).ljust(3) + " | ", end='')
        i+=1
        if i==20 or i==40 or i==60 or i==80:
            print()
    print()

def print_table(A, B, table):
    sizeA = len(A)
    sizeB = len(B)
    print(end="  ")
    for i in range(sizeB):
        print(B[i], end = " ")
    print()
    for i in range(sizeA):
        print(A[i], end = " ")
        for j in range(sizeB):
            print(table[i][j], end=" ")
        print()

def linear_search(arr, el):
    for i in range(len(arr)):
        if el == arr[i]:
            return el
        else: 
            continue
    return None

def binary_search(arr, el):
    start = 0
    end = len(arr) - 1
    while start<=end:
        mid_index = start +(end - start)//2
        mid_element = arr[mid_index]
        if mid_element == el:
            return mid_element
        elif el < mid_element:
            end = mid_index-1
        else:
            start = mid_index+1
    return None

def substring_search(S,T):
    sizeS = len(S)
    sizeT = len(T)
    #table = [[0]*(sizeT+1) for x in range(sizeS+1)]
    table = []
    for i in range(sizeS+1):
        subarr = []
        for j in range(sizeT+1):
            subarr.append(0)
        table.append(subarr)
    longest = 0
    common_substr = set()
    for i in range(sizeS):
        for j in range(sizeT):
            if S[i] == T[j]:
                c = table[i][j] + 1
                table[i+1][j+1] = c
                if c > longest:
                    common_substr = set()
                    longest = c
                    common_substr.add(S[i-c+1:i+1])
                elif c == longest:
                    common_substr.add(S[i-c+1:i+1])
    print_2darray(table)
    return common_substr

def subarr_search(in_arr, from_arr):
    maxlen = 0
    result = "Нема"
    for i in range(len(from_arr)):
        for step in range(0 ,len(from_arr)+1-i):
            #print("i: ", i, " | i+step: ", i+step, " | arr: ", from_arr[i: i+step])
            subarray = from_arr[i: i+step]
            for j in range(len(in_arr)):
                #print(subarray, " | ", in_arr[j:j+step])
                if subarray == in_arr[j:j+step] and len(subarray) >= maxlen:
                    if len(subarray) > maxlen:
                        maxlen = len(subarray)
                        result = str(subarray)
                    elif len(subarray) == maxlen:
                        result = result + "\n" + str(subarray)
                    #print("Result: ", result)
    print("Найбільші підрядки")
    print(result)


if True:
    length = 100
    A = set_array(length)
    B = set_array(length)
    A.sort()
    B.sort()
    print("Масив А")
    print_array(A)
    print("Масив B")
    print_array(B)
    while True:
        num = int(input("Введіть номер пошуку: "))
        if num ==1:
            common_elements = []
            for element in A:
                item = linear_search(B, element)
                if item==None:
                    continue
                else:
                    if item in common_elements:
                        continue
                    else:
                        common_elements.append(item)      
            print("Однакові елементи:")
            print_array(common_elements)
        elif num==2:
            common_elements = []
            for element in A:
                item = binary_search(B, element)
                if item==None:
                    continue
                else:
                    if item in common_elements:
                        continue
                    else:
                        common_elements.append(item)
            print("Однакові елементи:")
            print_array(common_elements)
        elif num == 3:
            strA = "revolutioner"
            strB = "conditioner"
            print(strA + "\n" +strB)
            print(substring_search(strA, strB))
            #subarr_search(strB, strA)
        else:
            
            break
