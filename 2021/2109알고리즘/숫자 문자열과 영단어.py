import sys


def solution(s):
    i = 1
    ans = ''
    while i < len(s)-2:
        if s[i].isdigit():
            ans += s[i]
            i += 1
        elif s[i] == 'z':
            ans += '0';i += 4
        elif s[i] == 'o':
            ans += '1';i += 3
        elif s[i:i + 2] == 'tw':
            ans += '2';i += 3
        elif s[i:i + 2] == 'th':
            ans += '3';i += 5
        elif s[i:i + 2] == 'fo':
            ans += '4';i += 4
        elif s[i:i + 2] == 'fi':
            ans += '5';i += 4
        elif s[i:i + 2] == 'si':
            ans += '6';i += 3
        elif s[i:i + 2] == 'se':
            ans += '7';i += 5
        elif s[i] == 'e':
            ans += '8';i += 5
        elif s[i] == 'n':
            ans += '9';i += 4
    print(int(ans))
    return


nums = sys.stdin.readline()
solution(nums)
