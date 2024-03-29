class Node:

    def __init__(self, left, right, val) -> None:
        self.left = left
        self.right = right
        self.val = val


class BST:

    def __init__(self) -> None:
        self.root = None

    def insert(self, *, val) -> None:
        if not self.root:
            self.root = Node(val=val, left=None, right=None)
        else:
            self._insert_recur(value=val, node=self.root)

    def _insert_recur(self, *, value, node) -> None:
        if value < node.val:
            if node.left is None:
                node.left = Node(left=None, right=None, val=value)
            else:
                self._insert_recur(value=value, node=node.left)
        elif value > node.val:
            if node.right is None:
                node.right = Node(left=None, right=None, val=value)
            else:
                self._insert_recur(value=value, node=node.right)
        else:
            print("Node already exisits")

    def inorder_traversal(self, root, traversal: list[int]) -> list[int]:
        if root:
            traversal = self.inorder_traversal(root=root.left, traversal=traversal)
            traversal.append(root.val)
            traversal = self.inorder_traversal(root=root.right, traversal=traversal)
        return traversal

    def max_depth(self, root: Node) -> int:
        if not root:
            return 0
        else:
            left_depth = self.max_depth(root=root.left)
            right_depth = self.max_depth(root=root.right)
            return max(left_depth, right_depth) + 1

    def invert(self, root: Node):
        if root is None:
            return

        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invert(root=root.left)
        self.invert(root=root.right)

    @staticmethod
    def subtree(t: Node, s: Node) -> bool:
        if not t:
            return True
        if not s:
            return False

        if BST.same(t, s):
            return True

        BST.same(t.left, s)
        BST.same(t.right, s)

    @staticmethod
    def same(t: Node, s: Node) -> bool:
        if not t and not s:
            return True

        if t.val == s.val:
            left_same = BST.same(t.left, s.left)
            right_same = BST.same(t.right, s.right)
            return left_same and right_same

        return False
