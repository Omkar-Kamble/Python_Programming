#list : list is a collection of items, you can store different datatypes in it.
# in list, -1 means last item of any list
marks = [89, 95, 99, "history",98.33,'O']
print(marks)
print(marks[2]) #it prints 2nd index position item
print(marks[-1]) #it prints last item
print(marks[-6]) #it prints first item
print(marks[1:3]) #it prints index 1 to 2, it does not print index 3
print(marks[0:5]) #it prints index 1 to 4, it does not print index 5
marks.reverse() # it prints items in reverse order
print(marks)

for score in marks: #you can access list items sequentially
    print(score)
