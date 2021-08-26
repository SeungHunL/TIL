h='ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC'
str_list=list(h)
t=list(map(lambda c: ord('E')-ord(c),str_list))
print(sum(t))
print(ord('E'))
print(ord('A'))       
            