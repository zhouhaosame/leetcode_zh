#二叉树的镜像
def sysmetric(self,root):
    if not root:
        return root
    temp_node=root.right
    root.right=self.sysmetric(root.left)
    root.left=self.sysmetric(temp_node)
    return root

