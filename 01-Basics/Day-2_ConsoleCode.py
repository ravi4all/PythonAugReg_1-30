Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: E:\BMPL_Batches\Aug_2017\Regular\Python\Python_1_30-3\CorePython\01-Basics\03-Strings.py 
p
pytho
>>> 
 RESTART: E:\BMPL_Batches\Aug_2017\Regular\Python\Python_1_30-3\CorePython\01-Basics\03-Strings.py 
p
pytho
p 
>>> 
 RESTART: E:\BMPL_Batches\Aug_2017\Regular\Python\Python_1_30-3\CorePython\01-Basics\03-Strings.py 
p
pytho
pp
>>> 
 RESTART: E:\BMPL_Batches\Aug_2017\Regular\Python\Python_1_30-3\CorePython\01-Basics\03-Strings.py 
p
pytho
pp
g
>>> 
 RESTART: E:\BMPL_Batches\Aug_2017\Regular\Python\Python_1_30-3\CorePython\01-Basics\03-Strings.py 
p
pytho
pp
g
python
>>> 
 RESTART: E:\BMPL_Batches\Aug_2017\Regular\Python\Python_1_30-3\CorePython\01-Basics\03-Strings.py 
p
pytho
pp
g
python
 programming
>>> 
 RESTART: E:\BMPL_Batches\Aug_2017\Regular\Python\Python_1_30-3\CorePython\01-Basics\03-Strings.py 
p
pytho
pp
g
python
 programming
 programming
>>> 
 RESTART: E:\BMPL_Batches\Aug_2017\Regular\Python\Python_1_30-3\CorePython\01-Basics\03-Strings.py 
p
pytho
pp
g
python
 programming
 programming
Traceback (most recent call last):
  File "E:\BMPL_Batches\Aug_2017\Regular\Python\Python_1_30-3\CorePython\01-Basics\03-Strings.py", line 17, in <module>
    print(word[100])
IndexError: string index out of range
>>> word
'python programming'
>>> word[2] = "B"
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    word[2] = "B"
TypeError: 'str' object does not support item assignment
>>> word.replace("python","Py")
'Py programming'
>>> word
'python programming'
>>> 
 RESTART: E:\BMPL_Batches\Aug_2017\Regular\Python\Python_1_30-3\CorePython\01-Basics\03-Strings.py 
p
pytho
pp
g
python
 programming
 programming
Traceback (most recent call last):
  File "E:\BMPL_Batches\Aug_2017\Regular\Python\Python_1_30-3\CorePython\01-Basics\03-Strings.py", line 17, in <module>
    print(word[100])
IndexError: string index out of range
>>> 
 RESTART: E:\BMPL_Batches\Aug_2017\Regular\Python\Python_1_30-3\CorePython\01-Basics\03-Strings.py 
p
pytho
pp
g
python
 programming
 programming
Traceback (most recent call last):
  File "E:\BMPL_Batches\Aug_2017\Regular\Python\Python_1_30-3\CorePython\01-Basics\03-Strings.py", line 19, in <module>
    word[2] = "B"
TypeError: 'str' object does not support item assignment
>>> 
 RESTART: E:\BMPL_Batches\Aug_2017\Regular\Python\Python_1_30-3\CorePython\01-Basics\03-Strings.py 
p
pytho
pp
g
python
 programming
 programming
18
>>> word
'python programming'
>>> word.find("python")
0
>>> word.find("y")
1
>>> word.find("h")
3
>>> word.isupper()
False
>>> word.islower()
True
>>> word.isalpha()
False
>>> a = "nitin"
>>> a[::-1]
'nitin'
>>> a == a[::-1]
True
>>> a = "niitin"
>>> a == a[::-1]
False
>>> 
