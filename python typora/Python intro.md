## Python intro

```python
using ;?
한 줄로 표기할때는 ;을 작성하여 표기
            """
            여러줄 주석
            """
문장(statement)은 파이썬이 실행 가능(executable)한 최소한의 코드 단위
[] {} ()는 \ 없이도 가능합니다.
            print('hello\
            world')


변수는 =을 통해 할당(assignment)
해당 데이터 타입을 확인		 type()
해당 값의 메모리 주소를 확인 	id()

식별자의 이름은 영문알파벳(대문자와 소문자), 언더스코어(_), 숫자로 구성
첫 글자에 숫자가 올 수 없습니다.
길이에 제한이 없습니다.
대소문자(case)를 구별합니다.
            int float complex
            8진수 : 0o / 2진수 : 0b / 16진수: 0x 	ex) a = 0b101
            b = 314e-2 = 3.14	3.5 - 3.12 = 0.3799999999999999 
            round(): 반올림
            import math
            math.isclose(a, b)

            string ''/""/''''''/""""""/
    
    		a=input() #5입력 시 str 5로 입력 b="26", a+b=526
    
문자열 안에 문장부호(', ")가 사용될 경우 이스케이프 문자(\)를 활용 가능
            print("hey"*3+" yo!")
            
\n	줄 바꿈
\t	탭
\r	캐리지리턴
\0	널(Null)
\\	\
\'	단일인용부호(')
\"	이중인용부호(")

            %-formatting
            print("name=%s"%name)
            %d /%f /%s
            str.format()
            f-strings 
            str.format(name)  		#'po'
            print(str.format(name))	#po
			print(f'name={name}')
			print('name={name}')
            print(f"""
            Hello,
            {name}
            """)
            
            import datetime
            today = datetime.datetime.now()
            print(today)
            print(f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일 {today:%A}')
            #오늘은 21년 08월 07일 Saturday
            
0, 0.0, (), [], {}, '', None
bool() #bool 형변환
type(None) #NoneType
Data - int/float/complex	//	str	//	bool
True+5 		#6
int(5.99) 	#5
int(3.5)		#O
int(str(3.5))	#X
type(10/2)	#float
/	//	%
quotient, remainder =  divmod(5,2)

is	객체 아이덴티티
is not	부정된 객체 아이덴티티

& |은 파이썬에서 비트 연산자
5.3.1  단축평가
첫 번째 값이 확실할 때, 두 번째 값은 확인 하지 않습니다.
조건문에서 뒷 부분을 판단하지 않아도 되기 때문에 속도가 향상됩니다.
'a'and'b'	#'b'
('b'and'a')in(vowels) #True

()을 통한 grouping
Slicing
Indexing
제곱연산자 **
단항연산자 +, - (음수/양수 부호)
산술연산자 *, /, %
산술연산자 +, -
비교연산자, in, is
not
and
or

import random
list=[
    '()을 통한 grouping',
    'Slicing',
    'Indexing',
    '제곱연산자 **',
    '단항연산자 +, - (음수/양수 부호)',
    '산술연산자 *, /, %',
    '산술연산자 +, -',
    '비교연산자, in, is',
    'not',
    'and',
    'or']
random.shuffle(list)
print(list)
```

![variable](https://user-images.githubusercontent.com/9452521/87640197-55a7f280-c781-11ea-9cff-19c022ce704a.png)





