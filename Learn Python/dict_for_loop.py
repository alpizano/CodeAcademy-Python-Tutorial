# Write your function below!
def fizz_count(x):
  count = 0
  for item in x:
    if (item == "fizz"):
      count = count + 1
  return count

prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

for i in prices:
  print ("%s price: %s stock: %s" % (i,prices[i],stock[i]))