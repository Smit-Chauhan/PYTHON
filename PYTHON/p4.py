def calculate(operator, x, y):
  if operator == "+":
    print(x + y)
  elif operator == "-":
    print(x - y)
  else:
    print(f"unknown: {operator}")

calculate("-", 30, 10)


