import random

symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password = ""

length = int(input("Wpisz długość hasła: "))
for i in range(length):
    password += random.choice(symbols)
  
print(password)
