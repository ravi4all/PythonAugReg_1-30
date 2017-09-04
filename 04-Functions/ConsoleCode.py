Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = "Hello"
>>> a*6
'HelloHelloHelloHelloHelloHello'
>>> for i in range(6):
	print("*" * (i+1))

	
*
**
***
****
*****
******
>>> 
>>> for i in reversed(range(6)):
	print("*" * (i+1))

	
******
*****
****
***
**
*
>>> def func1(a,b):
	print(a+b)

	
>>> func1()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    func1()
TypeError: func1() missing 2 required positional arguments: 'a' and 'b'
>>> func1(2,3)
5
>>> func1("Hello",3)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    func1("Hello",3)
  File "<pyshell#11>", line 2, in func1
    print(a+b)
TypeError: must be str, not int
>>> func1("Hello","World")
HelloWorld
>>> def one(x):
	print(x)

	
>>> def one(x):
	print(x)
	def two():
		return x + 1

	
>>> two()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    two()
NameError: name 'two' is not defined
>>> def one(x):
	print(x)
	def two():
		return x + 1
	two()

	
>>> one(1)
1
>>> def one(x):
	print(x)
	def two():
		print("Inside two")
		return x + 1
	two()

	
>>> one(11)
11
Inside two
>>> def one(x):
	
	def two():
		print("Inside two")
		return x + 1
	return two

>>> one(1)
<function one.<locals>.two at 0x00000206975ABAE8>
>>> x = one(1)
>>> x
<function one.<locals>.two at 0x00000206975ABBF8>
>>> x()
Inside two
2
>>> def one(x):

	def two():
		print("Inside two")
		return x + 1

	
>>> one(1)
>>> print(one(1))
None
>>> def one(x):

	def two():
		print("Inside two")
		return x + 1
	return two

>>> 
