from functools import reduce


# def countOfAnagramSubstring(s):
#     n = len(s)
#     sub_strings = dict()

#     for i in range(n):
#         substr = ''
#         for j in range(i, n):
#             substr = ''.join(sorted(substr + s[j]))
#             sub_strings[substr] = sub_strings.get(substr, 0)
#             sub_strings[substr] += 1

#     return reduce(lambda total, value: total + (value * (value - 1))//2, sub_strings.values(), 0)


def countOfAnagramSubstring(s):
    n = len(s)
    sub_strings = dict()

    for i in range(n):
        substr = ''
        for j in range(i, n):
            substr = ''.join(sorted(substr + s[j]))
            sub_strings[substr] = sub_strings.get(substr, 0)
            sub_strings[substr] += 1

    answer = 0
    for value in sub_strings.values():
        print('answer -> ', answer)
        print('value -> ' ,value)
        print('--------------')
        answer += (value * (value - 1))//2
    return answer      
      

print(countOfAnagramSubstring('xyyx'))
