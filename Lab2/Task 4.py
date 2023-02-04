if __name__ == '__main__':
    print("\n__________________________________________part 4______________________________\n")
    # Білого ферзя, чорного короля, чорного пішака
    queen_x = int(input("X королеви "))
    queen_y = int(input("Y королеви "))
    king_x = int(input("X короля "))
    king_y = int(input("Y короля "))
    pawn_x = int(input("X пішака "))
    pawn_y = int(input("Y пішака "))

    queenStatus = True
    kingStatus = True
    pawnStatus = True
    attackOnKing = False
    attackOnPawn = False
    kingDefendPawn = False
    pawnDefendKing = False
    queen_VS_king = 0
    queen_VS_pawn = 0

    ######################################################################
    if queen_x == king_x and queen_y == king_y:
        queenStatus = False
        kingStatus = False
        print("Координати Короля та Королеви збігаються")
    if queen_x == pawn_x and queen_y == pawn_y:
        pawnStatus = False
        queenStatus = False
        print("Координати Пішака та Королеви збігаються")
    if pawn_x == king_x and pawn_y == king_y:
        kingStatus = False
        pawnStatus = False
        print("Координати Короля та Пішака збігаються")

    if queen_x > 8 or queen_x < 1 or queen_y > 8 or queen_y < 1:
        print("Королева не на дощці")
        queenStatus = False
    if king_x > 8 or king_x < 1 or king_y > 8 or king_y < 1:
        print("Король не на дощці")
        kingStatus = False
    if pawn_x > 8 or pawn_x < 1 or pawn_y > 8 or pawn_y < 1:
        print("Пішак не на дошці")
        pawnStatus = False
    #######################################################################

    if king_y != queen_y and queenStatus and kingStatus:
        queen_VS_king = abs(queen_x - king_x) / abs(queen_y - king_y)
    if pawn_y != queen_y and queenStatus and pawnStatus:
        queen_VS_pawn = abs(queen_x - pawn_x) / abs(queen_y - pawn_y)

    # Захист фігури, якщо своя фігура в клітині биття
    if kingStatus:
        if pawnStatus:
            if(king_x + 1 == pawn_x and king_y == pawn_y) or (king_x - 1 == pawn_x and king_y == pawn_y):
                kingDefendPawn = True
            elif (king_x == pawn_x and king_y + 1 == pawn_y) or (king_x == pawn_x and king_y - 1 == pawn_y):
                kingDefendPawn = True
            elif (king_x + 1 == pawn_x and king_y - 1 == pawn_y) or (king_x - 1 == pawn_x and king_y - 1 == pawn_y):
                kingDefendPawn = True
            elif (king_x + 1 == pawn_x and king_y + 1 == pawn_y) or (king_x - 1 == pawn_x and king_y + 1 == pawn_y):
                kingDefendPawn = True
    if pawnStatus:
        if kingStatus:
            if (pawn_x - 1 == king_x and pawn_y - 1 == king_y) or (pawn_x + 1 == king_x and pawn_y - 1 == king_y):
                pawnDefendKing = True


    print("\nМожливі дії Королеви:")
    if queenStatus:
        if kingStatus:
            if (queen_x == king_x) or (queen_y == king_y) or (queen_VS_king == 1):
                print("\tНапад на Короля")
                attackOnKing = True
                if pawnDefendKing:
                    print("\tКороль під захистом Пішака")
        if pawnStatus:
            if (queen_x == pawn_x) or (queen_y == pawn_y) or (queen_VS_pawn == 1):
                print("\tНапад на Пішака")
                attackOnPawn = True
                if kingDefendPawn:
                    print("\tПішак під захистом Короля")
    else:
        print("\tКоролева поза грою")


    print("\nМожливі дії Пішака")
    if pawnStatus:
        if queenStatus:
            if (pawn_x - 1 == queen_x and pawn_y - 1 == queen_y) or (pawn_x + 1 == queen_x and pawn_y - 1 == queen_y):
                print("\tНапад на Королеву")
                if attackOnKing:
                    print("\tЗахист Короля шляхом побиття Королеви")
            else:
                print("\tДій немає")
    else:
        print("\tПішак поза грою")


    print("\nМожливі дії Короля")
    if kingStatus:
        if queenStatus:
            if(king_x + 1 == queen_x and king_y == queen_y) or (king_x - 1 == queen_x and king_y == queen_y):
                print("\tНапад на Королеву")
                if attackOnPawn:
                    print("\tЗахист Пішака шляхом побиття Королеви")
            elif (king_x == queen_x and king_y + 1 == queen_y) or (king_x == queen_x and king_y - 1 == queen_y):
                print("\tНапад на Королеву")
                if attackOnPawn:
                    print("\tЗахист Пішака шляхом побиття Королеви")
            elif (king_x + 1 == queen_x and king_y - 1 == queen_y) or (king_x - 1 == queen_x and king_y - 1 == queen_y):
                print("\tНапад на Королеву")
                if attackOnPawn:
                    print("\tЗахист Пішака шляхом побиття Королеви")
            elif (king_x + 1 == queen_x and king_y + 1 == queen_y) or (king_x - 1 == queen_x and king_y + 1 == queen_y):
                print("\tНапад на Королеву")
                if attackOnPawn:
                    print("\tЗахист Пішака шляхом побиття Королеви")
            else:
                print("\tДій немає")
