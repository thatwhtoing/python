# +와 -를 번갈아 출력하기 1

# 프로그램 설명
print('+와 -를 번갈아 출력합니다.')

# n값 입력
n = int(input('몇 개를 출력할까요?: '))

# 1부터 n 중의 값이 홀수인지 짝수인지에 따라 -, + 값 출력
for i in range(n):
    if i % 2: # i가 짝수이면 '-' 출력
        print('-', end = '')
    else: # i가 홀수이면 '+' 출력
        print('+', end = '')

# 마지막 출력 후 개행
print()