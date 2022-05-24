# p = type(range(5))
# print(p)


#
# def fun():
#     x  = 50
#     return x
# L = fun()
# print(L)

A = 5
def B():
    global A
    A = 4
B()
print(A)