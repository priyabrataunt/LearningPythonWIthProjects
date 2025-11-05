#email = "priyabrata@gmail.com"

email = input("What's your email?: ")

if "@" in email and "." in email:
    print(f"{email} is correct! Whooo!")

else:
    print("{email} is incorrect! Sorry try again!")
