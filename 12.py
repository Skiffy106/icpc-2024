x = int(input())

els = []
for i in range(x):
    els.append(input())
    st = input()
    ret = True
    for ch in st:
        if not ch in els[i]:
            ret = False
            break
    if ret:
        print("YES")
    else:
        print("NO")
