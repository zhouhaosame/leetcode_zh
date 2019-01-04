import json
def is_whitespace(c):
    if c == " " or c == "\t" or c == "\r" or c == "\n" or ord(c) == 0x202F:
        return True
    return False
def add_space(strs):#是一个字符串
    return



with open("./webqa_test.json","r",encoding="utf-8") as f:
    input_data=json.load(f)[:10]
for i in range(len(input_data)):
    input_data[i]["article_content"] = add_space(input_data[i]["article_content"])
    input_data[i]["questions"]["answer"]=add_space(input_data[i]["questions"]["answer"])
    input_data[i]["questions"]["question"] = add_space(input_data[i]["questions"]["question"])
s="周豪zh190,45zh周豪\n周豪pp，哈哈"
