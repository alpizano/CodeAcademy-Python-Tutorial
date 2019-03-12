n = [1,3,5, 7 ,9]

print (n)

print (n[2])

n[2] = n[2]*5

print (n)

n.pop(0) # deletes and returns

print ("After deleting the 0th index item: %s" % n)

n.remove(9) # deletes if finds item

print ("After popping number 9: %s" % n)


del(n[2]) # deletes but doesn't return

print ("After deleting the 2th index item: %s" % n)