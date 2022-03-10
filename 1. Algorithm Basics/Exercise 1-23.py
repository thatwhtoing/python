# 오른쪽 아래가 직각인 이등변 삼각형으로 * 출력하기

# 프로그램 설명
print('오른쪽 아래가 직각인 이등변 삼각형을 출력합니다.')

# 변의 길이를 입력
n = int(input('짧은 변의 길이를 입력하세요.: '))

# 공백을 출력하고 *를 출력하는 For 문
for i in range(n):
    for _ in range(n - i - 1):
        print(' ', end = '')
    for _ in range(i + 1):
        print('*', end = '')
    print()
