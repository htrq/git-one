list = [2, 4, 8, 16, 32]
print(list)
list[1] = 0
print(list)
print(list[2:]) # Lists can also as strings be indexed
print(list[:])  # Some way to out whole list

# method that adds new elements to the end of the list append()
list.append(609)
print(list)

# built-in function len as for strings is also appied to lists
print(len(list))