Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> fred = turtle.Pen()
>>> fred.shape("turtle")
>>> for i in range(4):
	fred.forward(100)
	fred.left(90)

	
>>> fred.reset()
>>> for i in range(10):
	fred.forward(100)
	fred.left(50)

	
>>> fred.reset()
>>> for i in range(10):
	fred.forward(100)
	fred.left(i*3)

	
>>> fred.reset()
>>> for i in range(10):
	fred.forward(i*5)
	fred.left(90)

	
>>> fred.reset()]
SyntaxError: invalid syntax
>>> fred.reset()
>>> for i in range(50):
	fred.forward(i*5)
	fred.left(90)

	
>>> fred.reset()
>>> for i in range(50):
	fred.circle(10)

	
Traceback (most recent call last):
  File "<pyshell#23>", line 2, in <module>
    fred.circle(10)
  File "C:\Python36-32\lib\turtle.py", line 1991, in circle
    self._go(l)
  File "C:\Python36-32\lib\turtle.py", line 1605, in _go
    self._goto(ende)
  File "C:\Python36-32\lib\turtle.py", line 3195, in _goto
    self._update() #count=True)
  File "C:\Python36-32\lib\turtle.py", line 2663, in _update
    screen._delay(screen._delayvalue) # TurtleScreenBase
  File "C:\Python36-32\lib\turtle.py", line 566, in _delay
    self.cv.after(delay)
  File "C:\Python36-32\lib\tkinter\__init__.py", line 741, in after
    self.tk.call('after', ms)
KeyboardInterrupt
>>> fred.reset()
>>> for i in range(50):
	fred.circle(10)
	fred.left(10)

	
>>> fred.reset()
>>> for i in range(50):
	fred.circle(i*3)
	fred.left(50)

	
>>> fred.reset()
>>> fred.speed(0)
>>> for i in range(50):
	fred.circle(i*3)
	fred.left(50)

	
>>> fred.speed(0)
>>> fred.reset()
>>> fred.speed(0)
>>> for i in range(50):
	fred.circle(i*3)
	fred.left(i*10)

	
>>> fred.reset()
>>> fred.speed(0)
>>> for i in range(50):
	fred.forward(i*10)
	fred.left(135)
	fred.forward(i*5)
	fred.left(90)
	fred.forward(i*6)

	
>>> 
