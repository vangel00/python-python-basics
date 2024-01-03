
# 안녕하세요 반갑습니다.....

print("hello world")
print("안녕하세요")

# 함수 처리 : 전달인자와 매개변수가 존재하는 형태 
def  add(a, b):  # 매개변수(parameter a, b)
    return a+b   # 리턴 

print(add(3, 4))   #전달인자(argement value)값

# 함수 처리 : 전달인자가 없는 경우 
def add3():
    a=3
    b=4
    c=a+b
    return c

print(add3())


def add(a,b):
    return a + b

a = int(input("정수형 데이터 입력 하세요."))
b = int(input("정수형 데이터 입력 하세요."))

c = add(a,b)

print(c)


# 함수 처리 : 리턴이 없는 경우 
def add2(a, b):
    print(a + b)  

add2(3, 4)


def add(a,b):
    print(a + b)

a = int(input("정수형 데이터 입력 하세요."))
b = int(input("정수형 데이터 입력 하세요."))

add(a,b)


# 함수 처리 : 둘 다 없는 경우 
def add4():
    a=3
    b=4
    c=a+b
    print(c)

add4()

def add():
    a = int(input("정수형 데이터 입력 하세요."))
    b = int(input("정수형 데이터 입력 하세요."))
    
    print(a + b)

add()


#function(함수)

# 예제 1

def p(x,y):
    print('%s 과 %s 의 더한 값은 %s 입니다' %(x, y, x+y) )
    return 

def main():
    p(33, 44)
        
main()



def p(x,y):
    result = x + y
    return result

def main():
    x = int(input("123"));
    y = int(input("123"))
    result = p(33, 44)
    print(x, '와', y, '의' , '더한 값은', result, '입니다')
    
main()



# 예제 2
#여러개의 입력값을 처리하는 함수 만들기(*x)
def pmany(*x):
    hap =0

    for i in x:
        hap += i
    return hap

sum = pmany(1,3,5)
print(sum)

sum = pmany(2,4,6, 8)
print(sum)

#print(pmany(1,3,5))
#print(pmany(2,4,6,8))


# 예제 3

def add(a, b):
    return a + b # 100 + 200 = 300

a = 100
b = 200
c = add(a, b)
print(c) # 300

d = add(3000, 5000)
print(d) # 8000


# # 함수의 오버로딩
# ## 함수이름은 같으나 인자의 갯수와 데이터 타입이 다르면 ...

# In[20]:


sum = 0

def cal(x, y, z):
    sum = a + b + c
    return sum

def cal(a, b):
    sum = a * b
    return sum

e = cal(11, 22, 33)
f = cal(100, 200)

print(e) # 66
print(f) # 결론은 좀 다른 형태로 지원합니다. 기존 스타일 형태의 방법은 지원하지 않습니다.




#입력값이 없는 함수 유형
def say():
    return 'Hi'

a = say()
print(a) # Hi

def say():
    msg = input("Hello")
    return msg # 안녕

a = say()
print(a) # 안녕

#반환이 없는 함수

def add(a, b):
    print(a+b) # 70

add(30,40)

#반환이 있는 함수
def add(a,b):
    return a + b

result = add(30, 40)
print(result) # 70


#반환값이 없는데, 전달인자도 없는 함수
def say():
    print('HI')

say() # HI

def add():
    print(30 + 40)

add() # 70

#매개변수 지정하여 호출하기
def add(a, b):
    return a + b

result = add(a=3, b=7)
print(result) # 10

result = add(b=5, a=7)
print(result) # 12


#여러개의 입력값을 처리하는 함수 만들기
def add_many(*args):    
    result = 0
    
    for i in args:
        result = result + i
    return result

def main():
    x = int(input("123"))
    y = int(input("456"))
    z = int(input("789"))
    result = add_many(x, y, z)
    print(result)

main()



a =1

def vartest(a):
     a =  a + 1

vartest(a)
print(a) # 1

[해결방안]

a =1

def vartest(a):
     a =  a + 1
     return a

a = vartest(a)
print(a) # 2


a =1

def vartest(a):
     global a
     a =  a + 1
    

vartest()
print(a) # 2


-------------------------------------
#연습문제 10-1

for i in range(3):
    print(i + 1, i + 2, i + 3, sep = ', ')
    # 0+1=1, 0+2=2, 0+3=3
    # 1+1=2, 2+1=3, 3+1=4
    # 2+1=3, 3+1=4, 4+1=5

#1, 2, 3
#2, 3, 4
#3, 4, 5

------------------------------------
교재 p.190

st = [100, 200, 300]

def func(st):
    
    st[0] = 500
    st[-1] = 1000
    
    return st

def main():
   func(st)
    
main()

func(st)

----------------------------------


#연습문제 10-2
    
def adder(s):
    for i in range(len(s)):
	    s[i] += 1

st = [1, 2, 3, 4, 5]
adder(st)
st
[2, 3, 4, 5, 6]



#여러개의 입력값을 처리하는 함수 만들기
def add_many(*args):    
    result = 0
    
    for i in args:
        result = result + i
    return result

def main():
    x = int(input(""))
    y = int(input(""))
    z = int(input(""))
    result = add_many(x, y, z)
    print(result)

main()




#연습문제 10-1

for i in range(5):
    print(i + 1, i + 2, i + 3, sep = ', ')
    # 0+1=1, 0+2=2, 0+3=3
    # 1+1=2, 2+1=3, 3+1=4
    # 2+1=3, 3+1=4, 4+1=5

#1, 2, 3
#2, 3, 4
#3, 4, 5




#      0    1    2    
st = [100, 200, 300]

def func(st):
    
    st[0] = 500
    st[-1] = 1000
    
    return st

def main():
   func(st)
    
main()

func(st)




#연습문제 10-2
    
def adder(s):
    for i in range(len(s)):
        s[i] += 1

st = [1, 2, 3, 4, 5]
adder(st)
st


# In[28]:


#연습문제 10-2

st = [1, 2, 3, 4, 5]

def adder(s):
    for i in range(len(s)):
        s[i] += 1

adder(st)
st



#연습문제 10-2

st = [1, 2, 3, 4, 5]

def adder(s):
    for i in range(len(s)):
        s[i] += 1
def main():
    adder(st)
  #  print(st)
    
main()

st



def divi2(su1, su2):
    divisum2 = su1 % su2
    return divisum2
    
def divi(su1, su2):
    divisum = su1 / su2
    return divisum

def multi(su1, su2):
    mulsum = su1 * su2
    return mulsum

def sub(su1, su2):
    subsum = su1 - su2
    return subsum

def add(su1, su2):
    addsum = su1 + su2
    return addsum
    
def main():
    x = input("첫번째 데이터를 입력해 주세요.")
    y = input("두번째 데이터를 입력해 주세요.")   
    
    su1 = int(x)
    su2 = int(y)
    
    addsum = add(su1, su2)
    subsum = sub(su1, su2)
    multisum = multi(su1, su2)
    divisum = divi(su1, su2)
    divisum2 = divi2(su1, su2)
    
    print("덧셈: ", addsum)
    print("뺄셈: ", subsum)
    print("곱셈: ", multisum)
    print("나눗셈(/): ", divisum)
    print("나눗셈(%): ", divisum2)
    
main()
