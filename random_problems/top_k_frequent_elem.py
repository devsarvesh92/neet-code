"""Top k frequent elements"""

from typing import Any
import heapq


def top_frequent_elems(ls: list[Any], k: int) -> list[Any]:
    """_summary_

    Args:
        input (list[Any]): _description_
        k (int): _description_

    Returns:
        list[Any]: _description_
    """
    element_counter: dict[Any, Any] = {}

    # Time complexity: O(n)
    for l in ls:
        if l in element_counter:
            element_counter[l] += 1
        else:
            element_counter[l] = 1

    # Use heap
    heap = []
    for key, v in element_counter.items():
        heapq.heappush(heap, (-v, key))

    result = []
    for _ in range(0, k):
        result.append(heapq.heappop(heap)[1])

    return result


if __name__ == "__main__":
    print(top_frequent_elems(ls=[1, 1, 1, 2, 2, 3], k=2))
