```python
sequence-container : list / tuple / range()
[value1, value2, value3]
list[i]

# tuple : immutable
x, y = 1, 2 # tuple
a=()	# empty tuple
st=(1,)
type(st)
len(st)

range(n,m) # n부터 m-1까지 값을 가짐 (n,m,s): +s만큼 증가한다.
list(range(3)) # [0, 1, 2]
list(range(0,-10,-1))

in not in / len min max / + */ s[i]/s[i:j]/s[i:j:k]/s.count() 
(1,2)+(5,6) #(1,2,5,6)
list=['z','b','c','d'] #[z,b,c,d] 실행 x

Non-sequence : set / dictionary
    
    set: {} # 순서가 없고 중복된 값이 없는 자료구조
    set()	# 빈 세트 
    set_a = {1, 2, 3}
	set_b = {3, 6, 9}
    print(set_a - set_b)	# {1, 2}
    print(set_a | set_b)	# {1, 2, 3, 6, 9}
    set_c = {1, 1, 1}		# {1}
	
    {}, dict()	#empty dict
    .keys()
    .values()
    .items()
    
    e=pb.items()
    list(e)
        
        리터럴(literal)
immutable
숫자(Number)
글자(String)
참/거짓(Bool)
range()
tuple()
frozenset()

mutable
list
dict
set
```

![typecasting](https://user-images.githubusercontent.com/18046097/61180466-a6a67780-a651-11e9-8c0a-adb9e1ee04de.png)