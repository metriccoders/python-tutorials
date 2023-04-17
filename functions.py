def fun_1():
    print("Metric Coder")

fun_1()

def fun_2(a, b):
    print(a, b)

fun_2(10, 20)

def fun_3(*a):
    for x in a:
        print(x)
        
fun_3(1, "a", 3)

def fun_3(**a):
    for x in a:
        print(x, a[x])
        
fun_3(k = 1, l = "a", m = 3)


def fun_4(a = 3):
    print(a)
    
    
fun_4()
fun_4(20)

def fun_5():
    return 10

x = fun_5()
print(x)