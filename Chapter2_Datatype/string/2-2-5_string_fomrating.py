# 문자열 포매팅

# 문자열 안에 특정한 값을 바꿔야 할 경우에 사용
# ex) 시간에 따른 온도의 변화를 알려주는 프로그램을 작성할 때
# -> "현재는 %[온도] 도 입니다." % [온도]

# 문자열 포매팅 방법

# 1. 숫자 포매팅
'I eat %d apples.' % 3  # 'I eat 3 apples.' -> 3은 정수

# 2. 문자열 포매팅
'I eat %s apples.' % 'three' # 'I eat three apples.' -> three는 문자열

# 3. 변수 포매팅
number = 3
'I eat %d apples.' % number # 'I eat 3 apples.' -> 정수 3을 number라는 변수로 지정해 number를 3 대신 포매팅

# 4. 2개 이상의 값 넣기
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


# 포맷 코드와 숫자 함께 사용하기

# 1. 포맷 정렬

# 포맷 오른쪽으로 정렬
'%5s' % 'hi' #      hi,
# 전체 길이가 5개인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬, 그 앞은 모두 공백으로 남겨둔다.
# 즉, 전체 길이는 5개이며 , 공백은 3개이다. (hi가 두 글자이므로 5-2 == 3). / hi를 인덱싱하면 [3]:h / [4]:i

# 포맷 왼쪽으로 정렬
"%-5sjane." % 'hi' # 'hi   jane.'

# 전체 길이 5개, hi와 jane 사이 공백 3개.

#2. 소수점 표현


