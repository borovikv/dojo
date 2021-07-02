def count_palindromes(s):
    if s[0] * len(s) == s:
        return len(s) * (len(s) + 1) // 2
    return sum(is_polindrom(s, i, j) for i in range(len(s)) for j in range(i + 1, len(s) + 1))


def is_polindrom(s, start, stop):
    l = stop - start
    for i in range(l//2):
        if s[start + i] != s[stop-i-1]:
            return 0
    return 1


def count_palindromes_n2(a):
    index = []
    count, local_count = 0, 0
    for i, s in enumerate(list(a)):
        if i > 0 and s == a[i - 1]:
            index.append(i)
            local_count += 1
        for j in range(len(index)):
            ix = index[j]
            if ix <= 0:
                local_count -= int(ix == 0)
                index[j] -= 1
                continue
            if s == a[ix - 1]:
                index[j] -= 1
            else:
                index[j] = -1
                local_count -= 1
        index.append(i)
        local_count += 1
        count += local_count
    return count
