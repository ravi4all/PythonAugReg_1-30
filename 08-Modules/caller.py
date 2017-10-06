import calc2

# print(calc.add(12,11))
# print(calc.sub(18,3))
# print(calc.mul(4,4))
# print(calc.div(10,2))

print("""
1. Add
2. Sub
3. Div
4. Mul
5. Quit
""")

userChoice = input("Enter your choice : ")

# todo = {
#     "1" : calc.add,
#     "2" : calc.sub,
#     "3" : calc.mul,
#     "4" : calc.div,
#     "5"  : quit
# }

# todo = {
#     "1" : calc2.calculator,
#     "2" : calc2.calculator,
#     "3" : calc2.calculator,
#     "4" : calc2.calculator,
#     "5"  : quit
# }

todo = {
    "1" : "+",
    "2" : "-",
    "3" : "/",
    "4" : "*",
    "5"  : quit
}

num_1 = input("Enter first number : ")
num_2 = input("Enter second number : ")

# result = todo.get(userChoice)(userChoice,num_1, num_2)

opr = todo[userChoice]

result = calc2.calculator(opr,num_1, num_2)

print(result)
