import random
chars = "qwertyuiopasdfghjklzxcvbnm@#&?!1234567890QWETRYUIOPASDFGHJKLZXCVBNM"
length = int(input("Enter length:"))
password=""

for a in range(length):
  password+=random.choice(chars)
print(password)