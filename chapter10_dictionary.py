
#list, tuple : 중복을 허용 합니다. 순서가 있습니다.

# set, dictionary : 집합
# 중복을 허용하지 않습니다.
# 순서가 중요하지 않습니다.
# indexing을 지원하지 않는다.

#dictionary(key : value) => JSON(javascript, jquery, jsp, spring..)
# {key1:value1, key2:value2,......}

a = {1:'hi'}
print(a) # {1: 'hi'}

a = {1:'a'}
a[2] = 'b' #{2:'b'}
print(a) # {1: 'a', 2: 'b'}

a['name'] = 'hyun'
print(a) # {1: 'a', 2: 'b', 'name': 'hyun'}

a[3] =[10,200,300]
print(a) # {1: 'a', 2: 'b', 'name': 'hyun', 3: [10, 200, 300]}

# 디션어리요소 삭제하기
del a[1]
print(a) # {2: 'b', 'name': 'hyun', 3: [10, 200, 300]}


#문제> 국어 100점, 영어 98점, 수학 25점을 디션어리 형태로 저장 및
# 출력하는 프로그램을 작성하세요.

sungjuk = {'kor': 100, 'eng': 98, 'mat': 25}
print(sungjuk)
print(sungjuk['kor'])

dic = {2: 'b', 'name': 'hyun', 3: [10, 200, 300]}
print(dic[2]) # 'b'
print(dic['name']) # 'hyun'
print(dic[3]) # [10, 200, 300]

#같은키를 가진 여러개의 값이 존재한다면 마지막 값만 기억합니다.
sungjuk = {'kor': 100, 'eng': 98, 'mat': 25, 'kor': 45}
print(sungjuk)
print(sungjuk['kor'])

a = {[1, 2]: 'hi'}
#print(a) # TypeError: unhashable type: 'list'

dic = {2: 'b', 'name': 'hyun', 3: [10, 200, 300]}
print(dic.keys()) # dict_keys([2, 'name', 3])

for k in dic.keys():
    print(k) # 2 name 3
    
print(list(dic.keys())) # [2, 'name', 3]
print(list(dic.values())) # ['b', 'hyun', [10, 200, 300]]

#문제> 국어 100점, 영어 98점, 수학 25점을 디션어리 형태로 저장 및
# 출력하는 프로그램을 작성하세요.

sungjuk = {'kor': 100, 'eng': 98, 'mat': 25, 'kor': 45}

print(sungjuk.keys()) # dict_keys(['kor', 'eng', 'mat'])

print(sungjuk.values()) # dict_values([45, 98, 25])

print(list(sungjuk.keys())) # ['kor', 'eng', 'mat']

print(sungjuk.items()) # dict_items([('kor', 45), ('eng', 98), ('mat', 25)])



#key와 value를 동시에 출력하기 
print(dic.items())
# dict_items([(2, 'b'), ('name', 'hyun'), (3, [10, 200, 300])])

#key와 value 삭제하기
dic.clear()
print(dic) # {}
print(dic.items()) # dict_items([])

dic = {2: 'b', 'name': 'hyun', 3: [10, 200, 300]}
print(dic.get(2)) # b
print(dic.get(3)) # [10, 200, 300]

print(dic.get('b')) # None

print(2 in dic) # True
print('name' in dic) # True


# 요구사항
#어느 문구점에서 연필은 200원, 펜은 800원, 지우개는 500원,
# 자는 300원으로 판매를 합니다.
# 이 목록을 list 형태로 만들어 보세요.

list_1  = ['pencil', 'pen', 'eraser', 'ruler']
list_2 = [200, 800, 500, 300]

tuple_1 = tuple(list_1)
tuple_2 = tuple(list_2 )

print(list_1) # ['pencil', 'pen', 'eraser', 'ruler']
print(list_2) # [200, 800, 500, 300]
print(tuple_1) # ('pencil', 'pen', 'eraser', 'ruler')
print(tuple_2) # (200, 800, 500, 300)

#          key : value
dict = {"pencil":200, "pen":800, "eraser":500, "ruler":300}
print(dict)
# {'pencil': 200, 'pen': 800, 'eraser': 500, 'ruler': 300}

dict2 = list(dict.values())
print(dict2) # [200, 800, 500, 300]

#print(list(dict.values())) # [200, 800, 500, 300]

dict3 = list(dict.keys())
print(dict3) # ['pencil', 'pen', 'eraser', 'ruler']


#quiz) 커피숍에 4가지 메뉴를 있습니다.
#americano, cappuccino, latte, ade 등이 있는데,
#가격은 2700원, 2000원, 3500원, 4000원 입니다.
#이 목록을 dictionary로 작성하고, americano와 latte가 있는지
# 확인하여 출력하세요.

list_menu  = {"americano":2700, "cappuccino":2000, "latte":3500, "ade":4000}

print("americano" in list_menu.keys()) # True
print("latte" in list_menu.keys())  # True

for menu, price in list_menu.items():
    print(menu, ':', price, '원')

#americano : 2700 원
#cappuccino : 2000 원
#latte : 3500 원
#ade : 4000 원


------- 집합 자료형 -----------------

s1 = set([1,2,3])
print(s1) # {1, 2, 3}

s2 = set("hello")
print(s2) # {'h', 'e', 'o', 'l'}


s1 = set([10, 20, 30])
l1 = list(s1)
print(l1) # [10, 20, 30]

t1 = tuple(s1)
print(t1) # (10, 20, 30)

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

#교집합 
print(s1 & s2) # {4, 5, 6}
print(s1.intersection(s2)) # {4, 5, 6}

#합집합 
print(s1 | s2) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1.union(s2)) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

#차집합
print(s1 - s2) # {1, 2, 3}
print(s2 - s1) # {8, 9, 7}

print(s1.difference(s1)) # set()
print(s2.difference(s2)) # set()

#1개의 값을 추가하기
s1 = set([100,200,300])
s1.add(400)
print(s1) # {200, 100, 400, 300}
s1.add(400) #중복 허용 X 테스트 
print(s1) # {200, 100, 400, 300}

#여러개의 값을 추가하기
s1 = set([1000, 2000, 3000])
s1.update([4000, 5000, 6000])
print(s1) # {4000, 1000, 5000, 2000, 6000, 3000}

#특정값을 제거하기
s1 = set([1000, 2000, 3000])
s1.remove(2000) 
print(s1) # {1000, 3000}

#boolean Type : True(참), False(거짓)
a = True
b = False
print(type(a)) # <class 'bool'>
print(type(b)) # <class 'bool'>

str = 'hello'
print(type(str)) # <class 'str'>

number = 100
print(type(number)) # <class 'int'>

number2 = 100.123456
print(type(number2)) # <class 'float'>

print(1 == 1) # True
print(2 > 1) # True
print(2 < 1) # False


a = [1,2,3,4]
while a:
    print(a.pop()) # stack: LIFO, 4 3 2 1

if[1,2,3]:
    print("참")
else:
    print["거짓"]
    
print(bool('python')) # True

print(bool('')) # False
   
#메모리 주소값 확인 : id()
a = [1,2,3]
print(id(a)) # 1700430969800 => pointer(C)

b = [100,200,300]
print(id(b)) # 1859769818184

#list copy : (배열 복사) => Deep Copy
a = [10,20,30]
b = a # C언어적 표현: b = &a
print(id(a)) # 3134620061192, pointer value
print(id(b)) # 3134620061192

# a = b = a[0] = b[0] = &a[0] = &b[0] = &a[0][0] = &b[0][0] ...

print(a is b) # True

a[1] = 4
print(a) #[10, 4, 30]
print(b) #[10, 4, 30]

b[2] = 500
print(b) #[10, 4, 500]
print(a) #[10, 4, 500]

#범위지정 연산자 
a = [11, 22, 33]
b = a[ : ]
print(b) # [11, 22, 33]
a[1] = 44
print(a)#[11, 44, 33]
print(b)#[11, 22, 33]

print(id(a)) #1997410687816
print(id(b)) #1997410688584

#copy 모듈 사용하기
from copy import copy
a = [11, 22, 33]
b = copy(a)
print(b) # [11, 22, 33]

print(id(a)) #1539286970440
print(id(b)) #1539286982152

a, b = ('python', 'life')
print(a) # python
print(b) # life

(a, b) = 'python', 'life'
print(a) # python
print(b) # life

[a, b] = ['python', 'life']
print(a) # python
print(b) # life

print(a is b) # False, 서로 다른 주소값을 지니는 객체

a = b = 'python'
print(a) #python
print(b) #python

# 보통은 생략 하지만,
# 필요에 따라서 사용 가능합니다.
# a=b=sum=0
a = 100
b = 300
sum = a + b
print(sum) # 400

#데이터 내용 변경하기
a = 100
b = 500
a,b = b,a
print(a)#500
print(b)#100

x = 10
y = 20
temp = 0
temp = x
x = y
y = temp
print(x) #20
print(y) #10

---------------------------------

#연습문제 12-1

#문제1)
dc = {'새우깡': 700, '콘치즈': 850, '꼬깔콘': 750}
if '홈런볼' not in dc:
	dc['홈런볼'] = 900

#dc
#{'새우깡': 700, '콘치즈': 850, '꼬깔콘': 750, '홈런볼': 900}

#문제2)
for i in dc:
    dc[i] += 100
	
#dc
#{'새우깡': 800, '콘치즈': 950, '꼬깔콘': 850, '홈런볼': 1000}


#문제3)
 if '콘치즈' in dc:       # ‘콘치즈’ 있으면
 del dc['콘치즈']       # ‘콘치즈’ 삭제

dc
#{'새우깡': 800, '꼬깔콘': 850, '홈런볼': 1000}
 
if '치즈콘' not in dc:       # ‘치즈콘’ 없으면
dc['치즈콘'] = 950       # ‘치즈콘’ 추가

dc
#{'새우깡': 800, '꼬깔콘': 850, '홈런볼': 1000, '치즈콘': 950}


dc = {'새우깡': 700, '콘치즈': 850, '꼬깔콘': 750}
if '홈런볼' not in dc:
	dc['홈런볼'] = 900

dc

-----되새김 문제 p.116

# 문제 1
subject={'국어': 80 , '영어': 75, '수학' : 55}
print(f"평균 : {(subject['국어']+subject['영어']+subject['수학'])/3}")

# 문제 2
result = 13%2
if result==1:
    print("13은 홀수입니다.")
else:
    print("13은 짝수입니다.")

# 문제 3
num = "881120-1068234"
result = num.split('-')
print(result[0])
print(result[1])

# 문제4
num2 = result[1]
print(f"해당하는 주민의 성별 코드는 {num2[0:1]}")

# 문제 5
a = "a:b:c:d"
b = a.replace(':','#')
print(b)

# 문제6
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

# 문제 7
a = ['life','is','too','short']
result =" ".join(a)
print(result)

# 문제 8
a = (1,2,3)
a = a + (4, )
print(a)

# 문제 9
a['name'] = 'ptyhon'
a[('a', )] = 'ptyhon'
a[[1]] = 'ptyhon'
a[250] = 'ptyhon'
# a[[1]] = 'python'은 에러 딕셔너리 키로 리스트는 사용할 수 없다.

# 문제 10
a ={'A':90,'B':80,'C':70}
result = a.pop('B')
print(a)
print(result)

# 문제 11
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
b = list(aSet)
print(b)

# 문제 12
a = b = [1,2,3]
a[1] = 4
print(b)
# a와 b를 각각 선언한 것이 아닌 동시에 같은 값으로 선언했기 때문에 메모리상에서 같은 주소를 공유하고 있음 따라서 a의 값을 변경하면 메모리에 저장된 값도 변경되기 때문에 b의 값도 변경됨







