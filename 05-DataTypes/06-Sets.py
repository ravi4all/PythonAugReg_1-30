Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s = {2,3,4,5,7,1,22}
>>> type(s)
<class 'set'>
>>> s[0]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    s[0]
TypeError: 'set' object does not support indexing
>>> s.add(11)
>>> a
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> s
{1, 2, 3, 4, 5, 7, 11, 22}
>>> s.add(33)
>>> s
{1, 2, 3, 4, 5, 33, 7, 11, 22}
>>> d = {'id':101, 'name':'Ram', 'age':22, 'salary':12000, 'dept':'IT'}
>>> for i in d.items():
	print(i)

	
('id', 101)
('name', 'Ram')
('age', 22)
('salary', 12000)
('dept', 'IT')
>>> d['company'] = 'IBM'
>>> d
{'id': 101, 'name': 'Ram', 'age': 22, 'salary': 12000, 'dept': 'IT', 'company': 'IBM'}
>>> s
{1, 2, 3, 4, 5, 33, 7, 11, 22}
>>> x = {3,4,5,21,13,9}
>>> x
{3, 4, 5, 9, 13, 21}
>>> s
{1, 2, 3, 4, 5, 33, 7, 11, 22}
>>> s.difference(x)
{1, 2, 33, 7, 11, 22}
>>> x.difference(s)
{9, 21, 13}
>>> s.intersection(x)
{3, 4, 5}
>>> s.union(x)
{1, 2, 3, 4, 5, 33, 7, 9, 11, 13, 21, 22}
>>> s.update(99)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s.update(99)
TypeError: 'int' object is not iterable
>>> s.update({99})
>>> s
{1, 2, 3, 4, 5, 33, 7, 99, 11, 22}
>>> 
