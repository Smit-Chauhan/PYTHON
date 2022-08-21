prices = [10, 22, 30, 40, 58, 60]

def halve(num):
  no_tax = 0.85 * num
  return no_tax/2

halved = [halve(price) for price in prices]

print(halved)

