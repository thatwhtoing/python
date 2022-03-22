# 자료구조와 함께 배우는 알고리즘 입문 <파이썬 편> 실습 5-1

# 양의 정수 n의 팩토리얼 구하기

def factorial(n: int) -> int:
    """양의 정수 n의 팩토리얼값을 재귀적으로 구함"""
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1

if __name__ == '__main__':
    n = int(input('출력할 팩토리얼값을 입력하세요.: '))
    print(f'{n}의 팩토리얼은 {factorial(n)}입니다.')
