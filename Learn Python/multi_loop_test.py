def test(x):
    return x*i

x_list = [1,2,3,4,5]

for i in range(6):
    for x in x_list:
        print (test(x)) # loop can access i var inside function


y_list = [1,5,3,7,1]
tot = 0
print ("Length of y list is: %s " % len(y_list))
for k in y_list:
    tot += k
    print (tot)




