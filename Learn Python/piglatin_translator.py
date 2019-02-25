
# raw_input renamed to input in Python 3
word = input("Input a word in English: ")
print ("You've entered: %s" % word)

print (len(word))

if len(word) > 0:
    print("Good!, this is a valid word!")
else:
    print("Please enter a valid word!")

print (len(word)-1)

last = len(word)

first = word[0].lower()

print (first)

print (word[1:last])

meat = word[1:last]

print ("The pig latin phrase of %s is: %s%say" % (word,meat,first))


#word[last_let] = word[0]
#print (word + "ay")