f = open("a1.txt", 'w')
f.write("Metric Coder")
f.close()

f = open("a1.txt", 'a')
f.write(" Bangalore ")
f.close()

f = open("a1.txt", 'r')
content = f.read()
print(content)
f.close()