def compress(s: str) -> str:
    parts = []
    for i, c in enumerate(s):
        if i == 0 or c != s[i-1]: cnt = 1
        else: cnt += 1  # s[i-1] = s[i]
        if i == len(s)-1 or c != s[i+1]:
            parts.append(c if cnt == 1 else f'{c}{cnt}')
    return ''.join(parts)

print(compress(s='AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB')) # Output: 'A4B3C2XYZD4E3F3A6B28'

print(compress(s='ABC')) # Output: 'ABC'
