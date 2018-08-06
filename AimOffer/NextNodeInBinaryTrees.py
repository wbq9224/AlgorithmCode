'''
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = Node
'''
def get_next(p_node):
    '''
    :param p_node:
    :return: p_node 's next node in inorder
    '''
    if not p_node:
        return

    if p_node.right:
        p_node = p_node.right
        while p_node.left:
            p_node = p_node.left
        return p_node
    elif p_node.parent:
        p_parent = p_node.parent
        while p_parent and p_node == p_parent.right:
            p_node = p_parent
            p_parent = p_node.parent
        return p_parent


if __name__ == '__main__':
    pass