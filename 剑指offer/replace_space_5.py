def replace_space(string):
    if not string:return False
    return string.replace(" ","%20")

def replace_space_1(string):
    chars=string.split(" ")
    string="%20".join(chars)
    return string

string="  ty u yt -1 "
print(replace_space(string))
print(replace_space_1(string))

