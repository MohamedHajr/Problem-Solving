import sys

INT_MAX = sys.maxsize  

def isBalanced(root):
    if not root:
        return 0
    left = isBalanced(root.left)
    right = isBalanced(root.right)

    diff = abs(left - right)
    if diff > 1 or left == INT_MAX or right == INT_MAX:
        return INT_MAX
    else:
        return max(left, right) + 1
