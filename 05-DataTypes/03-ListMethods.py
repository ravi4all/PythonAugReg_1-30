Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = [12,34,45,67,78,80]
>>> b = a[:]
>>> b
[12, 34, 45, 67, 78, 80]
>>> a
[12, 34, 45, 67, 78, 80]
>>> a = [12,34,45,67,78,80,['Hi','Hello','Bye']]
>>> a
[12, 34, 45, 67, 78, 80, ['Hi', 'Hello', 'Bye']]
>>> b = a[:]
>>> a[6][0] = 'Python'
>>> a
[12, 34, 45, 67, 78, 80, ['Python', 'Hello', 'Bye']]
>>> b
[12, 34, 45, 67, 78, 80, ['Python', 'Hello', 'Bye']]
>>> import copy
>>> c = copy.deepcopy(a)
>>> a
[12, 34, 45, 67, 78, 80, ['Python', 'Hello', 'Bye']]
>>> c
[12, 34, 45, 67, 78, 80, ['Python', 'Hello', 'Bye']]
>>> a[6][0] = 'Hi'
>>> a
[12, 34, 45, 67, 78, 80, ['Hi', 'Hello', 'Bye']]
>>> c
[12, 34, 45, 67, 78, 80, ['Python', 'Hello', 'Bye']]
>>> b
[12, 34, 45, 67, 78, 80, ['Hi', 'Hello', 'Bye']]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a
[12, 34, 45, 67, 78, 80, ['Hi', 'Hello', 'Bye']]
>>> a = [12, 34, 45, 67, 78, 80,11,23,9,31]
>>> sorted(a)
[9, 11, 12, 23, 31, 34, 45, 67, 78, 80]
>>> sorted(a, reverse = True)
[80, 78, 67, 45, 34, 31, 23, 12, 11, 9]
>>> 31 in a
True
>>> 13 in a
False
>>> 13 not in a
True
>>> a
[12, 34, 45, 67, 78, 80, 11, 23, 9, 31]
>>> b = a
>>> a is b
True
>>> b = a[:]
>>> b
[12, 34, 45, 67, 78, 80, 11, 23, 9, 31]
>>> a
[12, 34, 45, 67, 78, 80, 11, 23, 9, 31]
>>> a is b
False
>>> a == b
True
>>> a = "Hello"
>>> a[:]
'Hello'
>>> b = a[:]
>>> a = "10"
>>> b = 10
>>> a == b
False
>>> a is b
False
>>> len(a)
2
>>> a = [12, 34, 45, 67, 78, 80, 11, 23, 9, 31]
>>> len(a)
10
>>> del(a[2])
>>> a
[12, 34, 67, 78, 80, 11, 23, 9, 31]
>>> a.clear()
>>> a
[]
>>> a = [12, 34, 45, 67, 78, 80, 11, 23, 9, 31]
>>> a.append('Hi')
>>> a
[12, 34, 45, 67, 78, 80, 11, 23, 9, 31, 'Hi']
>>> a.insert('Hello',0)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    a.insert('Hello',0)
TypeError: 'str' object cannot be interpreted as an integer
>>> a.insert(0,'Hello')
>>> a
['Hello', 12, 34, 45, 67, 78, 80, 11, 23, 9, 31, 'Hi']
>>> b
10
>>> a.extend([99,98,97])
>>> a
['Hello', 12, 34, 45, 67, 78, 80, 11, 23, 9, 31, 'Hi', 99, 98, 97]
>>> a.remove(0)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a.remove(0)
ValueError: list.remove(x): x not in list
>>> a.remove(12)
>>> a
['Hello', 34, 45, 67, 78, 80, 11, 23, 9, 31, 'Hi', 99, 98, 97]
>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> a = [34, 45, 67, 78, 80, 11, 23, 9, 31,99, 98, 97]
>>> a.sort()
>>> a
[9, 11, 23, 31, 34, 45, 67, 78, 80, 97, 98, 99]
>>> 
