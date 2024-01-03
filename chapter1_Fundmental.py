Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
1 + 1
2
import sys
sys.exit()
1 + 2
3
 3 / 2.4
 
SyntaxError: unexpected indent
3 / 2.4
1.25
 3* 9
 
SyntaxError: unexpected indent
3*9
27
a=1
b=2
a+b
3
a=100;
b=200;
a+b
300
33 + 55
88
33 + 55 =
SyntaxError: incomplete input
33 + 55 = 123
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
a = 33+55
a
88
a = "Python"
a
'Python'
print(a)
Python


print('Hello, world')
Hello, world
>>> a='Hello, world'
>>> a
'Hello, world'
>>> print(a)
Hello, world
>>> 
>>> a=3
>>> if a > 1:
...     print('a는 1보다 큽니다.')
... 
...     
a는 1보다 큽니다.
>>> 
>>> for a in [1,2,3]:
...     print(a)
... 
...     
1
2
3
>>> 
>>> i=0
>>> while i < 3:
...     i=i+1
...     print(i)
... 
...     
1
2
3
>>> 
>>> def add(a,b):
...     return a+b
... 
>>> add(3,4)
7
>>>

7 * 5 / 2
17.5
Hello, world
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    Hello, world
NameError: name 'Hello' is not defined
print("Hello, wordl")
Hello, wordl
print("Hello, world")
Hello, world
print('Hello, world')
Hello, world

print(3+5)
8
print('3 + 5 = ', 3+5)
3 + 5 =  8

#연습문제 1-1

[문제1] 현대빈
print("[문제1] 현대빈")

>>> print("[문제2] 1~10 사이의 결과는 = ", 1+2+3+4+5+6+7+8+9+10)
[문제2] 1~10 사이의 결과는 =  55
>>> 
>>> print("[문제3] 2의 5승을 구하여 출력하세요. 결과는 = ", 2*2*2*2*2)

i=0
sum=0

while i < 10:
    i=i+1
    sum=sum+i

print(sum)

[문제3] 2의 5승을 구하여 출력하세요. 결과는 =  32
>>> 
>>> print("[문제4] 5-(3-1)을 구하여 출력하세요. 결과는 = ", 5-(3-1))
print("5-(3-1) = ", 5-(3-1)) 

[문제4] 5-(3-1)을 구하여 출력하세요. 결과는 =  3
>>> 
>>> print("[문제4] 5 / 2을 구하여 출력하세요. 결과는 = ", 5 / 2)
[문제4] 5 / 2을 구하여 출력하세요. 결과는 =  2.5
>>> print("[문제5] 5 * 2을 구하여 출력하세요. 결과는 = ", 5 * 2)
[문제5] 5 * 2을 구하여 출력하세요. 결과는 =  10
>>> 
>>> v1 = 25
>>> v2 = 30
>>> print(v1 + v2)
55
>>> 
>>> x = 3 * 50
>>> y = x + 120
>>> print("y의 값은 = ", y)
y의 값은 =  270
>>> 

[연습문제 01-2]
>>> print(r)
8
>>> x = 2 * 2 * 2
>>> print(x)
8
>>> y = x / 4
>>> print(y)
2.0
>>> z = y * y
>>> print(z)
4.0

x, y = 121, 797
x
121
y
797


