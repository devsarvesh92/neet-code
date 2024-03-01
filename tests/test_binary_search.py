import pytest

from blind_75.binary_search_tree.bst import BST


pytestmark = pytest.mark.binarysearchtreeproblems


def test_binary_search():
    bst = BST()
    bst.insert(val=4)
    for num in [1, 2, 3, 5]:
        bst.insert(val=num)
    assert [1, 2, 3, 4, 5] == bst.inorder_traversal(bst.root, traversal=[])


def test_invert_binary_tree():
    bst = BST()
    bst.insert(val=4)
    for num in [1, 2, 3, 5]:
        bst.insert(val=num)

    bst.invert(root=bst.root)

    assert [5, 4, 3, 2, 1] == bst.inorder_traversal(bst.root, traversal=[])
