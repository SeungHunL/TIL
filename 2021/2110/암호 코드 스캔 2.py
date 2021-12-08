import sys

sys.stdin=open('input.txt',"r")

token = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}


def htob(string):
    ans = ''
    for _ in range(len(string)):
        ans += str(format(int('0x' + string[_], 16), '04b'))
    return ans


def part(string):
    ans = ''
    for _ in range(7):
        if string[_ * k] * k == string[_ * k:_ * k + k]:
            ans += string[_ * k]
        else:
            return '0'
    return ans

T = int(input().strip())
for _ in range(T):
    N, M = map(int, input().strip().split())
    codelist=[] # 사용된 암호
    ans = []
    original=[[] for __ in range(N)]
    for n in range(N):
        original[n]=input().strip().rstrip('0')

    for l in range(N):
        string = htob(original[l]).rstrip('0')
        while string:
            t = [0] * 8
            end = len(string)

            # 암호코드 찾기
            for j in range(8):
                k=1
                teststr = part(string[end - 7:end])
                while teststr not in token:
                    k += 1
                    teststr = part(string[end - 7 * k:end])
                end -= 7 * k
                t[7 - j] = token[teststr]

            # 암호코드 확정
            code=string[end:]
            # 16진수 암호 코드
            oidx = end // 4
            olen = 2*7*k+1
            ocode=original[l][oidx]
            i=1
            while 1:
                if original[l+i][oidx] == ocode:
                    original[l+i] = original[l+i][:oidx]+'0' * olen+original[l+i][oidx+olen:]
                else:
                    break
                i+=1

            string = string[:end].rstrip('0')

            # 검증
            snum = (t[0] + t[2] + t[4] + t[6]) * 3 + t[1] + t[3] + t[5]
            scode = 10 - snum % 10 if snum % 10 else 0
            codesum = sum(t) if scode == t[-1] else 0

            # 암호가 이전에 있었는지
            if code in codelist:
                pass
            else:
                codelist.append(code)
                ans.append(codesum)

    print(f'#{_ + 1} {sum(ans)}')

