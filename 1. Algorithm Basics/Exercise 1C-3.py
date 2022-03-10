# 2자리 양수(10~99) 입력받기

# 프로그램 설명
print('2자리 양수를 입력하세요.')

# 10 이상 90 이하의 입력만을 받는 While 문
while True:
    no = int(input('값을 입력하세요.: '))
    if no >= 10 and no <= 90:
        break

# 결과 출력
print(f'입력받은 양수는 {no}입니다.')
