def lengthOfLastWord(s):
    if not s:
        return 0
    s=list(filter(None, s.split(" ")))
    if not s:
        return 0
    else:
        return len(s[-1])
s="  "
print(lengthOfLastWord(s))