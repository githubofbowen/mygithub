class Node(object):
    def __init__(self, item):
        self.item = item
        self.lchild = None
        self.rchild = None

class Tree(object):
    '''二叉树'''
    def __init__(self):
        self.root = None
    def add(self, item):
        node = Node(item)
        queue = [self.root]

        if self.root == None:
            self.root = node
            return
        # 通过队列来实现  [A B C D E ] 从左边取判断是否为空 ，空就直接添加，不空的话添加到队列右侧
        while queue:# [None]的值为True
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        '''广度遍历'''
        queue = [self.root]
        if self.root == None:
            return
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.item, end=' ')
            if cur_node.lchild:
                queue.append(cur_node.lchild)
            if cur_node.rchild:
                queue.append(cur_node.rchild)
        print(' ')

    def preorder(self, node):
        """前序遍历"""
        if node is None:
            return
        print(node.item, end=' ')
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def midorder(self, node):
        """中序遍历"""
        if node is None:
            return
        self.midorder(node.lchild)
        print(node.item, end=' ')
        self.midorder(node.rchild)

    def postorder(self, node):
        """后序遍历"""
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.item, end=' ')

if __name__ == '__main__':
    tree = Tree()
    for i in range(10):
        tree.add(i)
    tree.breadth_travel()
    # tree.preorder(tree.root)
    # print(' ')
    # tree.midorder(tree.root)
    # print(' ')
    # tree.postorder(tree.root)