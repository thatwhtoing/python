# 자료구조와 함께 배우는 알고리즘 입문 <파이썬 편> 실습 2-4

# 배열 원소의 최댓값을 구해서 출력하기(웟솟값을 난수로 생성)

import random
from max import max_of

# 프로그램 설명
print('난수의 최댓값을 구합니다.')

# 입력
num = int(input('난수의 개수를 입력하세요.: '))
lo = int(input('난수의 최솟값을 입력하세요.: '))
hi = int(input('난수의 최댓값을 입력하세요.: '))

x = [None] * num        # 원소 수가 num인 리스트를 생성

for i in range(num):
    x[i] = random.randint(lo, hi)   # lo 이상 hi 이하인 정수 난수를 반환

print(f'{(x)}')
print(f'이 가운데 최댓값은 {max_of(x)}입니다.')
