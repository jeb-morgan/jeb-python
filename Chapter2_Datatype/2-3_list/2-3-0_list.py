# 리스트

#TODO :: 리스트 만드는 법 항목 보완
# 리스트 만드는 법
list1 = ['a','b','c','d',1,'doremi', ['a']]


# 리스트의 종류
a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

# 리스트 인덱싱
list2 = ['a','b','c','d',1,'doremi',2, ['a']]
print(list2[0]) # 'a'
print(list2[7]) # ['a']
print(list2[-1]) # ['a']
print(list2[0] + list2[4]) # # TypeError: can only concatenate str (not "int") to str
print(list2[4] + list2[6]) # 3
print(list2[-1][0]) # 'a'

# 리스트 슬라이싱
list3 = [1, 2, 3, 4, 5]
print(a[0:2]) # [1, 2]
b = list3[:2] # [1, 2]
c = list3[2:] # [3, 4, 5]

#TODO :: 리스트 심화 보완하기

## 리스트 연산하기

#리스트 더하기(+)
# 리스트 사이에서 +는 2개의 리스트를 합치는 기능
a1 = [1, 2, 3]
b1 = [4, 5, 6]
print(a1 + b1) # [1, 2, 3, 4, 5, 6]

#리스트 반복하기(*)
a2 = [1, 2, 3]
print(a2 * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 리스트 길이 구하기 ***
a = [1, 2, 3]
len(a) # 3

#리스트의 값 수정하기
a = [1, 2, 3]
a[2] = 4
print(a) # [1, 2, 4]

