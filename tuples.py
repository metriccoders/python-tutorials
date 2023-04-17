a = ('a',1)
print(a)

print(len(a))

b = (1,2,3)
print(b)

print(b[0])

print(b[:1])

print(b[0:])

if 1 in b:
    print(True)
else:
    print(False)
    
#unpacking tuples
x, y, z = b
print(x, y, z)


for i in b:
    print(i)
    
for i in range(len(b)):
    print(b[i])
    
i = 0
while i < len(b):
    print(b[i])
    i = i + 1
    
c = a + b
print(c)