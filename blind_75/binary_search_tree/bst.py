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
