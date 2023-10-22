from typing import Any, Optional, TypeVar

TreeNode = TypeVar("TreeNode")


class TreeNode:
    def __init__(
        self, val: Any, left: Optional[TreeNode], right: Optional[TreeNode]
    ) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.val)


class Tree:
    def __init__(self, root: TreeNode) -> None:
        self.root = root

    def insert(self, val: Any, root: TreeNode) -> TreeNode:
        if not root:
            return TreeNode(val=val, left=None, right=None)
        if val > root.val:
            root.right = self.insert(val, root=root.right)
        elif val < root.val:
            root.left = self.insert(val, root=root.left)
        return root

    def search(self, val: Any, root: TreeNode) -> TreeNode:
        if not root:
            return None
        if val > root.val:
            return self.search(val, root=root.right)
        elif val < root.val:
            return self.search(val, root=root.left)
        else:
            return root

    def find_minimum(self, root: TreeNode):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    def preorder_dfs(self, root: TreeNode):
        if root:
            print(root.val)
            self.preorder_dfs(root.left)
            self.preorder_dfs(root.right)

    def remove(self, val, root) -> TreeNode:
        if not root:
            return None
        if val < root.val:
            root.left = self.remove(val=val, root=root.left)
        elif val > root.val:
            root.right = self.remove(val=val, root=root.right)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minnode = self.find_minimum(root=root.right)
                root.val = minnode.val
                root.right = self.remove(val=minnode.val, root=root.right)
        return root


if __name__ == "__main__":
    ls = [2, 1, 5, 3]

    t = Tree(root=TreeNode(val=4, left=None, right=None))

    for l in ls:
        t.insert(val=l, root=t.root)

    t.preorder_dfs(t.root)
    print("========================")

    print(t.find_minimum(t.root))
    print("========================")

    t.remove(val=3, root=t.root)

    t.preorder_dfs(t.root)
