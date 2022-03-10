# 왼쪽 아래가 직각인 이등변 삼각형으로 * 출력하기

# 프로그램 설명
print('왼쪽 아래가 직각인 이등변 삼각형을 출력합니다.')

# 변의 길이 입력
n = int(input('짧은 변의 길이를 입력하세요.: '))

# *를 i만큼 출력하는 For 
for i in range(n):
    for j in range(i + 1):
        print('*', end = '')
    print()
