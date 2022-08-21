flights = ["1122", "5788", "0044"]


codes_a = ["BA" + flight for flight in flights]
print(codes_a)


codes_b = []
for flight in flights:
  code = "BA" + flight
  codes_b.append(code)

print(codes_b)

