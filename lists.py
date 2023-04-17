a = [10,20,30,40,50, "ABC", True, 2.09, 3j]

print(a)

print(len(a))

print(type(a))

print(a[0])

print(a[-1])

print(a[2:7])

print(a[3:])


print(a[:4])


if 205 in a:
    print(True)
else:
    print(False)
    
    
a.insert(2,350)

print(a)


a.append(600)

print(a)


b = [1.8, 2.8]
a.extend(b)
print(a)

a.remove(1.8)

print(a)

a.pop()
print(a)

a.pop(2)
print(a)

#looping through a list
for x in a:
    print(x)

#looping through index
for i in range(len(a)):
    print(a[i])
    
i = 0
while i < len(a):
    print(a[i])
    i = i + 1
    
#list comprehension
print("List Comprehension")
[print(x) for x in a]


a.clear()
print(a)
#delete the list completely
del a