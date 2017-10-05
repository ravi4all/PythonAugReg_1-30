Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = (1,3,4,6,8,12,34)
>>> a
(1, 3, 4, 6, 8, 12, 34)
>>> a[0]
1
>>> a[1:5]
(3, 4, 6, 8)
>>> a
(1, 3, 4, 6, 8, 12, 34)
>>> a[0] = "Hi"
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a[0] = "Hi"
TypeError: 'tuple' object does not support item assignment
>>> a
(1, 3, 4, 6, 8, 12, 34)
>>> sorted(a)
[1, 3, 4, 6, 8, 12, 34]
>>> 
