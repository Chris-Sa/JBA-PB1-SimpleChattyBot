
amount = int(input())
year = 0
limit = 700000
rate = 1.071
while amount < limit:
    amount *= rate
    year += 1

print(year)
