n=int(input())
hours=int(n//3600)
minutes=int(n%3600)//60
sec=int(n%3600)%60
s=(hours%100)//10
d=(minutes%100)//10
f=(sec%100)//10
if hours%10==1 and s!=1:
    print(hours,"час", end=" ")
if 1<hours%10<5 and s!=1:
    print(hours,"часа", end=" ")
if hours%10>4 or s==1:
    print(hours,"часов", end=" ")
if minutes!=0:
    if minutes%10==1 and d!=1:
        print(minutes,"минута", end=" ")
    if 1<minutes%10<5 and d!=1:
        print(minutes,"минуты", end=" ")
    if minutes%10>4 or d==1:
        print(minutes,"минут", end=" ")    
if sec!=0:
    if sec%10==1 and f!=1:
        print(sec,"секунда", end=" ")
    if 1<sec%10<5 and f!=1:
        print(sec,"секунды", end=" ")
    if sec%10>4 or f==1:
        print(sec,"секунд", end=" ")    

