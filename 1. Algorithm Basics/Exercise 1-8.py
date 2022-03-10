# 1부터 n까지 정수의 합 구하기 2(for 문)

# 프로그램 설명
print('1부터 n까지 정수의 합을 구합니다.')

# n값 입력
n = int(input('n값을 입력하세요.: '))

# 기본값 설정
sum = 0

# 합계를 구하는 for 문 (1부터 n까지 sum에 더해나간다)
for i in range(1, n + 1): # range 함수는 마지막 값 바로 전 값까지 리스트로 반환
    sum += i

# 합계 출력
print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')

'''range 함수
range(n): 0 이상 n 미만인 수를 차례로 나열하는 수열
range(a, b): a 이상 b 미만인 수를 차례로 나열하는 수열
range(a, b, step): a 이상 b 미만인 수를 step 간격으로 나열하는 수열
'''
