# a부터 b까지 정수의 합 구하기 1

# 프로그램 설명
print('a부터 b까지 정수의 합을 구합니다.')

# 정수 입력
a = int(input('정수 a를 입력하세요.: '))
b = int(input('정수 b를 입력하세요.: '))

# a, b를 오름차순으로 정렬
if a > b:
    a, b = b, a

# 기본값 설정
sum = 0

# a부터 b까지 순차적으로 더해가는 for 문 (계산과정을 보기 쉽게 출력)
for i in range(a, b + 1):
    if i < b:
        print(f'{i} + ', end = '') # i가 b보다 작으면 +를 표시
    else:
        print(f'{i} = ', end = '') # i가 b와 같으면 =를 표시
    sum += i

# 합계를 출력
print(sum)
