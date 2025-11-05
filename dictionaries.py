# Dictionaries

Menu = {"butter chicken" : 5.00,
        "biriyani" : 12.00,
        "rice thali": 8.00,
        "tacos": 4.00,
        "indian thali": 9.00,
        "naan": 2.00}

cart = []
total = 0

for key, value in Menu.items():
    print(f"{key:20}: ${value:.2f}")

while True:
    food = input("Enter an Item(q to quit): ").lower()
    if food == "q":
        break
    elif Menu.get(food) is not None:
        cart.append(food)

print("---------------YOUR ORDER -----------------")
for food in cart:
    total += Menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total: .2f}")