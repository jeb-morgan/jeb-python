# 문자열 포매팅
from unittest.util import three_way_cmp

# 문자열 포매팅 방법

# 1. 숫자 포매팅
' I eat %d apples.' % 3

# 2. 문자열 포매팅
' I eat %s apples.' % 'three'

# 3. 변수 포매팅
number = 3
'I eat %d apples.' % number

# 4. 2개 이상의 값 넣기
number = 10
day = 'three'
'I ate %d apples. so I was sick for %s days.' %(number, day)


'''문자열 포맷 코드
%s : 문자열(string)
%c : 문자 1개(character)
%d : 정수(integer)
%f : 부동소수(floating-point)
%o : 8진수
%x : 16진수
%% : Literal %(문자 % 자체)'
'''

