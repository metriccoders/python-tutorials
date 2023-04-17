a = {"new", "old", 1, 2}
print(a)

print(len(a))

b = set((1,2,3))
print(b)

for x in b:
    print(x)
    
b.add(10)
print(b)

c = [89, 98]
b.update(c)
print(b)

b.remove(10)
print(b)

b.pop()
print(b)

b.clear()
print(b)

del b