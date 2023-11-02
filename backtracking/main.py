from typing import Any


class TreeNode:
    def __init__(self, val, left, right) -> None:
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root: TreeNode) -> None:
        self.root = root

    def insert(self, val: Any, root: TreeNode):
        if not root:
            return TreeNode(val=val, left=None, right=None)
        if val > root.val:
            root.right = self.insert(val=val, root=root.right)
        elif val < root.val:
            root.left = self.insert(val=val, root=root.left)
        return root

    def search(self, destination: Any, root: TreeNode):
        if root and root.val == destination:
            return True
        if self.back_tracking(destination=destination, root=root.left):
            return True
        if self.back_tracking(destination=destination, root=root.right):
            return True
        return False

    def get_paths(self, destination: Any, root: TreeNode, paths: list[Any]):
        if not root:
            return False
        if root.val == destination:
            paths.append(root.val)
            return True
        paths.append(root.val)
        if self.get_paths(destination=destination, root=root.left, paths=paths):
            return True
        if self.get_paths(destination=destination, root=root.right, paths=paths):
            return True
        paths.pop()
        return False

    def inorder(self, root):
        if not root:
            return
        self.inorder(root=root.left)
        print(root.val)
        self.inorder(root=root.right)


if __name__ == "__main__":
    tree = BinaryTree(root=TreeNode(4, None, None))
    for node in [2, 3, 6, 7, 5]:
        tree.insert(val=node, root=tree.root)
    tree.inorder(tree.root)

    paths = []
    tree.get_paths(destination=6, paths=paths, root=tree.root)

    print(f"{paths}")
