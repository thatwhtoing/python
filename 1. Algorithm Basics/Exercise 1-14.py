# *를 n개 출력하되 w개마다 줄바꿈하기 1

# 프로그램 설명
print('*를 출력합니다.')

# 출력 변수 입력
n = int(input('몇 개를 출력할까요?: '))
w = int(input('몇 개마다 줄바꿈할까요?: '))

# n개의 *를 출력하는데 i를 w만큼 출력되면 개행하는 for 문
for i in range(n):
    print('*', end = '')
    if i % w == w - 1: # i를 w로 나누었을 때 나머지가 w - 1이면 '*'가 w개 출력된 것이다
        print()

# w개 만큼 출력되지 않은 마지막 줄에서 개행
if n % w:
    print()
