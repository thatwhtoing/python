# a부터 b까지 정수의 합 구하기 2

# 프로그램 설명
print('a부터 b까지 정수의 합을 구합니다.')

# 정수 입력
a = int(input('정수 a를 입력하세요.: '))
b = int(input('정수 b를 입력하세요.: '))

# a와 b를 오름차순으로 정렬
if a > b:
    a, b = b, a

# 기본값 설정
sum = 0

# a와 b까지 순차적으로 더해가는 for 문 (계산과정을 보기 쉽게 출력)
for i in range(a, b):
    print(f'{i} + ', end = '')
    sum += i

# 마지막 문장에 추가
print(f'{b} = ', end = '')
sum += b

# 합계를 출력
print(sum)

'''실습 1-10과 같이 if를 for 문 안에 입력하게 되면 else문은 마지막에만 실행되게 된다.
else문의 내용을 for 문 밖으로 빼내어 프로그램의 효율성을 높인다.

실습 1-10의 코드

for i in range(a, b + 1):
    if i < b:
        print(f'{i} + ', end = '')
    else:
        print(f'{i} = ', end = '')
'''
