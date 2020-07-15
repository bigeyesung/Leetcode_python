def minRemoveToMakeValid(s):
    stack, cur = [], ''
    for c in s:
        if c == '(':
            stack += [cur]
            cur = ''
        elif c == ')':
            if stack:
                cur = stack.pop() + '(' + cur + ')' 
        else:
            cur += c
    
    while stack:
        cur = stack.pop() + cur
    return cur


ans = minRemoveToMakeValid("lee(t(c)o)de)")
