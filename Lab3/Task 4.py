if __name__ == '__main__':
    x=10
    for i in range(x, 0, -1):
        for j in range(2):
            print(i, " green bottles hanging on the wall,")
        print("And if one green bottle should accidentally fall,\n"
              "There\'ll be ", i-1, "green bottles hanging on the wall.\n")