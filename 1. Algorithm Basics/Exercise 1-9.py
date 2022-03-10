# a부터 b까지 정수의 합 구하기(for 문)

# 프로그램 설명
print('a부터 b까지 정수의 합을 구합니다.')

# 정수값 입력
a = int(input('정수 a를 입력하세요.: '))
b = int(input('정수 b를 입력하세요.: '))

# a, b를 내림차순으로 정렬
if a > b:
    a, b = b, a

# 기본값 설정
sum = 0

# a부터 b까지 차례대로 더하기
for i in range(a, b + 1):
    sum += i

# 구한 합계 출
print(f'{a}부터 {b}까지 정수의 합은 {sum}입니다.')
