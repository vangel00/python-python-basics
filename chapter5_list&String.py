#  변수 사용법과 입출력 배우기

# 1) var1 이름의 변수를 만들고 10의 값을 할당하세요
var1 = 20
print(var1)

# 2) var2 이름의 변수를 만들고 20의 값을 할당하세요
var2 = 20
print(var2)


# 3) 다양한 연산자 사용하기

print(var1 + var2)
print(var1 * var2)
print(var1 / var2)

var1 = 100
var2 = 200
var3 = var1 + var2
print(var3)

# 4)  % 연산자 활용하기

var5 = 3
var6 = 14
print(var6 % var5)


# 5) print( ) 함수 사용하기

# 출력할 문장을 직접 쓰기
print("오늘도 굿모닝이지 말입니다!")

# 출력할 문장을 변수에 넣고 변수값 출력하기
str = "내일도 굿모닝이지 말입니다!"
print(str)


# 6) 리터럴 문자와 함께 사용하기
hungry = 5
print(' 배가 무지 고파서 밥을 %s 그릇도 먹겠네!' %hungry)


# 7) 특수문자와 함께 사용해야 할 경우

up = 20
print(' 뉴스에서 물가가 %s %%까지 오른다는데....'  %up)


# 8) 여러개의 변수를 한꺼번에 사용할 경우

up = 20
sal = 10

print('뉴스에서 물가는 %s %% 오른다는데 내 월급도 %s %%라도..'  %(up , sal))


# 9) input( ) 함수로 정보 입력받기

txt1 = input()


# 10) input() 함수에서 안내 멘트 보이기
txt2 = input('점심 뭐 드셨어용?')


# 11) 출력 되는 양식을 지정하여 정보를 입력받기

area_no = input('''
1. 서울         2.대전           3.광주           4.부산
5. 경남         6.경북           7.충청           8.제주

위 지역중 정보를 조회할 지역의 번호를 입력하세요: ''')


=====  데이터 유형과 함수 =====

##### 파이썬에서 산술 연산자를 사용하는 예

#더하기
print("1.더하기 예 : 2 + 4 = " , 2 + 4)

#빼기
print("2.빼기 예 : 4 - 2 = " , 4 - 2 )

#곱하기
print("3.곱하기 예 : 4 X 2 = " , 4 * 2)

#나누기
print("4.나누기 예 : 4 / 2 = " , 4 / 2)

#나누기에서 몫 만 출력하기
print("5.나누기에서 몫만 출력하기 예 : 4 // 2 = " , 4 // 2)

#나누기에서 나머지값만 출력하기
print("6.나누기에서 나머지값만 출력하기 예 : 4 % 2 = ", 4 % 2)

# 주어진 숫자의 승수값 출력하기
print("7.주어진 숫자의 승수값 출력하기 예 : 4 ** 2 = " , 4**2)



# 연산자 사용 방법
# Case 1
i = 0
i = i + 2
print("i 에 저장된 값은 %s 입니다" %i)

# Case 2
j = 0
j += 3
print("j 에 저장된 값은 %s 입니다" %j)


# 정수형으로 변환하기 - 변환하기 전 

no1 = input("첫번째 숫자 입력: ")
no2 = input("두번째 숫자 입력: ")

print('''첫번째 숫자는 %s 이고 두번째 숫자는 %s 이며
두 숫자의 합은 %s 입니다''' %( no1, no2 , no1+no2 ) )


# 정수형으로 변환하기 - 변환 후

no1 = int( input("첫번째 숫자 입력: ") )
no2 = int( input("두번째 숫자 입력: ") )

print('''첫번째 숫자는 %s 이고 두번째 숫자는 %s 이며
두 숫자의 합은 %s 입니다''' %( no1, no2 , no1+no2 ) )


# 실수형 숫자 타입

print("정수형 숫자 타입:", int(1) )
print("실수형 숫자 타입:", float(1) )



# 숫자 타입에서 많이 사용되는 주요 함수
#a) round( ) - 반올림 함수

no1 = 3.45678
no2 = 3.56789
print("원래값: %s , 반올림후 값: %s" %(no1 , round(no1) ) )
print("원래값: %s , 반올림후 값: %s" %(no2 , round(no2) ) )



# 숫자 타입에서 많이 사용되는 주요 함수
#a) round( ) - 반올림 함수의 소수점 이하 자리수 지정

no1 = 3
no2 = 5
print("반올림하기 전 원래값:", no2 / no1)
print("소수 첫째자리까지 반올림하기:", round(no2 / no1,1) )
print("소수 둘째자리까지 반올림하기:", round(no2 / no1,2) )


x = float(input("첫번째 숫자 입력: "))
y = float(input("두번째 숫자 입력: "))

print("원래값: %d, 반올림후값: %d", x, round(x))
print("원래값: %d, 반올림후값: %d", y, round(y))

첫번째 숫자 입력: 123.45
두번째 숫자 입력: 345.67
원래값: %d, 반올림후값: %d 123.45 123
원래값: %d, 반올림후값: %d 345.67 346


x = float(input("첫번째 숫자 입력: "))
y = float(input("두번째 숫자 입력: "))

sum = x + y
print(sum)

print("원래값: %d, 반올림후값: %d", x, round(x))
print("원래값: %d, 반올림후값: %d", y, round(y))

sum = round(x) + round(y)

print(sum)


# 숫자 타입에서 많이 사용되는 주요 함수
#b) trunc() - 버림 함수
import math

no1 = 3
no2 = 5
print("버림하기 전 원래값:", no2 / no1)
print("소수 첫째자리까지 버림하기:", math.trunc(no2 / no1) )

import math

x = float(input("첫번째 숫자 입력: "))
y = float(input("두번째 숫자 입력: "))

sum = x + y
print(sum)

print("원래값: %d, 반올림후값: %d", x, math.trunc(x))
print("원래값: %d, 반올림후값: %d", y, math.trunc(y))

sum = math.trunc(x) + math.trunc(y)

print(sum)


# 숫자 타입에서 많이 사용되는 주요 함수
#c) ceil() - 큰 정수 찾기 함수

import math

count = int(input("게시물 총 수를 입력해 주세요: "))

# 페이지 넘버링
# 한 페이지에 15건의 게시물이 존재한다고 가정 합니다. 

pageCount = math.ceil(count / 15)

print("총 %d 페이지의 데이터를 수집해야 합니다.", pageCount)



# 숫자 타입에서 많이 사용되는 주요 함수
#d) floor() - 작은 정수 찾기 함수
import math

no1 = 4.9
no2 = 4.1

print("%s 보다 작으면서 가장 가까운 정수는 %s 입니다" %(no1 , math.floor(no1)))
print("%s 보다 작으면서 가장 가까운 정수는 %s 입니다" %(no2 , math.floor(no2)))

import math

count = int(input("게시물 총 수를 입력해 주세요: "))

# 페이지 넘버링
# 한 페이지에 15건의 게시물이 존재한다고 가정 합니다. 

pageCount = math.floor(count / 15)

print("총 %d 페이지의 데이터를 수집해야 합니다.", pageCount)


# 2. 문자열 유형
# 2) 인덱싱과 슬라이싱

#indexing
# python의 모든 변수는 객체이다.

str = input("게시물 총 수를 입력해 주세요: ")

print(str) # 안녕하세요...
print(str[0]) # 안
print(str[1]) # 녕

# 슬라이싱 예제

str2 = input("인사말을 입력해 주세요: ")

#             0 1 2 3 4 567
print(str2) # 안녕하세요...

print(str2[2:4]) #하세 

print(str2[0:5]) # 안녕하세요

print(str2[0:8]) # 안녕하세요...


# 슬라이싱 예제 2, slicing

str2 = input("인사말을 입력해 주세요: ")

#             0 1 2 3 4 567
print(str2) # 안녕하세요...

print(str2[2:4]) #하세 

print(str2[0:5]) # 안녕하세요

print(str2[0:8]) # 안녕하세요...

print(str2[0: ]) # 안녕하세요...

print(str2[ : 8]) # 안녕하세요...


# count 함수 
a = "hobby"
a
'hobby'
a.count('b')
2

# find 함수 
a = "python is the best choice"
a.find('b')
14
a.find('k')
-1

# index 함수
a = "python is the best choice"
print(a.index('b')) #14
print(a.index('k'))

#Traceback (most recent call last):
  File "D:\python\1.python.py", line 24, in <module>
    print(a.index('k'))
ValueError: substring not found

# join 함수
print(",".join('abcd'))
# a,b,c,d


# [ lower( ) 함수 / upper( ) 함수 ] 

str2 = "PyThoN"  # 대소문자가 섞여 있습니다
print(str2.lower())
print(str2.upper( ))


# [ lstrip( ) / rstrip( ) / strip( ) ] 
# 왼쪽공백 지우기, 오른쪽 공배 지우기, 양쪽공백지우기

str3 = "    <- 이쪽 끝에 공백 있었어요"
str4 = "오른쪽 끝에 공백 있었어요->    "
str5 = "   <- 양쪽 끝에 공백 있었어요 ->   "

print( str3.lstrip( ) ) #"이쪽 끝에 공백 있었어요"
print( str4.rstrip( ) ) #"    이쪽 끝에 공백 있었어요"
print( str5.strip( ) )


#[ replace( ) ] 
str6 = '새우깡도 해산물 인가요?'
print(str6.replace("새우깡" , "새우"))


#[ split( ) ] 

tel = '02-1234-5678'
print(tel.split()) #공백이 있다면 문자열 분리
print(tel.split('-'))
print(tel.split('-',1))



#[ len() ]

str1 = '파이썬 완전 좋아요'
str2 = ['파이썬','웹크롤러','가치랩스']

print(len(str1))
print(len(str2))



# 문자열로 연산하기

print("=" *80)
print("문자열로 연산하기 실습")
print("+" *80)



#문자열 관련 함수(문자열 내장함수)
#문자 객수 세기 : count()

a = "hobbyhobbyhobby"
print(a.count('b')) # 6

a = "Python is the best choice"
print(a.find('b')) # 14

print(a.find('k')) # -1, 틀림을 알려주는 메시지로 주로 사용합니다.

#결과 메시지에 대하여
# 0 : 정상 처리 되었음을 알려줍니다.
# 1, 100, 1000, 999 :
# -1 : 비정상 처리중임을 알려줍니다.
      
#index
a2 = "Life is too short"
print(a2.index('t')) # 8

#print(a2.index('k')) # Error 발생

#문자열 삽입(join)

print(",".join('abcd')) # a,b,c,d

print(",".join(['a','b','c','d'])) # a,b,c,d

print(",".join(['abb','bcc','cdd','dee'])) # abb,bcc,cdd,dee

print("/".join(['abb','bcc','cdd','dee'])) # abb/bcc/cdd/dee

print("$".join(['abb','bcc','cdd','dee'])) # abb$bcc$cdd$dee

# python syntax 적용에는 조금씩 2.X와 3.x의 차이가 있습니다.

# 소문자를 대문자로 변환하기
a = "hi Phython"
print(a.upper()) # HI PHYTHON

# 대문자를 소문자로 변환하기
a = "HI PHYTHON"
print(a.lower()) # hi phython

# 문자열 변경(replace)
a = "Life is too short"
print(a.replace("Life", "Your leg"))

# 공백 지우기
#좌측 공백 지우기
a = " hi "
print(a.lstrip())

b = " hi "
#우측 공백 지우기
print(b.rstrip())

c = " hi "
#양쪽 공백 지우기
print(c.strip())


c = " hi  hi hi "
#좌.우측 공백 지우기
print(c.strip()) #hi  hi hi

#문자열 나누기(split)
a = "Life is too short"
print(a.split()) #['Life', 'is', 'too', 'short']

a = "Life:is:too:short"
print(a.split(':')) #['Life', 'is', 'too', 'short']

a = "Life?is?too?short"
print(a.split('?')) #['Life', 'is', 'too', 'short']

a = "Life*is*too*short"
print(a.split('*')) #['Life', 'is', 'too', 'short']

a = "Life*?/ is*?/ too*?/ short"
print(a.split('*?/ ')) #['Life', 'is', 'too', 'short']

a = "Life*?/ is*?too/ short"
print(a.split('*?/ ')) #['Life', 'is*?too/ short']


# 여기까지가 [문자열 자료형]에 대한 내용입니다.
============================================


# # List형 데이터 처리

for i in [10, 20, 30]:
    print(i)


for i in [100, 200, 300]:
    print(i, end = '_')


for i in [100, 200, 300]:
    print(i, end = ' ') # 1020304050


for i in [100, 200, 300]:
    print(i, end = ', ') # 10, 20, 30, 40, 50, 


a = [1,2,3,['a','b','c']]
a
[1, 2, 3, ['a', 'b', 'c']]
a[0]
1
a[1]
2
a[2]
3
a[3][0]
'a'
a[3][1]
'b'
a[3][2]
'c'

a = [1,2,3,['a','b','c',['Life', 'is', 'hyun']]]
a
[1, 2, 3, ['a', 'b', 'c', ['Life', 'is', 'hyun']]]
a[0]
1
a[1]
2
a[2]
3
a[3][0]
'a'
a[3][1]
'b'
a[3][2]
'c'
a[3][3][0]
'Life'
a[3][3][1]
'is'
a[3][3][2]
'hyun'



x = 35
type(x)


x2 = 35.56
type(x2)


for i in [10,20,30,40,50]:
    print(i, end='_ ')
    print(type(i))

    
for i in [10.1,20.2,30.3,40.4,50.5]:
    print(i, end='_ ')
    print(type(i))

for i in [10.1,20.2,30,40,'hyun']:
    print(i, end='_ ')
    print(type(i))


x3 = '500'
sum = eval(x3) + 500
print(sum)
type(eval(x3))


'Happy'

str = 'Happy'
type(str)



# List형 데이터 처리
[10, 20, 30] 

type([10, 20, 30] )


x4 = [10, "hello", 3.3]
print(x4)
type([10, "hello", 3.3])


a = [1,2,3,['a','b','c'], 4,5]
print(a[2:5]) # [3, ['a', 'b', 'c'], 4]
print(a[3][ :2]) # ['a', 'b']



# Indexing Operation
b = [1, 2, 3] + [4, 5]
print(b)  # [1, 2, 3, 4, 5]


#    0  1  2
x = [1, 2, 3]
#    0  1
y = [4, 5]
z = x + y
z


# 반복하여 데이터를 생성하기
bb = [1, 2, 3, 40] * 5
print(bb)
# [1, 2, 3, 40, 1, 2, 3, 40, 1, 2, 3, 40, 1, 2, 3, 40, 1, 2, 3, 40]


# [ ] : Indexing Operation
# [  :  ] : Slicing Oparation
# 파이썬에서는 변수도 객체 입니다.
#     0   1    2   3   4
st = [10, 20, 30, 40, 50]
n1 = st[0] # 10
n2 = st[4] # 50
print(n1, n2)

str = [10, 20, 30, 40, 50]
sum = str[0] + str[4]
print(sum) # 60



str = [10, 20, 30, 40, 50]
x = str[0] = 100
y = str[4] = 500

sum = x + y
print(sum)



#     0  1  2  3  4
st = [1, 2, 3, 4, 5]
print(st)

st[0] = 500 # 500저장 
st[4] = 100 # 100저장 
print(st) # [500, 2, 3, 4, 100]

print(st[0]) 
print(st[1])
print(st[2])
print(st[3])
print(st[4])
print(st[0], st[1], st[2], st[3], st[4])


print(st[-1])
print(st[-2])
print(st[-3])
print(st[-4])
print(st[-5]) # [100, 4, 3, 2, 500]


x = 3
y = 4
print(x + y)
print(x - y)
print(x * y)
print(x ** 3) # 3*3*3 = 27


x = 123.12
y = 12.12
print( x / y)
print( x % y)

x2 = 123.12
y2 = 12.12
print(x2 // y2)
print(x2 % y2)



#연습문제 5-1
#[문제1]
st = [11, 12, 13, 14]
print(st[0], st[1], st[2], st[3])
print(st)


for i in [11, 12, 13, 14]:
    print(i, end = ', ') 

#[문제2]
st = [11, 12, 13, 14]
print(st[-1], st[-2], st[-3], st[-4])


for i in [100, 200, 300]:
    print(i.reverse(), end = ', ') 

st.reverse()
print(len(st))

#[문제3]
st = [11, 12, 13, 14]
st[0] += 1
st[1] += 1
st[2] += 1
st[3] += 1

print(st)
print(type(st))
#방안1
print(st[0] + 1, st[1] + 1, st[2] + 1, st[3] + 1)


#[문제4]

st = [11, 12, 13, 14]

for i in range(len(st)): # 0 ~ 4
    st[i] += 1
print(st) # [12, 13, 14, 15]


#[문제5]

x = [1,2,3,['a','b','c']]
print(a)

print('첫번째 데이터 : ', x[0]) # 1
print('두번째 데이터 : ', x[1]) # 2
print('세번째 데이터 : ', x[2]) # 3
print('네번째 데이터 : ', x[3]) # ['a','b','c']
print('네번째 데이터 : ', x[-1]) # ['a','b','c']

print('네번째 데이터 : ', x[-1][0]) # 'a'
print('네번째 데이터 : ', x[-1][1]) # 'b'
print('네번째 데이터 : ', x[-1][2]) # 'c'

print('네번째 데이터 : ', x[3][0]) # 'a'
print('네번째 데이터 : ', x[3][1]) # 'b'
print('네번째 데이터 : ', x[3][2]) # 'c'

문제6> 위 데이터를 거꾸로 출력하세요.

print('x[-1][0] = ', x[-1][0])
print('x[-1][1] = ', x[-1][1])
print('x[-1][2] = ', x[-1][2])

x.reverse()
x[0].reverse()
print(x[0][0])
print(x[0][1])
print(x[0][2])
print(x[1])
print(x[2])
print(x[3])


문제7>
# 3차원 배열 
#     0  1  2    3,0 3,1 3,2     3,3,0   3,3,1   3,3,2
x2 = [1, 2, 3, ['a', 'b', 'c', ['hyun', 'kim', 'park']]]

print(x2) # [1, 2, 3, ['a', 'b', 'c', ['hyun', 'kim', 'park']]]

print(x2[0])
print(x2[1])
print(x2[2])
#print(x2[0][0]) #[표현불가]
#print(x2[0][0][0]) #[표현불가]

print(x2[3][0])
print(x2[3][1]) 
print(x2[3][2]) 

# 3차원 배열 출력 
print(x2[3][3][0])
print(x2[3][3][1]) 
print(x2[3][3][2]) 


# 배열이란?
# 특정 조건을 만족하는 특정 데이터의 집합
# - 데이터의 자료형이 같아야 합니다.
# - 데이터의 갯수가 많아야 합니다.
# - fruits[5500]: 수백내지는 수천개의 데이터
#    [0] ~ [5499]의 인덱스(index) : address(pointer)
#    [0] : first element
#    [1] : second element
#    [2] : threed element
#           ~
#    [5499] : last element
# - 1차원 배열[ ] : 행과 열이 같습니다.
# - 2차원 배열[ ][ ] : 행과 열이 다릅니다. 열중심 언어
# - 3차원 배열[ ][ ][ ] : 면, 행, 열이 각각 존재 합니다.
# - 4차원 배열[ ][ ][ ][ ] : 시간과 공간 
# 메모리 사용: 주소(번지) : 공간 = 변수 (데이터를 저장)

# listname = [ element1, 2,.....]
odd = [10, 30, 50, 70, 90]
print(odd)

a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

#list의 indexing
#   a[0]  a[1]  a[2]  a[3]  a[4]
a = [1,    2,    3,   4,     5]
# a = a변수 = a배열 = a배열 객체 = a 객체 = a index 

print(a) # [1,2,3]

print('첫번째 데이터 : ', a[0]) # 1
print('두번째 데이터 : ', a[1]) # 2
print('세번째 데이터 : ', a[2]) # 3
print('네번째 데이터 : ', a[3]) # 4
print('다섯번째 데이터 : ', a[4]) # 5

print('a 배열의 연산은 : ', a[0] + a[2]) # 1 + 3 = 4

print(a[-1]) # 5




#삼중리스트에서 인덱싱하기
#     [0]    [1]      [2]
x = [1, 2, ['a','b',['Life', 'is']]]
print(x)

print(x[0]) # 1
print(x[1]) # 2

print(x[2][0]) # 'a'
print(x[2][1]) # 'b'

print(x[2][2][0]) # 'Life'
print(x[2][2][1]) # 'is'


#Slicing 연산

# [  :  ] =>  : 범위지정 연산자 

# python은 열 중심 언어
#[0] 
#[1]
#[2]

#[0][0]
#[1][0]
#[2][0]
#[0][0][0]
#[1][0][0]
#[2][0][0]


문제8>
# indexing
#     [0]  [1]   [2]  [3]  [4]                                [9]
st1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
st2 = st1[2:5] # 데이터를 st1 객체에서 불어오기: n-1
print(st2) #  300, 400, 500

st1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

st1[2:5] = [0, 0, 0, 0, 0] # insert시에는 n

print(st1) #  [100, 200, 0, 0, 0, 0, 0, 600, 700, 800, 900, 1000]
#데이터의 부분수정 

x = [10, 20, 30, 40, 50]
print(x[0:2]) # [10, 20]

x2 = "12345"
print(x2[0:2]) # 12



# 리스트 자료형(List DataType)

# 열 중심 일 경우 : Python
#[0]
#[1]
#[2][0]
#[2][1]
#[2][2][0]
#[2][2][1]

#행 중심 일 경우 
#[0][1]  => 1차원(a)
#[2][0][2][1] => 2차원(b)
#[2][2][0][2][2][1] => 3차원 (c)

#List의 Sliceing(: 범위지정 연산자) => c++
a = [1,2,3,4,5]
print(a[0:2]) #[1,2]

a = "12345"
print(a[0:2]) # '12'

a = [11, 22, 33, 44, 55]
b = a[:2] # 0 ~ 1까지 ...a[0], a[1]...
c = a[2:] # 2 ~ 끝가지 ... a[2] ~ a[4]....
print(b) #[11, 22]
print(c) #[33, 44, 55]

#중첩 리스트에서 슬라이싱하기
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5]) # [3, ['a', 'b', 'c'], 4]
print(a[3][:2]) # ['a', 'b']

#배열에서는 항상 인덱싱을 -1하여 처리합니다.
# a[2][3][4] => a[1][2][3]
# a[3][4] => a[2][3]
# a[5] => a[0] ~ a[4]

# List Operator

# list add(+)
a = [1,2,3]
b = [4,5,6]
print(a + b) # [1, 2, 3, 4, 5, 6]

#[0][0] = 1
#[1][0] = 4
#[2][0] = 2
#[0][1] = 5
#[1][1] = 3
#[2][1] = 6

#list repeat(*)
b = [10, 20, 30]
print(b * 3) # [10,20,30,10,20,30,10,20,30]

# Array 개념 => python = indexing으로 다룹니다.


#quiz1)다음 프로그램의 결과를 예측하여 보자.
list1 = ['a', 'b', ['c','d'], 1, [2,3], 'e']

print(len(list1)) # 6

print(['b'] in list1)# False

print( ['c','d'] in list1)# True

print('a' in list1) # True

print('b' in list1)# True

#quiz2)다음과 같이 작성된 프로그램의 결과는?

list_odd = [1,3,5,7,9]
list_even = [2,4,6,8,10]

print(list_odd[-3]) # 5

print(list_even[1+3]) # 10

print(list_odd + list_even) #[1,3,5,7,9,2,4,6,8,10]

print(list_odd * 2) #[1,3,5,7,9,1,3,5,7,9]


#quiz3)아래의 실행문에 대한 결과가 올바른지 O/X로 표시해보자
list1 = [1,2,3,4,5,6,7,8,9]

print(list1[:3]) #[1, 2, 3] ( O ) 
print(list1[0:3]) #[2, 3] ( X )
print(list1[3:5]) #[4, 5] ( O )
print(list1[3:]) #[4, 5, 6, 7, 8, 9] ( O )
print(list1[3:999]) #[4, 5, 6, 7, 8, 9, 10, ..] ( X )

string = ['a', 'b', 'c', 'd', 'e', 'f']

print(string[0:3]) # ['a', 'b', 'c']

print(string[2:5]) #['c', 'd', 'e']

print(string[1:3]) # ['b', 'c']

#list 길이 구하기
a = [1,2,3]
print(len(a)) # 3

#print(a[2] + "hi")

print(str(a[2]) + "hi") # 3hi => "3" + "hi"

#str함수는 문자열로 변환해주는 내장 함수 입니다.
# 정수와 실수를 문자열로 변환


#리스트의 수정과 삭제
a = [1,2,3]
a[2] = 4
print(a) # [1,2,4]

del a[1]
print(a)  #[1, 4]

a = [1,2,3,4,5]
del a[2:]

print(a) # [1, 2]

a = [1,2,3]
a.append(4)
print(a) # [1,2,3,4]

a.append([5,6])
print(a) # [1,2,3,4,[5,6]]

list1 = ['1982-07-15','홍길동',30]
print(list1)

#[ sort( ) 함수와 reverse( ) 함수 ] 
a = [1,9,3,5,2,7,8]
a.sort() #오름차순 
print(a) # [1,2,3,5,7,8,9]

a.reverse() #내림차순 
print(a) # [9, 8, 7, 5, 3, 2, 1]

a = ['a', 'c', 'f','b']
a.sort() #오름차순 
print(a) # ['a','b','c','f']

a.reverse() #내림차순 
print(a) # ['f',''c','b','a']


list3 = [ 3,1,5,8,2]
list3.sort()
print('오름차순(기본)정렬후', list3)

list3.reverse()
print('내림차순 정렬후:', list3)

list4 = ['banana','apple','cherry','Apple']
list4.sort()
print('영어 정렬:', list4)

list5 = ['홍길동','전우치','김유신','이순신']
list5.sort()
print('한글 정렬:' , list5)


#위치반환함수: index(x)의 위치 반환
a = [1,9,3,5,2,7,8]
print(a.index(3)) # 2, 5번째 구성요소 
print(a.index(5)) # 3, 3번째 구성요소

#print(a.index(0)) # ValueError: 0 is not in list

#insert(0, 4) : 0번 인덱스 위치에 4를 넣으시오.
a = [1,9,3,5,2,7,8]
a.insert(0,10) 
print(a) # [10, 1, 9, 3, 5, 2, 7, 8]

a.insert(3,50)
print(a) # [10, 1, 9, 50, 3, 5, 2, 7, 8]


#[ append( ) 함수/ insert( ) 함수 ] 

list2 = ['첫째','둘째','셋째']
list2.append('append로 추가한 것')
list2.insert(2,'insert로 추가한 것')
print(list2)


# [ del( ) 함수 / remove( ) 함수 ] 

print('삭제전목록:',list2)
del list2[2]
print('del 로 삭제후 목록:' , list2)

list2.remove("append로 추가한 것")
print('remove 로 삭제후 목록:', list2)


#list element remove
# remove(x) : 첫번째 대상 데이터만 지웁니다.
a = [1,2,3,1,2,3]
a.remove(3)
print(a) #[1, 2, 1, 2, 3]

a.remove(3)
print(a) #[1, 2, 1, 2]

#list의 요소 꺼내기
#pop()은 리스트의 마지막 요소를 반환하고, 삭제합니다.
# stack구조 : LIFO, pop(), push()
a = [10,20,30]
a.pop()
print(a) # 30, [10, 20]

x = a.pop()
print(x) # 20
print(a) # [10]

a = [10,20,50,70]
x = a.pop(2)
print(x) # 50
print(a) #[10, 20, 70]

#list에 포함된 요소 x의 갯수(count) 구하기
a = [1,2,3,5,7,1,2,3,10]
print(a.count(7)) # 1
print(a.count(2)) # 2

#list의 확장(extend)
a = [10,20,30]
a.extend([40,50])
print(a) # [10, 20, 30, 40, 50]

b = [60,70]
a.extend(b)
print(a) # [10, 20, 30, 40, 50, 60, 70]



x22 = "python"
print(x22[0:2]) # py

x3 = [11, 12, 13, 14, 15]
x4 = x3[ :2] # [11, 12]
x5 = x3[2: ] # [13, 14, 15]

print(x4) 
print(x5) 

x6 = [1, 2, 3, ['a', 'b', 'c', ['hyun', 'kim', 'park']]]

print(x6[2: ]) # [3, ['a', 'b', 'c', ['hyun', 'kim', 'park']]]

print(x6[3][ :3]) # ['a', 'b', 'c']
# print(x6[3: ][0][ :3])

print(x6[3][3][ :3]) # ['hyun', 'kim', 'park']



st = [1, 2, 3, 4, 5]
st[ :3] = [0, 0, 0, 0, 0]
st # [0, 0, 0, 0, 0, 4, 5]

st = [10, 20, 30, 40, 50]
st[ :3] = [100, 200, 300, 400, 500]
print(st)


st = [1, 2, 3, 4, 5]
st[2: ] = [0, 0, 0, 0, 0]
st # 

st = [10, 20, 30, 40, 50]
st[2: ] = [100, 200, 300, 400, 500]
print(st)

st = [1, 2, 3, 4, 5]
st[ : ] = [0, 0, 0, 0, 0, 0, 0, 100]
st # 

st = [10, 20, 30, 40, 50]
st[ : ] = [100, 200, 300, 400, 500, 600, 700]
print(st)

st = [1, 2, 3, 4, 5]
st[ : ] = [0]
st # 

st = [10, 20, 30, 40, 50]
st[ : ] = [1000]
print(st)

st = []
st # 



st = [1, 2, 3, 4, 5]
print(st)
st[ : ] = [ ]
st # [ ]



st1 = [1,2,3,4,5,6,7,8]
st2 = st1[0:4]
st2

st = [10, 20, 30, 40, 50]
x = st[0:5]
print(x)


st1 = [1,2,3,4,5,6,7,8]
st2 = st1[0:8:2]
st2

st = [10, 20, 30, 40, 50]
x = st[0:5:2]
print(x) # [10, 30, 50]

st1 = [1,2,3,4,5,6,7,8]
st2 = st1[0:8:3]
st2

st = [10, 20, 30, 40, 50, 60, 70, 80, 90]
x = st[0:9:3]
print(x) # [10, 40, 70]


#연습문제 5-2

#1.
st = [1,2,3,4,5]
st[1] = []
st[3] = []

print(st) # [1, [], 3, [], 5]

# st = [10, 20, 30, 40, 50, 60, 70, 80, 90]일때,
# 2,4,6,8번재의 데이터값을 공백으로 만들어 보세요.

st = [10, 20, 30, 40, 50, 60, 70, 80, 90]

st[1] = [ ]
st[3] = [ ]
st[5] = [ ]
st[7] = [ ]

print(st) # [10, [], 30, [], 50, [], 70, [], 90]



st[1:4] = [3]
print(st) # [1, 3, 5]



#2.
st = [1,2,3,4,5]

#st[2:3] = [3, 3.5]
st[2:4] = [3, 3.5, 4]
print(st) # [1, 2, 3, 3.5, 4, 5]



#3.
st = [1,2,3,4,5]

#st[1:4] = []
st[1:4] = [[],[],[]]
print(st) # [1, 5]

#     0   1   2   3   4   5   6   7   8
st = [10, 20, 30, 40, 50, 60, 70, 80, 90]

st[1 : 8] = [ ] 

print(st) # 10  90


#4.
st = [1,2,3,4,5]

#st[0:5] = []
st[ : ] = []

print(st) #[]



#5.
st = [1,2,3,4,5,6,7,8,9,10]

#nt = st[ : :2]
nt = st[0:10:2]

print(nt) # [1, 3, 5, 7, 9]



#6.
st = [1,2,3,4,5,6,7,8,9,10]

#nt = st[1:10:2]
nt = st[1:10:2]

print(nt) # [2, 4, 6, 8, 10]


print('Happy')
print(type('Happy'))



x = "Happy"
print(x)
print(type(x))



"     ' '    '  '    "

#Exercise
xList = [10, 20, 30]
yList = [40, 50, 60]

print(type(xList)) # <class 'list'>
print(type(yList)) # <class 'list'>

# + 연산의 결과는 ?
print(xList + yList) 
print(xList[0] + yList[0])
print(xList[0] + xList[1])



# 2차원 배열(2x3) 형태로 출력하여 저장된 결과를 확인해 주세요.
z = [xList, yList]

print(type(z)) # <class 'list'>

print(z[0][0], z[1][0])
print(z[0][1], z[1][1])
print(z[0][2], z[1][2])



#연습문제 5-3
str = "hello"
str = str + "Python"
str 



str = "hello"
str += "python"

print("str += 'python :' ", str) # hellopython


# ## 복합 대입 연산자
# ### +=, -=, *=, /=


a = 100
a+= 200
a



b = 50
b-=25
b



c = 25
c*= 5
c



d = 20
d/= 4
d


# ## len()함수

st = [10, 20, 30, 40, 50]
x = len(st)
x



str = 'Hahaha~~~hyun'
x2 = len(str)
x2



def sum(num):
    x = int(input("정수형 데이터 입력: "))
    hap = num + x

    return hap

def main():
    n = sum(100)
    print(n)

main()


x = int(input("첫번째 숫자 입력: "))
y = int(input("두번째 숫자 입력: "))


def so_simple(num):
    print(num) 

def main():
    so_simple([100, 300, 500]) 
        
main()


def sum(num):    
    hap = num[0] + num[1]
    return hap

def main():
    x = int(input("정수형 데이터 입력: "))
    y = int(input("정수형 데이터 입력: "))
    st = [x, y]
    n = sum(st)
    print(n)

main()


def so_simple(num):
    return num

def main():
    n = so_simple([100, 300, 500]) 
    print(n) 

main()


def sum():
    x = int(input("정수형 데이터 입력: "))
    y = int(input("정수형 데이터 입력: "))
    z = int(input("정수형 데이터 입력: "))
    st = [x, y, z]
    
    hap = st[0] + st[1] + st[2]

    return hap

def main():
      
    n = sum()
    
    print(n)

main()


def so_simple():
    st = [100, 300, 500]
    return st

def main():
    n = so_simple() 
    print(n) 

main()



def so_simple(str):
    return str + " hyun"

def main():
    n = so_simple("hello") 
    print(n) 

main()


def sum():
    x = input("문자열 데이터 입력: ")  
    st = [x]    
    return st

def main():      
    n = sum()
    
    print(n)

main()



#연습문제 5-4

#문제1>
def sum_all(num):

    sum = 0
    for i in range(len(num)):
        sum += num[i]
    return sum
    
sum = sum_all([1,2,3,4,5])
print(sum) # 15



def sum():

    sum = 0

    for i in range(1, 11):
       sum += i
      
    return sum

def main():
      
    n = sum()
    
    print(n)

main()




#문제2>
def show_reverse(str):

    for i in range(len(str)):
        print(str[(i+1) * -1], end = ' ')

x = show_reverse([1,2,3,4,5])

print(x) # 54321



def show_reverse2(str):

    for i in range(len(str)):
        print(str[(i+1) * -1], end = ' ')

x2 = show_reverse2("ABCDEFG")

print(x2) # GFEDCBA

