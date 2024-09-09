# 문자열 포매팅
from numpy.ma.core import floor

# 문자열 안에 특정한 값을 바꿔야 할 경우에 사용
# ex) 시간에 따른 온도의 변화를 알려주는 프로그램을 작성할 때
# -> "현재는 %[온도] 도 입니다." % [온도]

# 문자열 포매팅 방법
# 포매팅에는 크게 3가지 방법이 있다.

'''
# 1. %코드 사용
'Python is %s.' % 'best'

# 2. format 함수 사용
'Python is {0}.' .format('best')

#3.f 문자열 포매팅 기능 사용
adj = 'best'
f'Python is {adj}'
'''

## 1. %코드 사용

# 1-1. 숫자 포매팅
'I eat %d apples.' % 3  # 'I eat 3 apples.' -> 3은 정수

# 1-2. 문자열 포매팅
'I eat %s apples.' % 'three' # 'I eat three apples.' -> three는 문자열

# 1-3. 변수 포매팅
number = 3
'I eat %d apples.' % number # 'I eat 3 apples.' -> 정수 3을 number라는 변수로 지정해 number를 3 대신 포매팅

# 1-4. 2개 이상의 값 넣기
number = 10
day = 'three'
'I ate %d apples. so I was sick for %s days.' %(number, day) # 'I ate 10 apples. so I was sick for three days.'


'''
- 문자열 포맷 코드
%s : 문자열(string)
%c : 문자 1개(character)
%d : 정수(integer)
%f : 부동소수(floating-point)
%o : 8진수
%x : 16진수
%% : Literal %(문자 % 자체)'
'''

# 포매팅 연산자 %d와 %를 쓸 때는 %%로 써야 한다.
'Loading is %d%' % 97 # -> Error 반환
'Loading is %d%%' % 97 # -> 'Loading is 97%'


# 1. 포맷 정렬

# 1-(1). 포맷 오른쪽으로 정렬
'%5s' % 'hi' #      hi,
# 전체 길이가 5개인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬, 그 앞은 모두 공백으로 남겨둔다.
# 즉, 전체 길이는 5개이며 , 공백은 3개이다. (hi가 두 글자이므로 5-2 == 3). / hi를 인덱싱하면 [3]:h / [4]:i

# 1-(2). 포맷 왼쪽으로 정렬
"%-5sjane." % 'hi' # 'hi   jane.'
# 전체 길이 5개, hi와 jane 사이 공백 3개.

#1-(3). 소수점 표현
'%0.4f' % 3.4121313 # 3.4121, 길이에 상관없이(0) 소수점 4번째 자리까지 표현(4), %0.4f는 0을 생략하여 %.4f처럼 사용하기도 함.
'%10.4f' % 3.4121313 #'    3.4213', 전체 길이 10개에서 공백 4개


## 2. format 함수 사용

#2-1. 숫자
'I eat {0} apples.' .format(3) # 'I eat 3 apples.'

#2-2. 문자열
'I eat {0} apples.' .format('three') # 'I eat three apples.'

#2-3. 변수
number = 3
'I eat {0} apples.' .format(number) # 'I eat 3 apples.'

#2-4. 2개 이상
number = 10
day = 'three'
'I ate {0} apples. so I was sick for {1} days.' .format(number, day) # I ate 10 apples. so I was sick for three days.

#2-5. 이름으로 넣기
'I ate {number} apples. so I was sick for {day] days.' .format(number = 10, day = 3) # 'I ate 10 apples. so I was sick for 3 days.'

#2-6. 인덱스와 혼용
'I ate {0} apples. so I was sick for {day} days.' .format(10, day = 3) # 'I ate 10 apples. so I was sick for 3 days.'

# 2. format 함수로 정렬

# 2-(1) 왼쪽 정렬
'{0:<5}'.format('hi') # 'hi     '

# 2-(2) 오른쪽 정렬
'{0:>5}'.format('hi') # '     hi'

# 2-(3) 가운데 정렬
'{0:^6}'.format('hi') # '  hi  '

#2-(4) 공백 채우기
'{0:=%10}'.format('hi') # '====hi===='

'{0:!<10}'.format('hi') # 'hi!!!!!!!!'

#2-(5) 소수점 표현하기
y = 3.421342
'{0:0.4f}'.format(y) # '3.4213'

'{0:10.4f}'.format(y) #    3.4213'

#2-(6) {} 표현하기
'{{ and }}' .format() # '{ and }'

##3.f 문자열 포매팅 기능 사용

#3-(1) 표현
name = '홍길동'
age = 30
f'나의 이름은 {name} 입니다. 나이는 {age} 입니다.' # '나의 이름은 홍길동입니다. 나이는 30입니다.'

age = 30
f'나는 내년이면 {age + 1}살이 된다.' # '나는 내년이면 31살이 된다.'

#3-(2) 딕셔너리
d = {'name':'홍길동', 'age':30}
(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다. ') # 나의 이름은 홍길동입니다. 나이는 30입니다.'

#3-(3) 정렬

# 왼쪽 정렬
f'{"hi":<10}'   #  'hi        '

# 오른쪽 정렬
f'{"hi":>10}'  # '        hi'

# 가운데 정렬
f'{"hi":^10}'  # '    hi    '

#3-(4) 공백 채우기
# 가운데 정렬하고 '=' 문자로 공백 채우기
f'{"hi":=^10}'   # '====hi===='
# 왼쪽 정렬하고 '!' 문자로 공백 채우기
f'{"hi":!<10}'   #  'hi!!!!!!!!'

#3-(4) 소수점
y = 3.42134234
# 소수점 4자리까지만 표현
f'{y:0.4f}'   # '3.4213'

# 소수점 4자리까지 표현하고 총 자리수를 10으로 맞춤
f'{y:10.4f}'   # '    3.4213'