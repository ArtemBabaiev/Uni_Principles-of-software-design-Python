from Classes import ShopMan, LoopList
from random import randint


def ranstr():
    temp = ''
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y']
    for i in range(3):
        temp += letters[randint(0, len(letters) - 1)]
    return temp


if __name__ == '__main__':
    people = LoopList()
    products = LoopList()
    products.Add("fruit")
    products.Add("bread")
    products.Add("milk")
    products.Add("water")
    products.Add("meat")
    products.Add("pepper")
    products.Add("vegetables")
    products.Add("salt")
    products.Add("sugar")
    products.Add("flour")
    for i in range(3):
        people.Add(ShopMan(ranstr(), randint(1, 4)))
    for item in people:
        print(f"Покупець {item.Name}")
        for el in products:
            if input(f"Чи купити {el} (Y - так; N - ні): ") == "Y":
                if item.NumToBuy == 0:
                    print("Цей покупець купив максимальну кількість")
                    break
                item.AddToCart(el)
        if input("Закінчити покупки (Y - так; N - ні): ") == "Y":
            break
    people.PrintShoppers()
