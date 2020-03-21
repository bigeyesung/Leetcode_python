import collections
def reorganizeString(S):
    count = collections.Counter(S)
    c_max, f_max = count.most_common(1)[0]
    if 2 * f_max - 1 > len(S):
        return ''
    count.pop(c_max)
    res = len(S) * ['']
    res[:2*f_max:2] = f_max * [c_max]
    i = 2 * f_max
    for c in count:
        for _ in range(count[c]):
            if i >= len(S):
                i = 1
            res[i] = c
            i += 2
    return ''.join(res)

string = "aab"
ret = reorganizeString(string)