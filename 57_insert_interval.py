class Interval:
    def __init__(self,a=0,b=0):
        self.start=a
        self.end=b
def insert_interval(intervals,newInterval):
    visited,count=[],-1
    for i in range(len(intervals)):
        if intervals[i].end<newInterval.start:
            visited.append(intervals[i])
            count=i
        else:
            break
    #newInterval在最开始和在中间，是一样的讨论
    if count==len(intervals)-1:#newInterval在最后
        visited.append(newInterval)
        visited=[[x.start,x.end] for x in visited]
        return visited
    i=count+1
    j=i
    if newInterval.end<intervals[i].start:
        visited.append(newInterval)
        if intervals[i:]:
            visited.extend(intervals[i:])
    else:
        while(j<len(intervals) and intervals[j].start<=newInterval.end):
            j+=1
        j-=1#到这个else里面就意味着newInterval.end>=intervals[i].start:所以最少存在一个interval与newInterval相交的

        visited.append(Interval(min(intervals[i].start,newInterval.start),max(intervals[j].end,newInterval.end)))
        if j+1<len(intervals) and intervals[j+1:]:
            visited.extend(intervals[j+1:])
        visited=[[item.start,item.end] for item in visited]
    return visited
"""功夫不负有心人啊，这个我竟然超过了100%
思想就是刚开始的时候，只要interval.end<nreInterval.start的就指针往后，当指针i停下时，在添加一个指针j。此时指针
i所在的interval与new两种情况，相交，不想交。不想交意味着new在interval[i]前面。单独讨论这种情况。
相交的情况下，用指针j去找到最远的与new相交的interval[j]。然后接下来就好算了
因为i=0和i!=0的情况是同样讨论的。
还有一种情况，new在最后。直接添加就行了"""

intervals=[[1,5]]
intervals=[Interval(x[0],x[1]) for x in intervals]
newInterval=[6,8]
newInterval=Interval(newInterval[0],newInterval[1])
print(insert_interval(intervals,newInterval))

