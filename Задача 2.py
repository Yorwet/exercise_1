n=int(input())
s=int(n)
for i in range(1,n+1):
    print (' ' * s, end="")
    print(str(i)*i)
    s=s-1
