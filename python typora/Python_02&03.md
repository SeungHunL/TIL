제어문

조건문(if)

```python
value = num if num >= 0 else -num

result = dict({i:('매우나쁨' if dusts[i] > 150 else '나쁨'if dusts[i] > 80 else '보통'if dusts[i] >30 else '좋음') for i in dusts  })
print(result)
```

`for` 문은 시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체(iterable)의 요소들을 순회

for 문 안에서 임시 변수에 다른 값을 할당해도 반복구문에 영향을 주지 않습니다.

```python
chars = 안녕!
for i in chars:
    print(i)
    
enumerate()
print(enumerate(lunch))
print(list(enumerate(lunch)))
for idx, menu in enumerate(lunch, start=1):
    print(idx, menu)
    
for-else 
```

함수

```python
def
dir	 # 내장함수 목록을 직접 확인

매개변수: 함수의 정의 부분/ 전달인자: 함수를 호출하는 부분
위치인자(a,b)	/ 기본 인자(a=10)

*주의* 단, 기본 인자값(Default Argument Value)을 가지는 인자 다음에 기본 값이 없는 인자를 사용할 수는 없습니다.

def greeting(age, name):
    return f'{name}은 {age}살입니다.'
greeting(name='철수', age=24)
greeting(24, name='철수')
greeting(age=24, '철수')

print('첫번째 문장')
print('두번째 문장', end='_')
print('세번째 문장', '네번째 문장')
print('다섯번째 문장', '마지막 문장', sep='/', end='끝!')

가변(임의) 인자 리스트(Arbitrary Argument Lists)
def func(a, b, *args):
    *args : 임의의 개수의 위치인자를 받음을 의미
가변(임의) 키워드 인자(Arbitrary Keyword Arguments)
def func(**kwargs):
    **kwargs : 임의의 개수의 키워드 인자를 받음을 의미합니다

전역 스코프(global scope): 코드 어디에서든 참조할 수 있는 공간
지역 스코프(local scope): 함수가 만든 스코프로 함수 내부에서만 참조할 수 있는 공간
전역 변수(global variable): 전역 스코프에 정의된 변수
지역 변수(local variable): 로컬 스코프에 정의된 변수

변수의 수명주기
빌트인 스코프(built-in scope): 파이썬이 실행된 이후부터 영원히 유지
전역 스코프(global scope): 모듈이 호출된 시점 이후 혹은 이름 선언된 이후부터 인터프리터가 끝날 때 까지 유지
지역(함수) 스코프(local scope): 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지 (함수 내에서 처리되지 않는 예외를 일으킬 때 삭제됨)
    
Local scope: 함수
Enclosed scope: 특정 함수의 상위 함수
Global scope: 함수 밖의 변수 혹은 import된 모듈
Built-in scope: 파이썬안에 내장되어 있는 함수 또는 속성
    
# global 키워드를 사용하여 지역 스코프에서 전역 변수의 값을 바꿀 수 있습니다.
global global_num
global_num = 5

RecursionError
파이썬에서는 최대 재귀 깊이(maximum recursion depth): 1,000

반복문은 재귀로 구현된 함수보다 연산 속도가 빠른 편입니다.
```

