from collections import Counter


def isValid(s):
    char_counter = Counter(s)
    counts = dict()
    for key, value in char_counter.items():
        if value not in counts:
            counts[value] = [key]
        else:
            counts[value].append(key)
    print('Chars count ', counts)
    print('Keys -> ', counts)
    if len(counts) > 2:
        return 'NO'
    if len(counts) == 2:
        values = list(counts.values())
        keys = list(counts.keys())
        first = len(values[0])
        second = len(values[1])
        if first > 1 and second > 1:
            return 'NO'
        if abs(keys[0] - keys[1]) == 1:
            return 'YES'

    return 'NO'


# isValid('aaaabbcc')
print(isValid('aaaabbcc'))
# print(isValid('aabbcd'))
# print(isValid('aabbccddeefghi'))

def isValidd(s):
    s1 = Counter(s)
    p= list(s1.values())
    diff=[]

    a=max(p,key=p.count)
    b = max(p)

    if p.count(a)==p.count(b) or p.count(a)>p.count(b):
        max_num = a 
    else:
        max_num = b     
       
    for i in range(len(p)):
        if abs(max_num-p[i])==1:
            diff.append(p[i])
    
    sum_all= (sum(1 for i in p if i==max_num))
    
    if sum_all==len(p):
        print("YES")
  
    elif len(diff)==1:
        print("YES")

    else:
        print("NO")
    