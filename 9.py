from math import pow
from timeit import *

inp = input()
n = len(inp)
tot = 0

chars = [[] for _ in range(26)]

print(chars)


#first pass
# for chr_idx, ch in enumerate(inp):
#     letter_idx = ord(ch) % 26

# brute force
for chr_idx, ch in enumerate(inp):
    letter_idx = (ord(ch) - ord("A")) % 26
    chars[letter_idx].append(chr_idx)

table = [[] for _ in range(26)]

beg_idx = 0
for letter_idx, letter_data in enumerate(chars):
    prev = -1
    cur = -1
    for loc_idx in letter_data:
        prev = cur      # -1
        cur = loc_idx   # 0

        if prev + 1 != cur:
            table[letter_idx].append((beg_idx, loc_idx))
            beg_idx = loc_idx

print(table)

for i in range(1, n+1):
    for j in range(i, n+1):
        if inp[i-1] == inp[j-1]: continue
        tot += pow(j-i, 2)

# print(int(tot % (pow(10, 9) + 7)))
