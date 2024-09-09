#문자 개수 세기 - count
#count 함수로 문자열 중 문자 b의 개수를 리턴
a = "hobby"
a.count('b') # 2


# 위치 알려 주기 1 - find
# find 함수로 문자열 중 문자 b가 처음으로 나온 위치를 반환, 만약 찾는 문자나 문자열이 존재하지 않는다면 -1을 반환
a = "Python is the best choice"
a.find('b') # 14
a.find('k') # -1

# 위치 알려 주기 2 - index
a = "Life is too short"
a.index('t') # 8

a.index('k')
'''
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: substring not found
'''
# index 함수로 문자열 중 문자 t가 맨 처음으로 나온 위치를 반환. 만약 찾는 문자나 문자열이 존재하지 않는다면 오류가 발생한다. 앞의 find 함수와 다른 점은 문자열 안에 존재하지 않는 문자를 찾으면 오류 발생


# 문자열 삽입 - join
# join 함수로 abcd 문자열의 각각의 문자 사이에 ‘,’를 삽입
# 문자열뿐만 아니라 앞으로 배울 리스트나 튜플도 입력으로 사용할 수 있음
",".join('abcd') # 'a,b,c,d'
",".join(['a', 'b', 'c', 'd']) # 'a,b,c,d'

# 소문자를 대문자로 바꾸기 - upper
# 문자열이 이미 대문자라면 아무런 변화도 일어나지 않음
a = "hi"
a.upper() # 'HI'

# 대문자를 소문자로 바꾸기 - lower
a = "HI"
a.lower() # 'hi'

# 왼쪽 공백 지우기 - lstrip
# 문자열 중 가장 왼쪽에 있는 한 칸 이상의 연속된 공백들을 모두 지움
a = " hi "
a.lstrip() # 'hi '


# 오른쪽 공백 지우기 - rstrip
# 문자열 중 가장 오른쪽에 있는 한 칸 이상의 연속된 공백을 모두 지움
a= " hi "
a.rstrip() # ' hi'

# 양쪽 공백 지우기 - strip
# 문자열 양쪽에 있는 한 칸 이상의 연속된 공백을 모두 지움수
a = " hi "
a.strip() # 'hi'


# 문자열 바꾸기 - replace
# replace(바뀔_문자열, 바꿀_문자열)처럼 사용해서 문자열 안의 특정한 값을 다른 값으로 치환
a = "Life is too short"
a.replace("Life", "Your leg")  # 'Your leg is too short'

# 문자열 나누기 - split
a = "Life is too short"
a.split() # ['Life', 'is', 'too', 'short']
b = "a:b:c:d"
b.split(':') # ['a', 'b', 'c', 'd']
# a.split()처럼 괄호 안에 아무 값도 넣어 주지 않으면 공백([Space], [Tab], [Enter])을 기준으로 문자열을 나누어 줌준. 만약 b.split(':')처럼 괄호 안에 특정 값이 있을 경우에는 괄호 안의 값을 구분자로 해서 문자열을 나누어 주고, 이렇게 나눈 값은 리스트에 하나씩 들어감

# 문자열은 immutable이다.
a = 'hi'
a.upper() # 'HI'
print(a) # 'hi'
# a.upper()를 수행하더라도 a 변수의 값은 변하지 않는다. a.upper()를 실행하면 upper 함수는 a 변수의 값 자체를 변경하는 것이 아닌 대문자로 바꾼 값을 리턴하기 때문이다.

# a 값 자체를 변경하고 싶다면 아래와 같이 사용:
a = a.upper()
print(a) # 'HI'