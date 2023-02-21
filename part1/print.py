# this is how write in many lines message
print("""\
Usage: command
bla-bla
bla-bla
""")

# raw string practice
print(r'C:\some\name')
# therefore typing something else
print('C:\some\name')

# Multiline comment 
# Favor to write this 
# way

#some plays with concatinations
conc_play = 40 * 'lool ' + 'hoo-hoo ' + 'cheetos laand '
print(conc_play)

print("if you put separated textes " "they will be joined " "and printed anyway")

#and here is indexing in strings
word = "Halloween twenty twenty three"
print(word[9])
#It also works with negative value when we need to count vice versa
print(word[-5])
# Even when we need to output some length text we can use such syntax
print(word[0:9])
# Or point the begin and let it output data til the end
print(word[10:])
# Also can count from negative positioned character
print(word[-5:])
# This can also been concatinated lol 
print(word[0:5] + word[-24:-20])

#Function that shows the length of the text len()
print(len(word)) 

