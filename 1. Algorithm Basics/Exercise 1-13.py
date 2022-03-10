# +와 -를 번갈아 출력하기 2

# 프로그램 설명
print('+와 -를 번갈아 출력합니다.')

# n값 입력
n = int(input('몇 개를 출력할까요?: '))

# n // 2: n을 2로 나누었을 때 몫
# 예시: n = 12
# 0, 1, 2, 3, 4, 5 ... 총 6회 반복 출력
for _ in range(n // 2):
    print('+-', end = '')

'''for 문에 언더스코어(_)를 사용한 이유는 for 문에서 range() 함수가
for 문을 순환하며 반환하는 값(인덱스)을 사용할 필요가 없기 때문입니다.
즉, 파이썬에서는 무시하고 싶은 값을 언더스코어로 표현할 수 있습니다.
'''

'''파이썬에서 언더스코어(_)는 다음과 같은 상황에서 사용되는데 크게 5가지의 경우가 있다.

1. 인터프리터(Interpreter)에서 마지막 값을 저장할 때
2. 값을 무시하고 싶을 때 (흔히 “I don’t care"라고 부른다.)
3. 변수나 함수명에 특별한 의미 또는 기능을 부여하고자 할 때
4. 국제화(Internationalization, i18n)/지역화(Localization, l10n) 함수로써 사용할 때
5. 숫자 리터럴값의 자릿수 구분을 위한 구분자로써 사용할 때

(https://mingrammer.com/underscore-in-python/)
'''

# n이 홀수인 경우 마지막에 '+'를 한 번 더 출력
if n % 2:
    print('+', ends = '')

# '+' 출력 후 개행
print()
