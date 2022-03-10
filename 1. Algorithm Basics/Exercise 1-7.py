# 1부터 n까지 정수의 합 구하기 1(while문)

# 프로그램 설명
print('1부터 n까지 정수의 합을 구합니다.')

# n값 입력
n = int(input('n값을 입력하세요.: '))

# 기본값 설정
sum = 0
i = 1

# while문을 사용한 합계 구하기
while i <= n:
    sum += i
    i += 1

# 구한 합계 출력
print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')
