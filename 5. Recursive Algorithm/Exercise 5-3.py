# 자료구조와 함께 배우는 알고리즘 입문 <파이썬 편> 실습 5-3

# 순수한 재귀 함수 구현하기

def recur(n: int) -> int:
    """순수한 재귀 함수 recur의 구현"""
    if n > 0:
        recur(n - 1)
        print(n)
        recur(n - 2)

x = int(input('정숫값을 입력하세요.: '))

recur(x)
