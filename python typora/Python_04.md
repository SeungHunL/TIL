## Syntax Error

```python
invalid syntax
EOL while scanning string literal
unexpected EOF while parsing
```

```python
ZeroDivisionError
NameError
TypeError
ValueError
IndexError
KeyError
ModuleNotFoundError
ImportError
KeyboardInterrupt
```

ssss

```python
try & except
try:
    a=input()
    print(int(a))
except:
    print('숫자입력 ㄱ')
else:
    <코드 블럭 3>
    
try:
    <코드 블럭 1>
except 예외:
    <코드 블럭 2>
finally:
    <코드 블럭 3>
    
에러 메시지 처리 as
try:
    empty_list = []
    print(empty_list[-1])
except IndexError as err:
    print(f'{err}, 오류가 발생했습니다.')

    
raise 예외 발생시키기
def avg(s):
    if len(s)==0:
        raise Exception('학생이 없습니다.')
    return len(s)
assert Boolean expression, error message
ex)
assert len([1, 2]) == 1, '길이가 1이 아닙니다.'
```



