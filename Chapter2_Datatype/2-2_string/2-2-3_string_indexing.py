# 문자열 인덱싱

# indexing :
# 무엇인가를 '가리킨다' 라는 의미,
# 파이썬에서는 문자열 안의 특정한 값을 뽑아 내는 작업을 말한다.


a = 'Life is short'
#    0123456789101112 (인덱싱은 0부터 시작하며, 스페이스 또한 인덱싱에 포함된다.(아래 참조))
# [0] : 'L' / [1] : 'i' / [2] : 'f' / [3] : 'e' / [4] : ' ' / [5] : 'i'  ...

print(a[3]) # e
print(a[-1]) # t (-1은 뒤에서부터 셌을 떄 첫 번째가 되는 문자)
print(a[-2]) # r
