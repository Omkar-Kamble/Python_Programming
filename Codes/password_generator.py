import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"

strings = lower + upper + numbers + symbols
length = 8
password = "".join(random.sample(strings, length))

print("your generated password is " + password)