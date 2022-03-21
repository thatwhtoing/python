# 자료구조와 함께 배우는 알고리즘 입문 <파이썬 편> 실습 2-5

# 각 배열 원소의 최댓값을 구해서 출력하기(튜플, 문자열, 문자열 리스트)

from max import max_of

t = (4, 7, 5.6, 2, 3.14, 1)    # 튜플
s = 'string'    # 문자열
a = ['DTS', 'AAC', 'FLAC']    # 문자열 리스

print(f'{t}의 최댓값은 {max_of(t)}입니다.')
print(f'{s}의 최댓값은 {max_of(s)}입니다.')
print(f'{a}의 최댓값은 {max_of(a)}입니다.')
