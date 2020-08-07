n=int(input())
a=int(n//3600)
b=int(n%3600)//60
c=int(n%3600)%60
s=(a%100)//10
d=(b%100)//10
f=(c%100)//10
if a%10==1 and s!=1:
    print(a,"час", end=" ")
if 1<a%10<5 and s!=1:
    print(a,"часа", end=" ")
if a%10>4 or s==1:
    print(a,"часов", end=" ")
if b!=0:
    if b%10==1 and d!=1:
        print(b,"минута", end=" ")
    if 1<b%10<5 and d!=1:
        print(b,"минуты", end=" ")
    if b%10>4 or d==1:
        print(b,"минут", end=" ")    
if c!=0:
    if c%10==1 and f!=1:
        print(c,"секунда", end=" ")
    if 1<c%10<5 and f!=1:
        print(c,"секунды", end=" ")
    if c%10>4 or f==1:
        print(c,"секунд", end=" ")    

