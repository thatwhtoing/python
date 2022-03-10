# 가로, 세로 길이가 정수이고 넓이가 area인 직사각형에서 변의 길이 나열하기

# 직사각형의 넓이 입력
area = int(input('직사각형의 넓이를 입력하세요.: '))

# 가능한 경우의 수를 찾는 for 문
for i in range(1, area + 1): # 1부터 직사각형의 넓이값까지 반복
    if i * i > area: # 입력한 값보다 넓이가 큰 정사각형의 변의 길이가 변의 최대이다
        break
    if area % i: # 입력한 값을 정수 두 개로 분해하지 못하는 경우에는 넘어간다
        continue
    print(f'{i} × {area // i}')
