# 자료구조와 함께 배우는 알고리즘 입문 <파이썬 편> 실습 2C-3

# 리스트의 모든 원소를 enumerate() 함수로 스캔하기(1부터 카운트))

x = ['John', 'George', 'Paul', 'Ringo']

for i, name in enumerate(x, 1):
    print(f'{i}번째 = {name}')
