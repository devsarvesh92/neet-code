import pytest
from stack.generate_parentheses import generate_parentheses


pytestmark = pytest.mark.generateparentheses


def test_generate_parentheses():
    generate_parentheses(n=3)
