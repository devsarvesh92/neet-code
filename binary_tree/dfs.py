from typing import Any


class Node:
    def __init__(self, val, left, right) -> None:
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root: Node) -> None:
        self.root = root

    def insert(self, val: Any, root: Node):
        """
        Inserts element in binary search tree
        Time complexity: O(log n)

        Args:
            val (Any): _description_
            root (Node): _description_

        Returns:
            _type_: _description_
        """
        if not root:
            return Node(val=val, left=None, right=None)

        if val < root.val:
            root.left = self.insert(val=val, root=root.left)
        elif val > root.val:
            root.right = self.insert(val=val, root=root.right)
        return root

    def search(self, val: Any, root: Node):
        if not root:
            return
        if val < root.val:
            return self.search(val=val, root=root.left)
        elif val > root.val:
            return self.search(val=val, root=root.right)
        else:
            return root

    def find_minimum(self, root: Node):
        if not root:
            return None
        while root:
            root = root.left
        return root.val

    def remove(self, val: Any, root: Node):
        if not root:
            return None
        if val < root.val:
            root.left = self.remove(val=val, root=root.left)
        elif val > root.val:
            root.right = self.remove(val=val, root=root.right)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                minval = self.find_minimum(root=root.right)
                root.val = minval
                root.right = self.remove(val=minval, root=root.right)
        return root

    def inorder(self, root: Node):
        """
        Left,Node,Right

        Args:
            val (Any): _description_
            root (Node): _description_
        """
        if not root:
            return

        self.inorder(root=root.left)
        print(root.val)
        self.inorder(root=root.right)

    def preorder(self, root: Node):
        """
        Node,Left,Right

        Args:
            root (Node): _description_
        """
        if not root:
            return
        print(root.val)
        self.preorder(root=root.left)
        self.preorder(root=root.right)

    def postorder(self, root: Node):
        """
        Left,Right,Node

        Args:
            root (Node): _description_
        """
        if not root:
            return
        self.postorder(root=root.left)
        self.postorder(root=root.right)
        print(root.val)


if __name__ == "__main__":
    ls = [2, 1, 5, 3]

    t = BinaryTree(root=Node(val=4, left=None, right=None))

    for l in ls:
        t.insert(val=l, root=t.root)

    print("==================================")
    print("==================================")

    t.inorder(root=t.root)
    t.preorder(root=t.root)
    t.postorder(root=t.root)
