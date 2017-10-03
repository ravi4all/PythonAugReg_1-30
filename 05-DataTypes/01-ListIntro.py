Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 12
>>> type(a)
<class 'int'>
>>> a = "hello"
>>> type(a)
<class 'str'>
>>> id(a)
2772919930752
>>> a = [1,2,3,4,5,6]
>>> b = (1,2,3,4,5,6)
>>> a[0] = 'Hi'
>>> a
['Hi', 2, 3, 4, 5, 6]
>>> b[0] = 'Hi'
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    b[0] = 'Hi'
TypeError: 'tuple' object does not support item assignment
>>> a = []
>>> a = [12,10.5,'Hello','Python',76,11]
>>> b = a
>>> b
[12, 10.5, 'Hello', 'Python', 76, 11]
>>> a
[12, 10.5, 'Hello', 'Python', 76, 11]
>>> a[0] = 'Bye'
>>> a
['Bye', 10.5, 'Hello', 'Python', 76, 11]
>>> b
['Bye', 10.5, 'Hello', 'Python', 76, 11]
>>> id(a)
2772919806024
>>> id(b)
2772919806024
>>> a[:]
['Bye', 10.5, 'Hello', 'Python', 76, 11]
>>> a[0]
'Bye'
>>> a[1]
10.5
>>> a[-1]
11
>>> a[0:2]
['Bye', 10.5]
>>> a[0:3]
['Bye', 10.5, 'Hello']
>>> a[:-1]
['Bye', 10.5, 'Hello', 'Python', 76]
>>> a[::-1]
[11, 76, 'Python', 'Hello', 10.5, 'Bye']
>>> a[0:100]
['Bye', 10.5, 'Hello', 'Python', 76, 11]
>>> a[0:4:2]
['Bye', 'Hello']
>>> li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
>>> li[0:10:2]
[1, 3, 5, 7, 9]
>>> li[1:12:2]
[2, 4, 6, 8, 10, 12]
>>> li[1:12:3]
[2, 5, 8, 11]
>>> a[-2]
76
>>> a
['Bye', 10.5, 'Hello', 'Python', 76, 11]
>>> b
['Bye', 10.5, 'Hello', 'Python', 76, 11]
>>> b = a[:]
>>> id(a)
2772919806024
>>> id(b)
2772919855816
>>> a[0] = 111
>>> a
[111, 10.5, 'Hello', 'Python', 76, 11]
>>> b
['Bye', 10.5, 'Hello', 'Python', 76, 11]
>>> a = [111, 10.5, 'Hello', 'Python', 76, 11, [99,98,97,96,95],110,111]
>>> a
[111, 10.5, 'Hello', 'Python', 76, 11, [99, 98, 97, 96, 95], 110, 111]
>>> a[:]
[111, 10.5, 'Hello', 'Python', 76, 11, [99, 98, 97, 96, 95], 110, 111]
>>> a[6][0]
99
>>> b = a[:]
>>> b
[111, 10.5, 'Hello', 'Python', 76, 11, [99, 98, 97, 96, 95], 110, 111]
>>> a
[111, 10.5, 'Hello', 'Python', 76, 11, [99, 98, 97, 96, 95], 110, 111]
>>> a[6][0] = 'xyz'
>>> a
[111, 10.5, 'Hello', 'Python', 76, 11, ['xyz', 98, 97, 96, 95], 110, 111]
>>> b
[111, 10.5, 'Hello', 'Python', 76, 11, ['xyz', 98, 97, 96, 95], 110, 111]
>>> a[0] = 'Hi'
>>> a
['Hi', 10.5, 'Hello', 'Python', 76, 11, ['xyz', 98, 97, 96, 95], 110, 111]
>>> b
[111, 10.5, 'Hello', 'Python', 76, 11, ['xyz', 98, 97, 96, 95], 110, 111]
>>> a[6]
['xyz', 98, 97, 96, 95]
>>> a[6] = 'hiiii'
>>> a
['Hi', 10.5, 'Hello', 'Python', 76, 11, 'hiiii', 110, 111]
>>> b
[111, 10.5, 'Hello', 'Python', 76, 11, ['xyz', 98, 97, 96, 95], 110, 111]
>>> a = [111, 10.5, 'Hello', 'Python', 76, 11, ['xyz', 98, 97, 96, 95], 110, 111]
>>> a
[111, 10.5, 'Hello', 'Python', 76, 11, ['xyz', 98, 97, 96, 95], 110, 111]
>>> a[:][:]
[111, 10.5, 'Hello', 'Python', 76, 11, ['xyz', 98, 97, 96, 95], 110, 111]
>>> a[:][0:3]
[111, 10.5, 'Hello']
>>> a[:, 0:3]
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a[:, 0:3]
TypeError: list indices must be integers or slices, not tuple
>>> a[:,:]
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a[:,:]
TypeError: list indices must be integers or slices, not tuple
>>> 
