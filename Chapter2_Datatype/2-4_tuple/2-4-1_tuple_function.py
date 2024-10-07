# 인덱싱
t1 = (1, 2, 'a', 'b')
t1[0] # 1
t1[3] # 'b'


# 슬라이싱
t1 = (1, 2, 'a', 'b')
t1[1:] #(2, 'a', 'b')


# 튜플 더하기
t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
t3 = t1 + t2
t3 # (1, 2, 'a', 'b', 3, 4)
# t1, t2 튜플의 요솟값이 바뀌는 것은 아니나, t1, t2 튜플을 더하여 새로운 튜플 t3를 생성할 수 있다.

# 튜플 곱하기
t2 = (3, 4)
t3 = t2 * 3
t3 # (3, 4, 3, 4, 3, 4)

# 튜플 길이 구하기
t1 = (1, 2, 'a', 'b')
len(t1) # 4
# 튜플은 요솟값을 변경할수 없기 때문에 sort, insert, remove, pop과 같은 내장 함수가 없다.