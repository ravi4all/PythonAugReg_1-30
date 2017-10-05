# a = []
#
# for i in range(101):
#     a.append(i)
#

# a = [i for i in range(101)]
# print(a)

# a = []
# for i in range(101):
#     if i%2 == 0:
#         a.append(i)
# print(a)

a = [i for i in range(101) if i%2 == 0]
print(a)
