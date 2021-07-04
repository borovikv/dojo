def count_palindromes(s):
    if s[0] * len(s) == s:
        return len(s) * (len(s) + 1) // 2
    return sum(is_polindrom(s, i, j) for i in range(len(s)) for j in range(i + 1, len(s) + 1))


def is_polindrom(s, start, stop):
    l = stop - start
    for i in range(l // 2):
        if s[start + i] != s[stop - i - 1]:
            return 0
    return 1


def count_palindromes_n2(s):
    index = []
    count, multi = 0, 0
    for i, symbol in enumerate(list(s)):
        if i > 0 and symbol == s[i - 1]:
            index.append(i)
        index = [j - 1 for j in index if j > 0 and s[j - 1] == symbol]
        index.append(i)
        count += len(index)
    return count
