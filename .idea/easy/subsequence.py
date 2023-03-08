def isSubseqeuence(s,t):
    dict = {}
    for i in range(0,len(s)):
        if s[i] in t:
            if (s[i] in dict):
                continue
            else:
                dict[s[i]] = t.index(s[i])

    values = list(dict.values())
    is_ordered = lambda values: all(values[i] < values[i+1] for i in range(len(values)-1))
    if (is_ordered(values) and len(values) == len(s)):
        return True
    else:
        return False


print(isSubseqeuence('ab','baab'))