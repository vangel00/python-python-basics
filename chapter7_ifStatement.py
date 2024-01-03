# # if Statement
# 
# ### 조건문이란?
# ### 특정 내용을 수행하기 위하여 조건을 체크하여 수행(실행)하는 명령문을 말합니다. 
조건문은 참이나 거짓으로 판별하여 참이면 실행합니다.

print(True) # 참
print(False) # 거짓

3 >= 10

10 >= 3


# 관계 연산자(비교 연산자): ==, !=, >, >=, <, <=
a = 100
b = 300

x = (a != b)
print(x)
print(type(x))

# 1유형
money = True
if money:
    print("go Taxi")

# 2유형
money = True
if money:
    print("go Taxi")
else:
    print("go Homeworking")
    
x = 300
y = 200

print(x > y) #True
print(x < y) #False
print(x == y) #False
print(x !=y) # True

money = 2000
if money >= 3800:
    print("taxi")
else:
    print("working")

# ## main 함수 사용법

def output():
    print("Simple Frame")
    
def main():
    output() 
    output()
    output()

main()


# 문제> 어떤값을 입력 받아서, 그 값이 양수인지 음수인지 판별하여 출력하세요.

x = int(input("숫자를 입력하세요."))

if x > 0:
    print("양의 정수 입니다.")                
else:
    print("음의 정수 입니다.")


def su():
    num = int(input("정수 입력 : "))

    if num > 0:
        print("0보다 큰 양의 정수 입니다.")
    elif num < 0:
        print("0보다 작은 음의 정수 입니다.")
    else:
        print("0입니다.")

def main2():
    su()

main2()



# is_phone_num.py

def main():
    pnum = input("스마트폰 번호 입력: ")

    if pnum.isdigit() and pnum.startswith("010"):
        print("정상적인 입력입니다.")
    else:
        print("정상적이지 않은 입력입니다.")

main()


# 문제3> 두수를 입력 받아서 덧셈과 곱셈의 결과를 출력하세요.
def adder(num1, num2):
    print("adder(): ", num1 + num2)

def multer(num1, num2):
    print("multer(): ", num1 * num2)
    
def main():
    x = int(input("숫자를 입력하세요."))
    y = int(input("숫자를 입력하세요."))      
   
    adder(x,y)
    multer(x,y)

main()


# divide&conquer

def baesu23(num1):
    if (num1 % 2 == 0):
        if (num1 % 3 == 0):
            print(num1, "은 2의 배수이면서 3의 배수 입니다.!!!")
        else:
            print(num1, "은 3의 배수가 아닙니다.")
    else:
        print(num1, "은 2의 배수가 아닙니다.")
            
def main():
    num1 = int(input("정수 입력 : "))
    baesu23(num1) #2의 배수 구하기
    
main()



def baesu3(num1):
    if (num1 % 3 == 0):
        print(num1, "은 3의 배수 입니다.!!!")
    else:
        print(num1, "은 3의 배수가 아닙니다.")

def main():
    num1 = int(input("정수 입력 : "))
    baesu3(num1) #3의 배수 구하기
    
main()


# # 논리 연산자
# 
# ## 논리 회로

##############################
# a b   and   or   not    exor
##############################
# 0 0    0    0   0 => 1   0
# 0 1    0    1   1 => 0   1
# 1 0    0    1            1
# 1 1    1    1            0
##############################


# and.py

def main():
    num = int(input("2의 배수이면서 3의 배수인 수 입력: "))

    if num % 2 == 0 and num % 3 == 0:
        print("OK!")
    else:
        print("NO!") 

main()

# if_and_if.py

def main():
    num = int(input("2의 배수이면서 3의 배수인 수 입력: "))

    if num % 2 == 0:
        if num % 3 == 0:
            print("OK!")
        else:
            print("NO!")
    else:
        print("NO!")
    
main()

# num = 6
num = int(input("정수 입력 : "))
(num%2) == 0 and (num%3) == 0


value = 1 in [1,2,3] # 1이 속해있으면 true, 아니면 false
print(value) #True
print(10 in [10,20,30]) #True

print(100 not in [100,200,300]) #False

print('a' in('a','b','c')) # True
print('j' not in 'Python') # True

pocket = ['paper', 'cellphone', 'money']

if 'money' in pocket:
    print('Taxi')
else:
    print('working') # Taxi

# 3유형 : if ~ else ~ if else....
pocket = ['paper', 'cellphone']
card = True

if 'money' in pocket:
    print('Taxi')
else:
    if card:
        print('Taxi')
    else:
        print('working') # Taxi
    
# 4유형 : if ~ elif
pocket = ['paper', 'cellphone']
card = True

if 'money' in pocket:
    print('Taxi')
elif card:
    print('Taxi')
else:
    print('working') # Taxi     

score = 100

if score  >= 60:
    message = "success"
else:
    message = "failure"
print(message) #success

#조건부 표현식
message = "success" if score >= 60 else "failure"
print(message) # success

score = 90
message2 = "100" if score >= 60 else "400" "100" if score >=70 else "400"
print(message2)


# 1~100사이에 3의 배수를 구하여 그 합계를 출력하세요.
sum = 0
count = 0

for i in range(1, 101):
    
    if(i%3 == 0): 
        print(i)
        sum += i
        count += 1        
        
print(sum)
print(count)


#quiz1)사용자로부터 나이를 입력 받아서,
#20살 이상인 경우에 '성인'이라는 문장을 출력하세요.
age = input('나이를 입력해 주세요.')
age2 = int(age)
if age2 > 20:
    print('성인입니다.')
else:
    print('미성년 입니다')
    
#quiz2)백화점에서 여러 물품을 구매합니다.
#구매한 물품의 총합계가 10만원 이상인 경우에는
#상품권을 받을 수 있도록 출력 하세요.

total = 30000 + 15000 + 25000 + 55000
if total >= 100000:
    print('상품권 지급')
else:
    print('상품권이 없습니다.')

----------------------------------------
#연습문제 7-1

#1.
def Operation():
    num = int(input("정수 입력"))
    
    if(num >= 0):
        print("입력한 값이 0이거나 0보다 큽니다.")
    else:
        print("입력한 값이 0보다 작습니다.")

def main():
    Operation()
    Operation()
    Operation()
    
main()


#2.
num = 3
print(1 < num and num < 5) # True

#3.
num = 12
print(num < 3 or num > 10) # True

#4.
num = 4
print(num % 2 == 0 and num % 3 != 0) # True
print(num % 2 == 0 or num % 3 == 0) # True

#5.
def RelationOparation2():
    num = int(input("정수 입력: "))

    if num < 0:
        print("입력한 값이 0보다 작습니다.")
    elif 0 <= num < 10 : # (0 <= num && num < 10)
        print("입력한 값이 0이상 10미만 입니다.")
    elif 10 <= num < 20:
        print("입력한 값이 10이상 20미만 입니다.")
    else:
        print("입력한 값이 20보다 큽니다.")

def main():
    RelationOparation2()

main()
    


st1 = "123"
x = st1.isdigit()
print(x)

st2 = "ABC"
xx = st2.isdigit()
print(xx)


# In[68]:


st3 = "abcdefg"
x = st3.isalpha()
print(x)

xx = st3.isdigit()
print(xx)


str = "Supersprint"
x = str.startswith("Super")
print(x)
y = str.endswith("Int")
print(y)


"ABC" == "abc" #ASCII code 기준으로 판단합니다.


#p.141 전화번호 처리 조건
#1.공백이 없이 데이터 입력
#2. - 이라는 특수문자를 제거 하고 입력
#3.010으로 시작하라.


# 예제 1
name = input('조회할 사람의 이름을 입력하세요: ')

if name=='홍길동' :
    print("홍길동 입니다")
    print("남자입니다")
    print("활빈당 총수입니다")

# 예제 2
name = input('조회할 사람의 이름을 입력하세요: ')

if name=='홍길동' :
    print("홍길동 입니다")
    print("남자입니다")
    print("활빈당 총수입니다")


# 예제 3
name = input('조회할 사람의 이름을 입력하세요: ')

if name=='홍길동' :
    print("홍길동 입니다")
    print("남자입니다")
    print("활빈당 총수입니다")
else :
    print("홍길동이 아니고 %s 입니다" %name)
    print("남자인가요?")
    print("여자인가요?")


#예제 4

jumsu = int(input("점수를 입력하세요: "))

if jumsu >= 91 and jumsu <= 100 :
    print(" A 등급입니다!")
elif jumsu >= 81 and jumsu <= 90 :
    print(" B 등급입니다!")
elif jumsu >= 71 and jumsu <= 80 :
    print(" C 등급입니다!")
else :
    print(" D 등급입니다!")


# 예제 6
answer = input("Y 또는 y 를 입력하세요: ")
if answer == 'Y' or answer == 'y' :
    print("입력하신 문자는 %s 입니다" %answer)
else :
    print("Y 또는 y 를 입력하세요")



# 예제 8
answer = input("Y 또는 y 를 입력하세요: ")
if answer != 'Y' and answer != 'y' :
    print("입력하신 문자는 %s 입니다" %answer)
else :
    print("Y 또는 y 를 입력하셨군요~")



#Quiz) 영어단어 문제를 출제하기 위하여 아래와 같은
# 단어가 준비되어 있습니다.
# ex1 = ["risk", "issue", "test", "maintenance", "mat"]
# ex2 = ["security", "pain", "design", "system", "safe"]
# ex3 = ["maintenance", "verification", "validation"]

# 위의 3가지의 list중에서 하나를 골라서.
# 영어 단어 시험을 출제 합니다.
# 1."maintenance"라는 단어를 이용합니다.
# 2. 영어 단어의 갯수는 적어도 5개는 되어야 합니다.

# 시험 문제로 사용할 수 있는 리스트를 찾아서
# 프로그램을 작성해 보세요.

ex1 = ["risk", "issue", "test", "maintenance", "mat"]
ex2 = ["security", "pain", "design", "system", "safe"]
ex3 = ["maintenance", "verification", "validation"]

if('maintenance' in ex1) and (len(ex1) >= 5):
    print('ex1을 시험 출제로 사용합니다.')
elif('maintenance' in ex2) and (len(ex2) >= 5):
    print('ex2를 시험 출제로 사용합니다.')
elif('maintenance' in ex3) and (len(ex3) >= 5):
    print('ex3을 시험 출제로 사용합니다.')
else:
    print('시험 출제로 사용할 데이터가 존재하지 않습니다.')

    # ex1을 시험 출제로 사용합니다.    

def select():
    num = int(input("정수 입력"))
    
    print(num, "을 입력 받았습니다.")  

def main():
    select()
main()    

------------------------------------------



#연습문제 7-2

def RelationOparation3():
    
    num = input("정수 입력: ") # "123"

    if num.isdigit():
        print(int(num) ** 2)
    else:
        print("입력한 값이 정수형이 아닙니다.!!!")

def main():
    RelationOparation3()

main()    

print(bool(0)) # False


#Quiz) 영어단어 문제를 출제하기 위하여 아래와 같은
# 단어가 준비되어 있습니다.
# ex1 = ["risk", "issue", "test", "maintenance", "mat"]
# ex2 = ["security", "pain", "design", "system", "safe"]
# ex3 = ["maintenance", "verification", "validation"]

# 위의 3가지의 list중에서 하나를 골라서.
# 영어 단어 시험을 출제 합니다.
# 1."maintenance"라는 단어를 이용합니다.
# 2. 영어 단어의 갯수는 적어도 5개는 되어야 합니다.

# 시험 문제로 사용할 수 있는 리스트를 찾아서
# 프로그램을 작성해 보세요.

ex1 = ["risk", "issue", "test", "maintenance", "mat"]
ex2 = ["security", "pain", "design", "system", "safe"]
ex3 = ["maintenance", "verification", "validation"]

if('maintenance' in ex1) and (len(ex1) >=5):
    print('ex1을 시험 출제로 사용합니다.')
elif('maintenance' in ex2) and (len(ex2) >=5):
    print('ex2를 시험 출제로 사용합니다.')
elif('maintenance' in ex3) and (len(ex3) >=5):
    print('ex3를 시험 출제로 사용합니다.')
else:
    print('시험 출제를 할 수 없습니다.') 




