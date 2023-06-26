import re

str1 = [el.lower() for el in re.split('\W', input())]
str2 = [el.lower() for el in re.split('\W', input())]

if sorted(str1) == sorted(str2):
    print('equal')
else:
    print('different')