def brute_force(arr):
    # 这个划分可以看成是通过指针进行划分的，就是看指针落处作为划分点
    # 是不是合适的
    if not arr: return 0
    count = 0
    left = right = 0
    while (right < len(arr) - 1):
        if max(arr[left:right + 1]) <= min(arr[right + 1:]):
            count += 1
            left = right
            right += 1
        else:
            right += 1
    return count + 1  # right在count处有意义，将arr分成count+1种


# 暴力法超过了5%

def correct(arr):
    import collections
    ans, c1, c2 = 0, collections.Counter(), collections.Counter()
    for index, item in enumerate(sorted(arr)):
        #
        c1[arr[index]] += 1
        c2[item] += 1
        if c1 == c2: ans += 1
    return ans


arr = [0, 0, 1, 1, 1]
print(brute_force(arr))
print(correct(arr))
