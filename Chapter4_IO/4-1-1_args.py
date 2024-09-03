# 입력값이 몇 개가 될지 알 수 없을 때, 여러 개의 입력값을 받을 때 : *args
from bisect import insort


def function(*args):
    '수행할 문장'
    ...

# 여러 개의 입력값을 받는 함수 만들기
def add_args(*args):
    result = 0
    for i in args:
        result = result + i
    return result

# *args 처럼 매개변수 이름 앞에 *을 붙이면 입력값을 전부 모아 튜플로 담아준다.
# ex) : add_args(1,2,3) 이면 args (1,2,3)이 된다.


