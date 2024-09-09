# 문자열 자료형


# 문자열 명시 방법

# 1. 큰따옴표
"Hello World"

# 2. 작은따옴표
'Hello World'

# 3. 큰따옴표 3개 연속 사용
"""Hello World"""

# 4. 작은따옴표 3개 연속 사용
'''Hello World'''


# 문자열 안에 따옴표가 있는 경우

# 1. 문자열에 작은따옴표가 포함되어 있을 경우 큰따옴표로 둘러싼다.
guido1 = "Python's father"

# 2. 문자열에 큰따옴표가 포함되어 있을 경우 작은따옴표로 둘러싼다.
guido2 = 'Guido says, "Python is very easy."'

# 출력
print(guido1) # Python's father
print(guido2) # Guido says, "Python is very easy."

# 3. 역슬래시 사용
guido1 = "Python\'s father"
guido2 = 'Guido says, \"Python is very easy.\"'


# 여러 줄인 문자열을 변수에 대입하려는 경우
'Life is short'
'You need Python'

# 1. \n (줄바꿈) 사용
multiline = 'Life is short\nYou need Python'

# 2. 연속된 따옴표 3개 사용
"""Life is short
You need Python"""

'''Life is short
You need Python'''
