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

# It is possible to make lists of lists(it calls nested lists)
a = [1, 2, 3, 4]
b = ['a', 'b', 'c', 'd']
c = [a, b]
print(c)
print(c[1])     # out index list 1
print(c[0][2])  # out indexed list 0 with idexed value 2