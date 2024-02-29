import pytest

from blind_75.binary_search_tree.bst import BST


pytestmark = pytest.mark.binarysearchtreeproblems


def test_binary_search():
    bst = BST()
    bst.insert(val=4)
    for num in [1, 2, 3, 5]:
        bst.insert(val=num)
    assert [1, 2, 3, 4, 5] == bst.inorder_traversal(bst.root, traversal=[])
