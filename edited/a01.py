import sys
nums = []

s = 0
for i, line in enumerate(sys.stdin):
    line = line.replace('\n', '')
    if i == 0:
        s = int(line)
        continue

    tmp = [int(x) for x in line.split()]
    for el in tmp:
        nums.append(el)


has = set()

pairs = 0
for i in range(s):
    for j in range(i+1, s):
        pairs += 1
        tmp = int(nums[i] + nums[j])
        if tmp in has:
            continue
        else:
            has.add(tmp)

print(pairs, len(has))