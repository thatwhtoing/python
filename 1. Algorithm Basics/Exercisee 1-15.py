# *를 n개 출력하되 w개마다 줄바꿈하기 2

# 프로그램 설명
print('*를 출력합니다.')

# n과 w 변수 입력
n = int(input('몇 개를 출력할까요?: '))
w = int(input('몇 개마다 줄바꿈할까요?: '))

# n // w: n을 w로 나누었을 때 몫
# n이 10이고, w가 3이라면 n // w는 3이다
# 0, 1, 2로 3회 반복된다
'''
***
***
***
'''

for _ in range(n // w):
    print('*' * w)

# n % w: n을 w로 나누었을 때 나머지
# 나머지 개수만큼 '*'를 출력한다
rest = n % w
if rest:
    print('*' * rest)