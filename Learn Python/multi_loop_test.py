def test(x):
    return x*i

x_list = [1,2,3,4,5]

for i in range(6):
    for x in x_list:
        print (test(x)) # loop can access i var inside function


y_list = [1,5,3,7,1]
tot = 0
avg = 0

print ("Length of y list is: %s " % len(y_list))
for idx,k in enumerate(y_list):
    tot += k
    avg = tot/len(y_list)
    print ("At iteration %s, total of y_list is: %s" % (idx,tot))
print ("The manual average of y_list is: %s" % avg)
print ("The final total of y_list is: %s" % tot)

the_sum = sum(y_list)
the_avg = the_sum/len(y_list)

print ("The sum of y_list is: %s" % the_sum)
print ("The avg of y_list using built in funct is: %s" % the_avg)

test_list = []

test_list.append(1)
test_list.append(3)
test_list.append(5)

print (test_list)

for epoch in range(3):
    print ("hello")

n = [3, 5, 7]


def print_list(x):
    for i in range(0, len(x)):
        print (x[i])


print_list(n)
