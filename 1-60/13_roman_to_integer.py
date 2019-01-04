def romanToInteger(s):
    dct={"I":1,"V":2,"X":10,"L":50,"C":100,"D":500,"M":1000,
         "IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
    sum,i,l=0,0,len(s)
    while(i<l-1):
        if s[i]=="I" and s[i+1] in ["V","X"]:
            sum+=dct[s[i]+s[i+1]]
            i+=2
        elif s[i]=="X" and s[i+1] in ["L","C"]:
            sum+=dct[s[i]+s[i+1]]
            i+=2
        elif s[i]=="C" and s[i+1] in ["D","M"]:
            sum+=dct[s[i]+s[i+1]]
            i+=2
        else:
            sum+=dct[s[i]]
            i+=1
    return sum+dct[s[i]] if i==l-1 else sum
s="XIV"
print(romanToInteger(s))