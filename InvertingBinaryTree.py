class TreeNode:
    def __init__(self, val=0, left=None, right=None,):
        self.val= val
        self.left =left
        self.right=right

    def print_treenode(self,root):
        if not root:
            return
        self.print_treenode(root.left)
        print(root.val, end=" ")
        self.print_treenode(root.right)        

class Solution:
    def invertTree(self, root):
        if root== None:
            return None
        root.left, root.right= self.invertTree(root.right), self.invertTree(root.left)
        return root

        

if __name__=="__main__":
    root = TreeNode(4)
    root.left = TreeNode(3, TreeNode(1), TreeNode(3))
    root.right = TreeNode(9, TreeNode(6), TreeNode(9))
    
    print("Original Tree (In-order):")
    root.print_treenode(root)

    # Invert the tree
    solution = Solution()
    inverted = solution.invertTree(root)

    print("\nInverted Tree (In-order):")
    root.print_treenode(inverted)
