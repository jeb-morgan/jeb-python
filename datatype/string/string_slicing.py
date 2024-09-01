# 문자열 슬라이싱
# 문자열 중 특정 범위의 문자열만을 추출해서 보고 싶을 때 사용

a = 'Life is short'

print(a[0:3]) # Lif
print(a[0:4]) # Life
# 0:3이 Life 를 추출하지 않는 이유 : 0 <= a < 3,
# 끝 번호를 포함하지 않기 때문.


print(a[3:]) # index 3부터 끝까지
print(a[:7]) # 처음부터 index 7까지
print(a[:]) # 처음부터 끝까지
print(a[3:-3]) # a[3]부터 a[-3]까지

# 문자열은 immutable 자료형이기 때문에, 대입해도 값을 바꿀 수 없다.
b = 'Pithon'
b[1] = 'y' # i를 y로 바꾸려고 하면 오류가 발생한다.

# 다만, 슬라이스를 이용해 아래와 같이 만들 수는 있다.
b = 'Pithon'
b[:1] # P
b[2:] # thon
p[:1] + 'y' + b[2:] # Python


#포맷 정렬
'%10s' % 'hi' #           hi