for q in range(int(input())):
    N = int(input())
    num = bin(int(input(), 16))[2:]  # 16진수를 10진수로 다시 2진수로 바꾼 뒤 '0b'이후의 부분만 사용
    c = 0                            # 연속하는 1의 개수를 센다
    ans = [0] * 10                   # 1이 연속한 개수를 센다.
    for i in range(len(num)):
        if num[i] == '1':
            c += 1                   # num의 i번째 숫자가 '1'이면 c를 더한다. 연속의 유무를 파악
        else:
            ans[c] += 1              # 연속하지 않으면 그때까지의 연속한 개수를 ans 에 +1
            c = 0
    ans[c] += 1                      # 마지막에 연속한 개수를 ans에 +1
    ans = map(str, ans[1:])          # join을 사용하기 위해 연속한 개수가 하나 이상인 부분을 str로 변환
    ans = ' '.join(ans)              # 띄어쓰기가 들어간 하나의 문자열로 바꿈
    print(f'#{q + 1} {ans}')
