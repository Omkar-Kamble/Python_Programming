# range : we can generate a sequence of numbers using range() function
# range(10) will generate numbers using from 0 to 9 (10 numbers) 

i = range(5) # it prints range(0, 5)
print(i)

for numbers in range(5): # it prints numbers from 0 to 4 in horizontal form
    print(numbers, end=" ")
print()
for numbers in range(2,10): # it prints numbers from 3 to 9 in horizontal form 
    print(numbers, end=" ")
print()

for i in range(4): # it prints numbers 0 to 3 in vertical form
    print(i)