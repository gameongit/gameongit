Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> updates={'GTA5 10.3.1.2':2013,'GTA5 12.4.4.5':2016,'GTA5 17.8.23.8':2023}
>>> for key,value in sorted(updates.items()):
...     print(key,value)
... 
...     
GTA5 10.3.1.2 2013
GTA5 12.4.4.5 2016
GTA5 17.8.23.8 2023
>>> print(sorted(updates))
['GTA5 10.3.1.2', 'GTA5 12.4.4.5', 'GTA5 17.8.23.8']
