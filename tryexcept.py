a = 100

try:
    print(a)
except:
    print("Error")
else:
    print("Just print")
finally:
    print("Metric Coder")
    
try:
    print(b)
except NameError:
    print("Name error")
except:
    print("Error")
finally:
    print("Finally wow!")
    
if a > -1:
    raise Exception("Positive value...")