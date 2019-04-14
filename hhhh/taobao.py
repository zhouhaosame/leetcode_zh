"""
m个红球和n个蓝球，放到k个相同的碗中，然后可以有空碗，问有多少种放法。

"""
while True:
    try:
        m, n, k = list(map(int, input().split()))
        ans = []
        def find_bowl(res, flag):
            t = []
            for i in range(k):
                if res[i]==0 or res[i] > 0 and flag > 0 or res[i] < 0 and flag < 0:
                    t.append(i)
            return t
        def f(res, x, y):
            if x == 0 and y == 0:
                d = []
                for item in res.items():
                    d.append(item)
                ans.append(d)
            else:
                if x != 0:
                    bowl = find_bowl(res, 1)
                    for item in bowl:
                        res[item] += 1
                        f(res, x - 1, y)
                        res[item] -= 1
                if y != 0:
                    bowl1 = find_bowl(res, -1)
                    for item in bowl1:
                        res[item] -= 1
                        f(res, x, y + 1)
                        res[item] += 1
        dct=dict()
        for i in range(k):
            dct.update({i:0})
        f(dct, n, -m)
        res = []
        for item in ans:
            res.append([i for i in item].sort())
        print(len(set(res)))
    except:
        break