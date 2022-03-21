# 자료구조와 함께 배우는 알고리즘 입문 <파이썬 편> 실습 2-2

# 시퀀스 원소의 최댓값 출력하기

from typing import Any, Sequence

# 최댓값을 구하는 함수 정의
def max_of(a: Sequence) -> Any:
    """시퀀스형 a 원소의 최댓값을 반환"""
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum

# 최댓값을 구하려는 입력 받기
if __name__ == '__main__':
    print('배열의 최댓값을 구합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요.: '))

    print(f'최댓값은 {max_of(x)}입니다.')
