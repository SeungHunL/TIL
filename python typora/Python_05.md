#  data structure

```Python
a.find('p') #위치 /-1 반환
a.index('p')#위치 / 오류 발생
a.replace(old,new[,count]) #count 지정 시 해당 갯수만큼 시행	b.replace('o','_',2)
a.strip([chars]) # ()공백 제거 ('hi') hi제거
a.split('_')
'!'.join(word) # 'separator'.join(iterable) iterable 반복 가능한;
.capitalize(), .title(), .upper() # 원본이 바뀌지 않음
.lower(), .swapcase()
기타 문자열 관련 검증 메소드: 참/거짓 반환
.isalpha(), .isdecimal(), .isdigit(), .isnumeric(), .isspace(), .isupper(), .istitle(), .islower()
dir('string') 문자열이 가지고 있는 메소드 확인 가능

```



```python
list
.append()
.extend(iterable)
	cafe.extend(['twosome_place'])
    cafe.extend('ediya')		# e,d,i,y,a 저장
.insert(i,x)
.remove(x) 값이 없으면 오류
.pop(i)
.clear()
.index(x)
.count(x)
.sort() #원본 list를 변형시키고, None을 리턴 
	lotto.sort(reverse=True)
.sorted()
리스트 복사 얕은 복사
immutable - literal(int,float,complex,str,bool), range(), tuple(), frozenset()
mutable - list, dict, set
slice[:]	#b = a[:]
list()		#b = list(a)
import copy
b = copy.deepcopy(a)

list comprehension
list(expression for 변수 in iterable)
list(i for i in range(1,11) if i%2==0)
list((i,j) for i in girls for j in boys)

result = list( i for i in words if i not in ('a','i','o','u','e'))
print(''.join(result))

''.join(str(i) for i in numbers)
''.join(map(str,numbers))

list(int(i) for i in numbers)
list(map(int,numbers))

a,b = map(int,input().split())
print(a+b)

new_numbers = list(filter(odd, numbers))
pair = list(zip(girls, boys))

```



```python
set
.add(elem)
.update(*others) #중복되는 값을 제외하고 set에 추가
.remove(elem)	#없을 시 error
.discard(elem)	#error발생 x
.pop()			#순서가 없으므로 

dictionary
.get(key[,default])
.pop(key[,default])
.update()

dict({i:'매우나쁨' if dusts[i]>150 else '나쁨' if dusts[i]>80 else'보통'if dusts[i]>30 else '좋음' for i in dusts})
```

