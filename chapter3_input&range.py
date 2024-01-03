
x = input("첫 번째 입력: ")
y = input("두 번째 입력: ")

num = x + y
print(num)


num = 31 + 24
print(num)


x = input("첫 번째 입력: ")
y = input("두 번째 입력: ")

xx = int(x)
yy = int(y)

num = xx + yy

print(num)


x = input("첫 번째 입력(실수형): ")
y = input("두 번째 입력(실수형): ")

xx = float(x)
yy = float(y)

num = xx + yy

print(num)
# 17.939999999999998 합계를 보면 오차가 발생함을 알수있습니다.


# eval함수는 수식을 포함하여 연산합니다.
year = input("연도를 입력하세요.")

y = int(year)

x = eval("y + 55 - 10")

x = x + 100

print(x)


# (3 + ((4 / 2) * 7)) =?
x = eval(input("연도를 입력하세요."))

print(x) # 


# indexing
#          0    1     2
for i in [100, 110, 120]:  #  가변 for문 
    print(i, "hi~~~")
       

for i in ['홍길동', '김길동', '이길동', '사길동', '오길동']:
    print(i, "hi~~~")



#1 
sum = 0

for i in [1,3,5,7]:
    sum += i
    
print(sum)    


#2

sum = 1

for i in [1,2,3,4,5,6,7,8,9,10]:
    sum *= i
    
print(sum)    


#3
dan = int(input("원하는 단을 입력하세요."))

for i in [1,2,3,4,5,6,7,8,9]:   
    
    print(dan, "*", i, "=", dan*i)
  
    
for i in range(1, 10):
    print(dan, "*", i, "=", dan*i)


sum = 0;

# 난수 발생: 45 : 0~44, (45) + 1 : 1 ~ 45 숫자 발생
# range[0,1,2,3,4,5,6,7....100] => 0~99
for i in range(1,101): # 1~ 100
    sum+=i
    
print(sum)    


cnt = int(input("횟수를 입력하세요."))

for i in range(cnt):
    print("I love coffee")


#정수형 데이터 출력 
a=123
print (a)

a = input("숫자 데이터를 입력하시오.") #키보드에서 직접 데이터를 입력합니다.
print(a)


a=-178
print (a)

a=0
print (a)

#실수형 데이터 출력
a=1.2
print(a)

a = input("실수형 데이터를 입력하시오.")
print(a)

a=-3.45
print(a)

#부동소수점(지수형) 데이터 출력
# 가장 큰 값이나 가장 작은 값을 표현 할 때 사용합니다.
# 오른쪽 소숫점 이동 : 값이 커집니다.
a=4.24E+10
print(a) # 42400000000.

# 왼쪽으로 소수점 이동 : 값이 작아집니다.
a=4.24E-10
print(a) # 0.00000000424

#8진수 (2의 3승) = 3비트 
a = 0o177
print(a) # 127 (0   0   1  1  1  1 1 1 1)


#16진수 (2의 4승) = 4비트 
b = 0x177
print(b) # 375


# 2진수 => 컴퓨터 입장
# 10진수 => 사람 입장
# 응용프로그램 => 16진수 형태

#사칙연산
a=3
b=4
print('덧셈 : ', a + b)
print('뺄셈 : ', a - b)
print('곱셈 : ', a * b)
print('나눗셈 : ', a / b) # 나머지의 몫 
print('나눗셈(나머지) : ', a % b); #나눗셈의 나머지
print(7 / 4)
print(7 // 4)

print(a ** b) #3의 4승

#a = input("정수형 데이터를 입력하시오.")
#b = input("정수형 데이터를 입력하시오.")
sum = int(input("정수형 데이터를 입력하시오.")) + int(input("정수형 데이터를 입력하시오."))
print("정수형의 연산 : ", sum)

a = input("정수형 데이터를 입력하시오.")
b = input("실수형 데이터를 입력하시오.")
sum2 = int(a) + float(b)
print("실수형의 연산 : ", sum2)

a = input("문자열 데이터를 입력하시오.")
b = input("문자열 데이터를 입력하시오.")
sum3 = a + b
print("실수형의 연산 : ", sum3)


#연산자 우선순위 : 산술, 관계(비교), 논리연산 

print(2 + 4 * 5) #22
print((2 + 4) * 5) #30
print(9 + 54 / 6) #18.0

print(2 ** 4 + 5) # 21


#복합대입(단축) 연산자 : +=, -=, *=, /=, //=, %=

x=1
x+=1 # x= x + 1
print(x)

x2=10
x2-=30 # x2 = x2 - 30
print(x2)

x3=5
x3*=10 # x3 = x3 * 10
print(x3)

x4=20
x4/=3  # x4 = x4 / 3
print(x4)

x5=30
x5//=3 # x5 = x5 // 3
print(x5)

x6=30
x6%=3 # x6 = x6 % 3
print(x6)


#문자열(String)

print("Hello World")
print('Hello World')
print("""Life is too short, You need python""")
print('''Life is too short, You need python''')

#문자열 안에 작은따옴표나 큰따옴표를 포함하고자 할 때
food = "Python's favorits food is perl"
print(food)

say='"python is very easy". he says.'
print(say)

#큰 작은 따옴표 포함하기
food2 = "Python\'s favorits food is perl"
say2 = "\"python is very easy\". he says."
print(food2 + say2)

# + : 덧셈(산술연산), 연결연산자(문장의 연결)

multiline = "Life is too short \nYou need python"
print('line1: ', multiline)

multiline = "Life is too short \tYou need python"
print('line2 : ', multiline)

multiline = "Life is too short \\You need python"
print('line3 : ', multiline)

multiline = "Life is too short \aYou need python"
print('line4 : ', multiline)


multiline2 = '''
    Life is too short
    You need python
    '''
print(multiline2)

multiline3 = """
    Life is too short
    You need python
    """
print('Line3 : ', multiline3)

multiline4 = input("문자열 데이터 입력")
multiline5 = input("문자열 데이터 입력")

print("\n", multiline4)
print(multiline5)

	
i = 123
f = 45.6
s = "this is a string"
list_of_stuff = ["foo", "bar", "baz"]
print("\n", i)
print("\n", f)
print("\n", s)
print("\n", list_of_stuff)

#문자열 연산하기
a="python"
a= a * 3
print(a)

print("=" * 10)
print("My program")
print("=" * 10)

#문자열 길이 구하기
a = "Life is too short"
print(len(a)) #17바이트 소요

#Quiz>
# x,y에 각각 10과 20을 할당하고, z라는 변수를
# 이용하여 두 수를 교환하여 출력하세요.
x=10
y=20
z=x
x=y
y=z
print('x값: ', x)
print('y값: ', y)

#문자열 인덱싱
# 0 123456789101112
a="Life is too short, You need Python"
print(a[3])
print(a[6])
print(a[-2])
print(a[0]) #L
print(a[-0]) #L

#문자열 슬라이싱
a="Life is too short, You need Python"
b=a[0] + a[1] + a[2] + a[3]
print(b)

print(a[0:4]) # -1: 0,1,2,3 => Life
print(a[0:3]) # -1: 0,1,2 => Lif


# a[10] => a[0] ~ a[9] : -1

print(a[19:]) #You need Python
print(a[:17]) #Life is too short
print(a[:]) #Life is too short, You need Python
print(len(a)) #34 => 0 ~ 33


#슬라이싱으로 문자열 나누기
#    012345678
a = "20210605Rainy"
date = a[:8] # 20210605
weather = a[8:] # Rainy
print("오늘 날짜는 " + date + "이고, 날씨는 " + weather + "입니다.")

a2 = "20210605Rainy"
date = a2[:4] # 2021
day = a2[4:8] # 0605
weather = a2[8:] # Rainy
print("년도는 " + date + "이고, 날짜는 " + day + "이고, " +  "날씨는 " + weather + "입니다.")

print(type(a2)) # <class 'str'>
print(type(date))
print(type(day))
print(type(weather))

# 정수형이란? 부동 소수점이 없는 수 
a=300
print(type(a)) #<class 'int'>

# 실수형이란? 부동 소수점이 있는 수 
b=330.123
print(type(b)) #<class 'float'>

#문자열의 변경 
a="pithon"
print (a[1]) # i

# a[1] = 'y' #'str' object does not support item assignment

print(a)

#문자열의 변경의 해결방안
#string은 한번 지정하면 변경이 안됩니다.
# 할당문의 지정이 안됩니다. ( = )
# 특히, index를 이용한 변경은 허용하지 않습니다.
print(a[:1]) #p
print(a[2:]) #thon
print(a[:1] + 'y' + a[2:]) #python

#문자열 포매팅(Formatting)
a = "I eat %d apples." % 3
print(a)

a = "I eat %s apples." % "five"
print(a)

number = 3
a = "I eat %d apples." % number
print(a)

number = 10
day = "three"
a = "I eat %d apples. so I was sick for %s days." % (number, day)
print(a)

#숫자 + 문자 => 문자
# 300 + abc => 300abc
#정수형 + 정수형 => 정수형
#정수형 + 실수형 => 실수형
#실수형 + 문자 => 문자열

#a = 'k' # %c character => 영문 소문자 한문자 
#b = 'kim' # %s String => 영문 소문자 여러문자

#a => ascii code 97
#A => ascii code 65

# ASCII code : 미국 정보통신용 표준코드 => 유니코드

#포멧코드와 숫자 사용
# 1.정렬과 공백
a = "%10s" % "hi"
print(a)

a = "%-15s Hyun" % "hi superman"
print(a)

#2.소수점 표현하기
a = "%0.4f" % 3.4213234
print(a)

a = "%10.4f" % 3.4213234
print(a)

a = "%8.3f" % 12.456
print(a)

# %8.3f => 전체자릿수는 8자리이고,
# 소수점 이하 자릿수는 3자리 이고
#  나머지는 공백 2자리입니다.


#포맷함수 이용하기 : 함수의 형식 => 함수이름(매개변수)
a = "I eat {0} apples".format(3)
print(a)

number = 3
a = "I eat {0} apples".format(number)
print(a)

a = "I eat {0} apples".format("five")
print(a)

str = "five"
a = "I eat {0} apples".format(str)
print(a)

#2개 이상의 값 넣기
number = input("정수형 데이터 입력")
day = input("문자열 입력")

str = "I eat {0} apples. I was sick for {1} days.".format(number, day)
print(str)

# 왼쪽 정렬
a = "{0:<10}".format("hi")
print(a) # 'hi        '

# 오른쪽 정렬
a = "{0:>10}".format("hi")
print(a) # '        hi'

# 가운데 정렬
a = "{0:^10}".format("hi")
print(a) # '    hi    '


#문자열 인덱싱
# 0 123456789101112
a="Life is too short, You need Python"
print(a[3])
print(a[6])
print(a[-2])
print(a[0]) #L
print(a[-0]) #L

#문자열 슬라이싱
a="Life is too short, You need Python"
b=a[0] + a[1] + a[2] + a[3]
print(b)

print(a[0:4]) # -1: 0,1,2,3 => Life
print(a[0:3]) # -1: 0,1,2 => Lif


# a[10] => a[0] ~ a[9] : -1

print(a[19:]) #You need Python
print(a[:17]) #Life is too short
print(a[:]) #Life is too short, You need Python
print(len(a)) #34 => 0 ~ 33


#슬라이싱으로 문자열 나누기
#    012345678
a = "20210605Rainy"
date = a[:8] # 20210605
weather = a[8:] # Rainy
print("오늘 날짜는 " + date + "이고, 날씨는 " + weather + "입니다.")

a2 = "20210605Rainy"
date = a2[:4] # 2021
day = a2[4:8] # 0605
weather = a2[8:] # Rainy
print("년도는 " + date + "이고, 날짜는 " + day + "이고, " +  "날씨는 " + weather + "입니다.")

print(type(a2)) # <class 'str'>
print(type(date))
print(type(day))
print(type(weather))

# 정수형이란? 부동 소수점이 없는 수 
a=300
print(type(a)) #<class 'int'>

# 실수형이란? 부동 소수점이 있는 수 
b=330.123
print(type(b)) #<class 'float'>

#문자열의 변경 
a="pithon"
print (a[1]) # i

# a[1] = 'y' #'str' object does not support item assignment

print(a)

#문자열의 변경의 해결방안
#string은 한번 지정하면 변경이 안됩니다.
# 할당문의 지정이 안됩니다. ( = )
# 특히, index를 이용한 변경은 허용하지 않습니다.
print(a[:1]) #p
print(a[2:]) #thon
print(a[:1] + 'y' + a[2:]) #python

#문자열 포매팅(Formatting)
a = "I eat %d apples." % 3
print(a)

a = "I eat %s apples." % "five"
print(a)

number = 3
a = "I eat %d apples." % number
print(a)

number = 10
day = "three"
a = "I eat %d apples. so I was sick for %s days." % (number, day)
print(a)

#숫자 + 문자 => 문자
# 300 + abc => 300abc
#정수형 + 정수형 => 정수형
#정수형 + 실수형 => 실수형
#실수형 + 문자 => 문자열

#a = 'k' # %c character => 영문 소문자 한문자 
#b = 'kim' # %s String => 영문 소문자 여러문자

#a => ascii code 97
#A => ascii code 65

# ASCII code : 미국 정보통신용 표준코드 => 유니코드

#포멧코드와 숫자 사용
# 1.정렬과 공백
a = "%10s" % "hi"
print(a)

a = "%-15s Hyun" % "hi superman"
print(a)

#2.소수점 표현하기
a = "%0.4f" % 3.4213234
print(a)

a = "%10.4f" % 3.4213234
print(a)

a = "%8.3f" % 12.456
print(a)

# %8.3f => 전체자릿수는 8자리이고,
# 소수점 이하 자릿수는 3자리 이고
#  나머지는 공백 2자리입니다.


#포맷함수 이용하기 : 함수의 형식 => 함수이름(매개변수)
a = "I eat {0} apples".format(3)
print(a)

number = 3
a = "I eat {0} apples".format(number)
print(a)

a = "I eat {0} apples".format("five")
print(a)

str = "five"
a = "I eat {0} apples".format(str)
print(a)

#2개 이상의 값 넣기
number = input("정수형 데이터 입력")
day = input("문자열 입력")

str = "I eat {0} apples. I was sick for {1} days.".format(number, day)
print(str)

# 왼쪽 정렬
a = "{0:<10}".format("hi")
print(a) # 'hi        '

# 오른쪽 정렬
a = "{0:>10}".format("hi")
print(a) # '        hi'

# 가운데 정렬
a = "{0:^10}".format("hi")
print(a) # '    hi    '

#공백 채우기
a = "{0:=<10}".format("hi")
print(a) #hi========

a = "{0:=>10}".format("hi")
print(a) # '========hi'

a = "{0:=^10}".format("hi")
print(a) # '====hi===='

a = "{0:!^10}".format("Hello")
print(a) # '!!Hello!!!'

y = 3.42134234
print("{0:0.4f}".format(y)) #3.4213

y = 3.42134234
print("{0:10.4f}".format(y))#    3.4213

y = 3.42134234
print("{0:9.4f}".format(y))#    3.4213
      
#문자 표현하기
x = "{{ and }}".format()
print(x)#{ and }


print("{{ and }}".format())#{ and }

# f 문자열 포매팅(Formatted)
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
#나의 이름은 홍길동입니다. 나이는 30입니다.


#아래 형식 출력은 지원하지 않습니다.
#print(f'나의 이름은' + {name} + '입니다. 나이는' +  {age} + '입니다.')

# dictionary : key:value => Map
d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]} 입니다. 나이는 {d["age"]}입니다.')      
#나의 이름은 홍길동 입니다. 나이는 30입니다.

age = 30
print(f'나는 내년이면 {age + 5} 살이 됩니다.')
#나는 내년이면 35 살이 됩니다.

print(f'{"hi":<10}') #hi
print(f'{"hi":>10}') #          hi
print(f'{"hi":^10}') #    hi    

print(f'{"hi":=<10}') #hi========
print(f'{"hi":!>10}') #!!!!!!!!hi
print(f'{"hi":*^10}') #****hi****

y = 3.42134234
print(f'{y:0.4f}') #3.4213

y = 3.42134234
print(f'{y:10.4f}')#    3.4213

y = 3.42134234
print(f'{y:9.4f}')#    3.4213


x = f'{{ and }}'
print(x)   #{ and }

# !!!Python!!! 문자열을 출력 합니다.
print(f'{"Python":!^12}')

print("{0:!^12}".format('Python'))

x = 'Python'
print("{0:!^12}".format(x))

# name = "Gildong", location = "seoul"
# 결과는 길동이는 서울에 살고 있습니다.

name = 'Gildong'
location = 'seoul'
print(name + '이는 ' + location + '에 살고 있습니다.')

# 다음과 같은 문자열을 출력하세요.
# *****Hello, Python*****

str1 = 'Hello,'
str2 = 'Python'
str3 = '*****'
print(str3 + str1 + str2 + str3)

str1 = 'Hello,'
str2 = 'Python'
str3 = '*'
print(str3 * 5 + str1 + str2 + str3 * 5)
print(len(str1)) #6
print(len(str2)) #6
print(len(str3)) #1
print(len(str3 * 5)) #5

#다음 문자열에서 특정 문자를 뽑아 출력하세요.
# name = 'Hong Gil Dong'에서 Gil을 출력합니다.
name = 'Hong Gil Dong'
str = name[5:8]
print(str)


#input 함수를 이용하여 연필과 지우개를 구입하여 출력
# 연필 5개 , 각 가격은 1000원
# 지우개 10개, 각 가격은 100원 으로 합니다.
# 총 가격을 출력하세요.

pen = input("연필은 몇 개를 구입하시겠어요?")
earser = input("지우개는 몇 개를 구입하시렵니까?")

intpen = int(pen)
pentotal = intpen * 1000

earsertotal = int(earser) * 100

total = pentotal + earsertotal
print('전체 가격은 ', total, '원 입니다.')
