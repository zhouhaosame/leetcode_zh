def countAndSay(n):
    count_e, x= '1', 0
    while (x < n-1):
        count=""
        i,j=0,0
        while (i < len(count_e)):
            while( j + 1 < len(count_e) and count_e[j] == count_e[j + 1]):
                j = j + 1
            count=count+str(j + 1 - i) + count_e[i]
            j+=1
            i = j
        x+=1
        count_e=count
    return count_e
n=4
print(countAndSay(n))