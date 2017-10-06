# def calculator(ch,x,y):
#     if ch == "1":
#         return x+y
#     elif ch == "2":
#         return x-y
#     elif ch == "3":
#         return x/y
#     elif ch == "4":
#         return x*y
#     else:
#         quit()


def  calculator(opr,x,y):
    return eval(x+opr+y)
