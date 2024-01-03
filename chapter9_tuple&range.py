
# tuple 자료형
# 값의 변화(추가나 수정)가 자주 발생하면 리스트 자료형을 씁니다.
# 반대이면, 그렇지 않으면 튜블형(고정된 데이터만 사용)을 사용합니다.
# 왜? 튜플은 값의 변경이 안됩니다.
# 처음 만들어진 상태 그대로 사용해야 합니다.
# 튜플 : ( ), list : [ ]
# t1 = ()
# t2 = (10, )
# t3 = (10, 20, 30)
# t4 = 1, 2, 3
# t5 = ('a', 'b', ('ab', 'cd'))

t1 = (1, 2, 'a', 'b')
#del t1[2]
#TypeError: 'tuple' object doesn't support item deletion

t1 = (1, 2, 'a', 'b')
#t1[0] = 'c'
#TypeError: 'tuple' object does not support item assignment

#1.indexing
t1 = (1, 2, 'a', 'b')
#t1 = [1,2,'a','b']
print(t1[0]) # 1
print(t1[3]) # 'b'
print(type(t1)) # <class 'tuple'>

#2.slicing
t1 = (1, 2, 'a', 'b')
print(t1[1: ]) # (2, 'a', 'b')

#3.tuple 더하기
t2 = (30,40)
print(t1 + t2) # (1, 2, 'a', 'b', 30, 40), 연결 연산자의 역할 

#4.tuple 곱하기
print(t2 * 3) # (30, 40, 30, 40, 30, 40)

#5.길이 구하기
t1 = (1, 2, 'a', 'b')
t2 = [1,2,'a','b']
print(len(t1)) # 4
print(len(t2)) # 4

#아래의 string형과 list형 으로부터 tuple형을 생성하세요.
str_red = 'Red'
list_color = ['Red', 'Yellow', 'Pink']

tuple_Red = ('R', 'e', 'd')
tuple_color = ('Red', 'Yellow', 'Pink')

tuple_Red2 = str_red
tuple_color2 = tuple(list_color)

print(tuple_Red2) # Red
print(type(tuple_Red2)) # String type
print(tuple_color) # ('Red', 'Yellow', 'Pink')
print(tuple_color2) # ('Red', 'Yellow', 'Pink')

#어떤 고등학교에서 평소에 영어, 수학, 과학, 사회 4과목을
#시험을 봅니다. 하지만 올해에는 수학 과목을 과제로 대체하려고
#합니다. 이때, 수학 과목만 과제로 대체한 리스트를 출력하는
#프로그램을 작성합니다. 단, 원래 과목 목록은 변하지 않습니다.

# list인 경우 전제 1
subject = ['영어', '수학', '과학', '사회']
examtest = list(subject)
examtest[1] = '과제'
print(examtest) # 영어, 과제, 과학, 사회 
print(subject) # 영어, 수학, 과학, 사회

# list인 경우 전제 2
subject = ['영어', '수학', '과학', '사회']
examtest[1] = '과제'
print(examtest)

# tuple인 경우
subject = ('영어', '수학', '과학', '사회')
subject[1] = '과제'
print(subject)

TypeError                                 Traceback (most recent call last)
~\AppData\Local\Temp\ipykernel_11096\1509262810.py in <module>
      1 # tuple인 경우
      2 subject = ('영어', '수학', '과학', '사회')
----> 3 subject[1] = '과제'
      4 print(subject)

TypeError: 'tuple' object does not support item assignment

# tuple인 경우 2
subject = ['영어', '수학', '과학', '사회']
examtest = list(subject)
subject[1] = '과제'
print(subject)

# 가변적인 데이터는 리스트형으로, 고정 불변적인 데이터는 튜플형으로 처리 합니다.
#  기준? 요구사항에 따라서 다릅니다.

# 문제> 요구사항
#어느 문구점에서 연필은 200원, 펜은 800원, 지우개는 500원,
# 자는 300원으로 판매를 합니다.
# 이 목록을 list 형태로 만들어 보세요.
list_1 = ['pencil', 'pen', 'eraser', 'ruler']
list_2 = [200, 800, 500, 300]
print(list_1)
print(list_2)

tuple_1 = tuple(list_1) # ('pencil', 'pen', 'eraser', 'ruler')
tuple_2 = tuple(list_2) # (200, 800, 500, 300)

print(tuple_1)
print(tuple_2)


tuple1 = ('pencil', 'pen', 'eraser', 'ruler')
tuple2 = (200, 800, 500, 300)

print(type(tuple1))
print(tuple2)

x = list(tuple1)
x2 = list(tuple2)

print(type(x))
print(x2)


#연습문제 9-1

#문제1> 3개의 숫자를 입력받아서 su 객체에 저장하고, 반환하여
# 출력하는 프로그램을 작성하세요. 함수 이용


def to_list(data):
    su = [ ]

    for i in data:
        su.append(i)

    return su   

def main():

    x = int(input("정수형 데이터 입력: "))
    y = int(input("정수형 데이터 입력: "))
    z = int(input("정수형 데이터 입력: "))

    dataset = (x, y, z)
    
    num = to_list(dataset)
    print(num)
   
main()

--------------------------------------------

def math():
    x = int(input("정수를 입력해주세요"))
    y = int(input("정수를 입력해주세요"))
    z = int(input("정수를 입력해주세요"))
    list = []
    list.append(x)
    list.append(y)
    list.append(z)
    return list
result = math()
print(f"result 배열안에 요소는 다음과 같습니다. {result[0]},{result[1]},{result[2]}")


ds = ("hello")
ds = to_list(ds)
print(ds) # ['h', 'e', 'l', 'l', 'o']


#문제2> 2차원 배열 형태로 문자열과 숫자를 한쌍으로 n개를 저장하고,
# 중간에 2번 인덱스에 같은 형태의 다른 데이터를 추가하고,
# 마지막에 같은 형태의 다른 데이터를 추가하여 출력하세요.

#          [0][0]    [0][1]   [0][2]
sungjuk = [['최진혁', 'Python', 100], ['진형민', 'Python', 99],['윤홍일', 'Python', 98]]
sungjuk.insert(2, ['조서연', 'Python', 96])
sungjuk.append(['서동혁', 'Python', 93])

print(sungjuk)
  
print(sungjuk[0][0])
print(sungjuk[0][1])
print(sungjuk[0][2]) 

list1 = [['연필', 200], ['펜', 800], ['지우개', 500], ['자', 300]]
print(f"기존 리스트 : {list1}")
list1.insert(2,["프리미엄 지우개",600])
list1.insert(len(list1)-1, ["기타",9999])
print(f"변경된 리스트 : {list1}")


# tuple을 list구조로 감싸면, 수정이 가능한 데이터가 됩니다.
#         [0][0] [0][1]    [1][0]  [1][1]    [2][0]   [2][1]
frns = [('동수', 131120), ('진우', 130312), ('선영', 130904)]
print(frns)
frns[1] = ('수진', 131122)
print(frns)        

for i in range(1,11):
    print(i, end=' ')    
    
print(type(i))    


lst = list(range(1, 10))
print(lst)

tp1 = tuple(range(1, 10))
print(tp1)

----------------------------------
#연습문제 09-2
#문제1)
# 1,2,3,4,5......99,100, 99, 98......3,2,1을 출력하는
#프로그램을 작성하세요.
for i in range(9, 0, -1):
    print(7 * i, end = ' ') # 63 56 49 42 35 28 21 14 7

#문제2)
tp = tuple(range(1, 100, 1)) + tuple(range(100, 0, -1))
print(tp)

for i in range(101):
    print(i, end= ",")
for i in range(1,100):
    print(100-i, end =",")

for i in range(1, 101):
    print(i, end= ",")

for i in range(99,0, -1):
    print(i, end =",")


#(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
# 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
# 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
# 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
# 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96,
# 97, 98, 99, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85,
# 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66,
# 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47,
# 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28,
# 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9,
# 8, 7, 6, 5, 4, 3, 2, 1)

