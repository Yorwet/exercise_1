size=int(input())
numer = [int(i) for i in input().split()]
dict_counts = {}
for p in numer:
    if p not in dict_counts:
        dict_counts[p] = 1
    else:
        dict_counts[p] += 1
maxp = 0
mode_num = None
for k, v in dict_counts.items():
    if maxp < v:
        maxp = v
        mode_num = k
print(mode_num)