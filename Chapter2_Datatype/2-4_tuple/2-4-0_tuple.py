# 튜플 (tuple)

# 튜플은 ()로 생성
# 리스트는 요솟값의 생성, 삭제, 수정이 가능하지만, 튜플은 요솟값을 바꿀 수 없다.
# 프로그램이 실행되는 동안 요솟값이 항상 변하지 않는 조건을 걸어야 할 경우 튜플을 사용한다



# 튜플 생성 방법
t1 = ()
t2 = (1,) # t2 = (1,)처럼 단지 1개의 요소만을 가질 때는 요소 뒤에 쉼표(,)를 반드시 붙여야 한다
t3 = (1, 2, 3)
t4 = 1, 2, 3 # t4 = 1, 2, 3처럼 소괄호(())를 생략해도 된다.
t5 = ('a', 'b', ('ab', 'cd'))

# 튜플 요솟값을 삭제하려 할 때
t1 = (1, 2, 'a', 'b')
del t1[0]
'''
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'tuple' object doesn't support item deletion
'''
# 튜플은 요솟값은 지울 수 없다


# 튜플 요솟값을 변경하려 할 때
t1 = (1, 2, 'a', 'b')
t1[0] = 'c'
'''
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
'''
# 튜플의 요솟값은 변경할 수 없다