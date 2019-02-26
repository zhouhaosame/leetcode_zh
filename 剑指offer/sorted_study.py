def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K(object):
         def __init__(self, obj, *args):
             print('obj created with ',obj)
             self.obj = obj
         def __lt__(self, other):
             print('comparing less than ',self.obj, other.obj)
             print(mycmp(self.obj, other.obj) < 0)
             return mycmp(self.obj, other.obj) < 0
         def __gt__(self, other):
             print('comparing greter than ',self.obj,other.obj)
             return mycmp(self.obj, other.obj) > 0

         def __eq__(self, other):
             print('comparing equal to ',self.obj,other.obj)
             return mycmp(self.obj, other.obj) == 0
         def __le__(self, other):
             print('comparing less than equal ',self.obj,other.obj)
             return mycmp(self.obj, other.obj) <= 0
         def __ge__(self, other):
             print('comparing greater than equal',self.obj,other.obj)
             return mycmp(self.obj, other.obj) >= 0
         def __ne__(self, other):
             print('comparing not equal ',self.obj,other.obj)
             return mycmp(self.obj, other.obj) != 0
    return K

def mycmp(a, b):
     print("In Mycmp for", a, ' ', b)
     if a < b:
         return -1
     elif a > b:
         return 1
     return 0
#print(sorted([3,4,2,5],key=cmp_to_key(mycmp)))
a=[-2,2,3]
print(sorted(a,key=cmp_to_key(lambda x,y:x*y)))#[2, 3, -2]
a=[2,-2,3]
print(sorted(a,key=cmp_to_key(lambda x,y:x*y)))#[3, -2, 2]