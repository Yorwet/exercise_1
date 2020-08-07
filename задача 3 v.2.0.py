useless_value=int(input())
list = input().split()
print(max(a for a in list if list.count(a) == max(map(list.count, list))))
