#find all the sum of all multiples of 3 and 5
sum = 0
for x in range(0, 1000):
    if x % 5 == 0:
        sum+=x
        continue
    if x%3 == 0:
        sum+=x


print(sum)