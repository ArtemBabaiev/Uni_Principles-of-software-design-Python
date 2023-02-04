def get_cost(owner_car: str, price_sparepart: tuple, price_inspection: int):
    average = 0
    for i in range(6):
        average += price_sparepart[i]
    average /= 6
    invoice = round(0.7 * average + 0.95*price_inspection, 2)
    print(f"Клієнт {owner_car} – ваша ціна до оплати становить {invoice}")


if __name__ == '__main__':
    get_cost("art", (150, 45, 56, 78, 79, 45), 450)
