def isSymmetric(root):
    innums,postnums=[],[]
    def pre_visist(root):
        if not root:
            innums.append(None)
        else:
            innums.append(root.val)
            pre_visist(root.left)
            pre_visist(root.right)
    def post_visit(root):
        if not root:
            postnums.append(None)
        else:
            post_visit(root.left)
            post_visit(root.right)
            postnums.append(root.val)
    pre_visist(root)
    post_visit(root)
    if innums==postnums[::-1]:
        return True
    else:
        return False
a=[None,1,2,None,4]
b=[4,None,2,1,None]
c=[1,2,3]
d=[3,2,1]
if a==b[::-1]:
    print("dd")
else:
    print("gg")
#dd
if c==d[::-1]:
    print("kk")
else:
    print("hh")
#kk
e="123"
v="123"
p="1234"
if e==v:
    print("yyyy")
else:
    print("nnn")
#yyyy