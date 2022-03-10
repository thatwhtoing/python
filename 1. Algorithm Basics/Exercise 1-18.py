# 10~99 사이의 난수 n개 생성하기(13이 나오면 중단)

# 랜덤 라이브러리
import random

# 출력할 난수의 개수를 입력
n = int(input('난수의 개수를 입력하세요.: '))

# 0부터 n-1까지 n번 반복
for _ in range(n):
    r = random.randint(10, 99)
    print(r, end = ' ')
    if r == 13: # 난수로 13이 나오면 프로그램을 중단
        print('\n프로그램을 중단합니다.')
        break

else:
    print('\n난수 생성을 종료합니다.')
