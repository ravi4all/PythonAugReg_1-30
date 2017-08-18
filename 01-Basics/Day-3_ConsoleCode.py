Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = [1,2,"Hello",10.5, True]
>>> for i in a:
	print(i)

	
1
2
Hello
10.5
True
>>> len(a)
5
>>> a[0]
1
>>> a[3]
10.5
>>> a[2:4]
['Hello', 10.5]
>>> b = a
>>> b
[1, 2, 'Hello', 10.5, True]
>>> b[0] = "Bye"
>>> b
['Bye', 2, 'Hello', 10.5, True]
>>> a
['Bye', 2, 'Hello', 10.5, True]
>>> a = (1,2,3,4,5)
>>> a
(1, 2, 3, 4, 5)
>>> for i in a:
	print(i)

	
1
2
3
4
5
>>> type(a)
<class 'tuple'>
>>> a[0]
1
>>> a[2]
3
>>> a[0] = "Hi"
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a[0] = "Hi"
TypeError: 'tuple' object does not support item assignment
>>> a = {"id":101, "name":"Ram", "age":23}
>>> a
{'id': 101, 'name': 'Ram', 'age': 23}
>>> a.id
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a.id
AttributeError: 'dict' object has no attribute 'id'
>>> a["id"]
101
>>> a["name"]
'Ram'
>>> a["age"]
23
>>> a["id"] = 102
>>> a
{'id': 102, 'name': 'Ram', 'age': 23}
>>> for i in a:
	print(i)

	
id
name
age
>>> for i in a.values():
	print(i)

	
102
Ram
23
>>> for i in a.items():
	print(i)

	
('id', 102)
('name', 'Ram')
('age', 23)
>>> a = [1,2,3,4,5,6,7]
>>> import random
>>> choice = random.choice(a)
>>> choice
5
>>> choice
5
>>> choice
5
>>> choice
5
>>> choice
5
>>> choice = random.choice(a)
>>> choice
4
>>> 
