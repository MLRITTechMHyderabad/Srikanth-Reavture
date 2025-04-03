def sum(n):
    if n==1:
        return 1
    return n*sum(n-1)
# a=int(input("Enter a number: "))
a=9

print(sum(a))

def add(*a):
    sum=0
    for i in a:
        sum+=i
    return sum
a=(1,2,3,4,5,6,7,8,9)
print(add(*a))