# 자료구조와 함께 배우는 알고리즘 입문 <파이썬 편> 실습 2-1
# 학생 5명의 시험 점수를 입력받아 합계와 평균을 출력하기

# 프로그램 설명
print('학생 그룹 점수의 합계와 평균을 구합니다.')

# 점수 5개 입력
score1 = int(input('1번 학생의 점수를 입력하세요.: '))
score2 = int(input('2번 학생의 점수를 입력하세요.: '))
score3 = int(input('3번 학생의 점수를 입력하세요.: '))
score4 = int(input('4번 학생의 점수를 입력하세요.: '))
score5 = int(input('5번 학생의 점수를 입력하세요.: '))

# 합계 계산
total = 0
total += score1
total += score2
total += score3
total += score4
total += score5

# 출
print(f'합계는 {total}점입니다.')
print(f'합계는 {total / 5}점입니다.')
