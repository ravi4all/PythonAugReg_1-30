Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def add(x,y):
	return x+y

>>> add(11,12)
23
>>> def show(disp):
	return disp

>>> show(")
     
SyntaxError: EOL while scanning string literal
>>> show("Hello")
'Hello'
>>> def msg():
	print("Print me also...")

	
>>> show(def msg():)
SyntaxError: invalid syntax
>>> show(msg)
<function msg at 0x0000029F2A70E730>
>>> def show(disp):
	return disp()

>>> show(msg)
Print me also...
>>> msg
<function msg at 0x0000029F2A70E730>
>>> msg()
Print me also...
>>> def outer():
	def inner():
		print("Inner Function")
	print("Outer Function")

	
>>> outer()
Outer Function
>>> def outer():
	def inner():
		print("Inner Function")
	print("Outer Function")
	inner()

	
>>> outer()
Outer Function
Inner Function
>>> def outer():
	def inner():
		print("Inner Function")
	print("Outer Function")
	return inner()

>>> outer()
Outer Function
Inner Function
>>> def outer():
	def inner():
		print("Inner Function")
	print("Outer Function")
	return inner

>>> outer()
Outer Function
<function outer.<locals>.inner at 0x0000029F29C03E18>
>>> x = outer()
Outer Function
>>> x
<function outer.<locals>.inner at 0x0000029F2A70E8C8>
>>> x()
Inner Function
>>> 
