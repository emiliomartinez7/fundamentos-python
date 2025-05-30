lst = (input())
lst = [int(x) for x in str(lst).split()]
dups = set(lst)
no_dups = []
for i in lst:
    if i not in no_dups:
        no_dups.append(i)
    
print(*no_dups)
