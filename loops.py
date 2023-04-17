a = [1,2,3,4]

for x in a:
    print(x)
    
i = 0
while i < len(a):
    i = i + 1
    if i == 2:
        break
    elif i == 3:
        continue
    
    print(a[i])