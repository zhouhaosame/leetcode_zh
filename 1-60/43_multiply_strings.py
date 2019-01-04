def multiply(num1, num2):
    def com_sum(n1, n2):  # 求两个数的"和"，这里的和是从左往右边加，如果要是普通的，将i,j的其实范围改掉就好了
        # 输入格式n1和n2都是字符串
        i, j, l_1, l_2, ans, flag = 0, 0, len(n1), len(n2), "", 0
        [n1, l_1, n2, l_2] = [n1, l_1, n2, l_2] if l_1 < l_2 else [n2, l_2, n1, l_1]
        if l_1 == 0:
            return n2
        while (i < l_1):
            mul_num = int(n1[i]) + int(n2[j]) + flag
            flag = (mul_num) // 10
            ans = ans + str(mul_num % 10)
            j += 1
            i += 1
        while (flag != 0):
            if j == l_2:
                ans = ans + str(flag)
                break
            else:
                if j < l_2:
                    temp=int(n2[j]) + flag
                    flag = (temp) // 10
                    ans = ans + str((temp) % 10)
                    j += 1
        ans = ans + n2[j:]
        return ans

    if num2 == '0' or num1 == '0': return '0'
    i, j = len(num1) - 1, len(num2) - 1
    ans = []
    while (i >= 0):
        temp_l ,flag= "",0
        while (j >= 0):
            mul_num = int(num1[i]) * int(num2[j]) + flag
            flag = (mul_num) // 10
            temp_l=temp_l+str(mul_num % 10)
            j -= 1
        if flag != 0:
            temp_l=temp_l+str(flag)
        ans.append(temp_l)
        i -= 1
        j = len(num2) - 1
    for index, item in enumerate(ans):
        ans[index] ='0' * index + item
    from functools import reduce
    return reduce(com_sum, ans, [])[::-1]


num1 = "999"
num2 = "999"
print(multiply(num1, num2))
