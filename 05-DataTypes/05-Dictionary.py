Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> d = {'id':101,'name':'Ram'}
>>> d[0]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    d[0]
KeyError: 0
>>> d['id']
101
>>> d['id'] = 102
>>> d
{'id': 102, 'name': 'Ram'}
>>> d.keys()
dict_keys(['id', 'name'])
>>> d.values()
dict_values([102, 'Ram'])
>>> d.items()
dict_items([('id', 102), ('name', 'Ram')])
>>> for i in d:
	print(i)

	
id
name
>>> for i in d.items():
	print(i)

	
('id', 102)
('name', 'Ram')
>>> d.pop()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> d.pop('id')
102
>>> d
{'name': 'Ram'}
>>> 
