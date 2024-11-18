import tester

# Brute Force
def bf_solve(s):
    tot = 0
    n = len(s)
    for i in range(1, n+1):
        for j in range(i, n+1):
            if s[i-1] == s[j-1]: continue
            tot += pow(j-i, 2)
    return int(tot % (pow(10, 9) + 7))

# Dynamic Programming
def dp_simple_solve(s):
    n = len(s)
    tot = 0

    chars = [[] for _ in range(26)]

    # IDEA: build up hash set in first pass eliminates preprocessing
    for chr_idx, ch in enumerate(s):
        letter_idx = (ord(ch) - ord("A")) % 26
        chars[letter_idx].append(chr_idx)

    table = [[] for _ in range(26)]

    # preprocessing
    beg_idx = 0
    for letter_idx, letter_data in enumerate(chars):
        prev = -1
        cur = -1
        beg_idx = 0
        for loc_idx in letter_data:
            prev = cur
            cur = loc_idx

            if prev + 1 != cur:
                table[letter_idx].append((beg_idx, loc_idx - 1))
                beg_idx = loc_idx + 1
        if len(table[letter_idx]) == 0 or table[letter_idx][-1][1] != n-1: 
            if beg_idx != n and cur != n-1:
                table[letter_idx].append((beg_idx, n-1))
        else:
            table[letter_idx][-1] = (table[letter_idx][-1][0], n-1)

    cache = dict()
    def calc_range(start, end):
        if (start, end) in cache:
            return cache[(start, end)]
        elif start <= 1:
            cache[(start, end)] = (end*(end+1)*(2*end+1)/6.0)
        elif start == end:
            cache[(start, end)] = start ** 2
        else:
            cache[(start, end)] = (end*(end+1)*(2*end+1)/6.0) - calc_range(1, start-1)
        return cache[(start, end)]

    for i in range(0, n):
        ch = s[i]
        for rng in table[(ord(ch) - ord("A")) % 26]:
            if i < rng[1]:
                tot += calc_range(rng[0] - i, rng[1] - i)
    return int(tot % (pow(10, 9) + 7))

if __name__ == "__main__":
    tester.test_09()
