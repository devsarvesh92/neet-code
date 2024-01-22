import pytest
from blind_75.stack_problems.stack_problems import valid_parenttheses

pytestmark = pytest.mark.stackproblems


@pytest.mark.parametrize("input,output", [("()[]{}", True), ("(]", False)])
def test_valid_parenttheses(input, output):
    # https://leetcode.com/problems/valid-parentheses/submissions/1153764160/
    assert output == valid_parenttheses(s=input)
