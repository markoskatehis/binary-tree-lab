from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

def max_depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return 1 + max(left_depth, right_depth)

def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    current = root

    while current:
        if p.val < current.val and q.val < current.val:
            current = current.left

        elif p.val > current.val and q.val > current.val:
            current = current.right

        else:
            return current

    return None