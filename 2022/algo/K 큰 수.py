# def solution(numbers):
#     answer = ''
#     numbers=sorted(list(map(str,numbers)))
#     ndic={}
#     for i in numbers:
#         if len(i) in ndic:
#             ndic[len(i)].append(i)
#         else:
#             ndic[len(i)]=[i]
#     print(ndic)
#     while ndic:
#         tlen=0
#         target=''
#         keys=sorted(ndic.keys())
#         for key in keys:
#             v=ndic[key]
#             if v:
#                 if tlen and v[-1][:tlen]==target and v[-1][-1]<target[-1]:
#                     pass
#                 elif target<v[-1]:
#                     tlen=key
#                     target=v[-1]
#         answer+=ndic[key].pop()
#         print(answer)
#         if not ndic[key]:
#             ndic.pop(key)
#     return answer
def solution(numbers):
    numbers = list(map(str, numbers))
    while 1:
        print(numbers)
        for i in range(1,len(numbers)):
            print(numbers[-i] + numbers[-i - 1],numbers[-i-1] + numbers[-i])
            if numbers[-i] + numbers[-i - 1] > numbers[-i - 1] + numbers[-i]:
                numbers[-i - 1], numbers[-i] = numbers[-i], numbers[-i - 1]
                break
        else:
            break

    return ''.join(numbers)


print(solution([6, 10, 2]))
# print(solution([3, 30, 34, 5, 9]))