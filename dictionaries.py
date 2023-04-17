a = {
    "cycle": "ABC",
    "year": 1999
}

print(a)

#add
a["country"] = "India"
print(a)

print(a.get("country"))

print(a.keys())
print(a.values())

for x, y in a.items():
    print(x,y)

if "country" in a:
    print(True)
    
a.update({"year": 2000})
print(a)


a.popitem()
print(a)

a.clear()
print(a)