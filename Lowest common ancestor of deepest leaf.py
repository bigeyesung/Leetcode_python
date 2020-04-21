class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lcaDeepestLeaves(root):
    def helper(root):
        if not root:
            return 0, None
        h1, left_node = helper(root.left)
        h2, right_node = helper(root.right)
        if h1>h2:
            return h1+1, left_node
        elif h1<h2:
            return h2+1, right_node
        else:
            return h1+1, root
    
    return helper(root)[0]

root = TreeNode(1)
left= TreeNode(2)
right = TreeNode(3)
root.left=left
root.right=right

ans = lcaDeepestLeaves(root)
print(ans)