if __name__ == '__main__':
    numberOfTickets = int(input("Скыльки купити лотерейних білетів: "))
    if numberOfTickets >= 100:
        print("Ви вийграли водокачку")
    else:
        if numberOfTickets == 0:
            print("Відключити газ")
        else:
            print("Ви нічого не вийграли")