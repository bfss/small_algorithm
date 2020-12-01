# -*- coding: utf-8 -*-
"""二叉树的先序遍历（根左右）"""
class Tree:
    """二叉树结构：值，左节点，右节点"""
    def __init__(self, value):
        """构造函数用来创建根节点"""
        self.value = value
        self.right = None
        self.left = None


    def create_node(self, value):
        """递归式创建节点"""
        if value < self.value :
            if self.left is None: 
                self.left = Tree(value)
            else:
                self.left.create_node(value)
        else:
            if self.right is None:
                self.right = Tree(value)
            else:
                self.right.create_node(value)


    def preorder(self, root):
        """先序遍历"""
        if root is None:
            return
        
        print(root.value)
        self.preorder(root.left)
        self.preorder(root.right)


root = Tree(5)
root.create_node(7)
root.create_node(9)
root.create_node(2)
root.create_node(4)
root.create_node(3)
root.create_node(8)
root.create_node(1)
root.create_node(6)
print('先序遍历 :')
root.preorder(root)