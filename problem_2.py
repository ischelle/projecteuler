#find the sum of all even numbers in Fibonacci  sequence
a=0
b=1
c=0

sum=0
while c < 4000000:
    c = a + b
    a = b
    b = c
    if(c % 2 == 0):
        sum+=c

print(sum)