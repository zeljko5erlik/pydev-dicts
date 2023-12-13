shopping_list = []
shopping_list_item = {}

# shopping_list = [
#     {'grocery': 'Kulen', 'price': 8.99,}
#     {'grocery': 'Seka', 'price': 5.99},
#     {'grocery': 'cvarci', 'price': 4.99}
# ]

shopping_list_size = int(input('Unesite broj namirnica: '))

for i in range(shopping_list_size):
    grocery = input('Unesite ime namirnice: ')
    price = float(input('Unesite cijenu namirnice: '))

    shopping_list_item = {}
    shopping_list_item[grocery] = price
    # shopping_list_item['grocery'] = grocery
    # shopping_list_item['price'] = price

    shopping_list.append(shopping_list_item)

for item in shopping_list:
    for key, value in item.items():
        print(key, value)