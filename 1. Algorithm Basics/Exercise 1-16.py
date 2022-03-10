# 1부터 n까지 정수의 합 구하기(n값은 양수만 입력받음)

# 프로그램 설명
print('1부터 n까지 정수의 합을 구합니다.')

# 양수가 입력되면 while 문을 종료, 0 이하의 값이 입력되면 while 문을 다시 실행
while True:
    n = int(input('n값을 입력하세요.: '))
    if n > 0:
        break

# 기본값 설정
sum = 0
i = 1

# 1부터 n까지의 합을 구하는 for 문
for i in range(1, n + 1):
    sum += i
    i += 1

# 합계 출
print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')
