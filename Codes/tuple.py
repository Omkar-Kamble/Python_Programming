# tuple : it is similar to list but it is immutable (you cannot change).
# parenthesis() in tuple is optial 
marks = (98, 87, 99, 97, 97, 97)
#it shows you how many time number is present in tuple using count() function
print(marks.count(97)) 
print(marks.count(90)) #if number is not present in tuple it will return you 0.
print(marks.index(97)) #it will return you index value of any numbers in tuple
