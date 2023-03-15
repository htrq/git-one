# for in Python is behaving like foreach in cpp or java

array = ["a", "b", "c"]
for i in array:
    print(i)

# testing built-in function range() that generates arithmetic progression
print("\nfirst for:")
for i in range(5):
    print(i)

# below futhermore examples of range func
# this example lets to suggest step over every iteration
print("\nsecond for:")
for i in range(0, 10, 2):
    print(i)

# or in this example we just set range
print("\nthird for:")
for i in range(10, 20):
    print(i)