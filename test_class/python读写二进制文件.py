#读取十进制文件
def reading_file_with_ten(filepath):
    #十进制文件的话，可能是空格间隔的数
    nums=[]
    with open(filepath,"r") as data:
        while True:
            line=data.readline().strip()#整行读取数据,这时候的line是一个字符串
            #一般一行就是一条gps记录，第一个是编号，第二个是时间，接下来就是经纬度之类的
            if line:
                #print(line)
                nums.append(list(map(int,line.split())))#将line字符串进行分割，并且
                #转换成int列表
            else:
                break
    #print(nums)#nums里面存的是十进制文件中所有的数据。
    save_file_as_ten(nums)#写入十进制文件中，"w"会覆盖原来文件
    save_file_as_two(nums)#写入二进制文件中
    data.close()
def save_file_as_ten(nums):#用十进制保存
    with open("./test_new_ten.txt","w") as data:
        for row in nums:
            for item in row:
                data.write(str(item)+" ")
            data.write("\n")
    data.close()
import struct
def save_file_as_two(nums):#用二进制保存
    with open("./test_new_two.dat","wb") as data:#注意文件的后缀
        for row in nums:
            for item in row:
                data.write(struct.pack("i",item))
                #如果里面的数据是小数，这里的i要改成f
    data.close()

"""二进制的读"""
def reading_file_with_two(filepath):
    nums=[]
    with open(filepath,"rb") as data:#二进制要加上b
        while True:
            #要先明确二进制文件中，是多少位的整形？？这里是32位的。
            # 操作过程中需要注意数据的size
            item=data.read(4)#整行读取数据,这时候的line是一个字符串
            #一般一行就是一条gps记录，第一个是编号，第二个是时间，接下来就是经纬度之类的
            if item:
                nums.append(struct.unpack("i",item)[0])#unpack出来的是一个元组形式
            else:
                break
    print(nums)#nums里面存的是十进制文件中所有的数据。
filepath="./test_data.txt"
reading_file_with_ten(filepath)
reading_file_with_two("./test_new_two.dat")
