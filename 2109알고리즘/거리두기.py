s=["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"]


i = [9 * 'X', 9 * 'X']
for j in range(5):
    i.append('XX' + s[j] + 'XX')
i += 9 * 'X', 9 * 'X'

for m in range(2, len(i) - 2):
    flag = 0
    for n in range(2, len(i) - 2):
        if i[m][n] == 'P':
            print(m, n)
            if i[m][n + 1] == 'P' or i[m + 1][n] == 'P' or i[m][n - 1] == 'P':
                print('xxxxxxxxxxxxxxx')
                flag = 1
            elif i[m][n + 1] == '0' and (i[m][n + 2] == 'P' or i[m + 1][n + 1] == 'P'):
                flag = 1
            elif i[m][n - 1] == '0' and (i[m][n - 2] == 'P' or i[m + 1][n - 1] == 'P'):
                flag = 1
            elif i[m + 1][n] == '0' and (
                    i[m + 2][n] == 'P' or i[m + 1][n + 1] == 'P' or i[m + 1][n - 1] == 'P'):
                flag = 1
    if flag == 1:
        print(0)
        break
print(i)