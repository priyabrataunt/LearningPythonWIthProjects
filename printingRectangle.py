# TO create a Rectagle using loops

len = input("How many stars for the length ")
bred = input("How many stars for Breadth ")

for x in range(int(len)):
    for y in range(int(bred)):
        print('*', end=' ')
    print()