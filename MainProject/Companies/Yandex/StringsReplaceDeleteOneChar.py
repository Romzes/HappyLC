def is_equiv(s1, s2):
    n1, n2 = len(s1), len(s2)
    d = n1 - n2
    if d not in (0, 1): return False
    if d == 0: return is_eq(s1=s1, i1=0, s2=s2, i2=0, max_diff=1)
    if d == 1:
        for i in range(len(s1)-1):
            if s1[i] != s2[i]: return is_eq(s1=s1, i1=i+1, s2=s2, i2=i, max_diff=0)
        return True

def is_eq(s1, i1, s2, i2, max_diff):
    cnt = 0; j = i2
    for i in range(i1, len(s1)):
        if s1[i] != s2[j]:
            cnt += 1
            if cnt > max_diff: return False
        j += 1
    return True

print(is_equiv(s1='abab', s2='aba'))