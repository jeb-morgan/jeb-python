# 함수

"""
함수를 사용하는 경우
1. 반복되는 내용이 있을 경우
-> '반복적으로 사용되는 가치 있는 부분' 을 묶어 입력값을 주었을 때 특정값을 리턴하도록 작성

2. 프로그램을 기능 단위의 함수로 분리할 때
-> 프로그램의 흐름과 오류 발생 지점을 직관적으로 확인하기 편함.
"""
from distutils.command.build import build
from smtplib import bCRLF

from fontTools.colorLib.builder import buildCPAL


# 함수의 구조
def function(parameter): #parameter(매개변수 : 함수에 입력으로 전달되는 값을 받는 변수)
    '수행 할 문장 1'
    '수행 할 문장 2'
    ...

def add1(a, b):
    return a + b
# 이 함수의 이름은 add이고, 입력으로 a, b 2개의 값을 받으며 리턴값은 입력값 2개를 더한 값이다.

def add2(a, b):
    a = 3
    b = 4
    return a + b


# 매개변수와 인수

# 매개변수 (parameter) : 함수에 입력값으로 전달된 값을 받는 변수
# 인수(argument) : 함수를 호출할 때 전달하는 입력값
def add (a, b): # a, b는 매개변수
    return a + b

print(add(3,4)) # 3, 4는 인수

# 함수 형태 4가지

# 1. 일반적인 함수 (입력값 o, 리턴값 o)
def one(parameter):
    '수행 문장'
    return '리턴값'

# ex)
def add(a, b):
    result = a + b
    return result

# 입력값, 리턴값이 없는 함수 호출방법 : 리턴값을 받을 변수 = 함수 이름(인수 1, 인수 2...)
a = add(3,4)
print(a)

#2. 입력값이 없는 함수 (입력값 x, 리턴값 o)
def say():
    return 'hi'

# 입력값 없는 함수 호출방법 : 리턴값을 받을 변수 = 입력값 없는 함수의 이름()
ya = say()
print(ya)  # 입력값 없이 'hi'라는 문자열만 리턴한다.


#3. 리턴값이 없는 함수 (입력값 o, 리턴값 x)
def add(a ,b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

# 리턴값이 없는 함수 호출방법 : 함수 이름(인수1, 인수2...)
add(3,4) # 리턴값이 없는 함수는 호출해도 리턴값이 없음

# 리턴값과 print문은 다르다.
# print는 함수의 구성 요소 중 하나인 수행하는 문장에 해당할 뿐, return 과는 엄연히 다르다.

# 리턴값 유무 확인하기
a = add(3, 4) # add 함수의 리턴값을 a에 대입
print(a)   # None , a 변수에 None을 리턴


# 4. 입력값, 리턴값이 모두 없는 함수 ( 입력값 x, 리턴값 x )
def say():
    print('hi')

# 입력값, 리턴값이 모두 없는 함수 호출방법 : 함수이름()
say()


# 매개변수를 지정하여 호출하기
def sub(a, b):
    return a - b

result1 = sub (a = 7, b = 3) # a에 7, b에 3을 지정
result2 = sub (b = 3, a= 7) # 순서 상관없이 매개변수 지정 가능
print(result1)
print(result2)