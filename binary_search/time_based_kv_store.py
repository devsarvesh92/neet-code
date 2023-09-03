from collections import defaultdict
from dataclasses import dataclass
import json
from typing import Any, Self


@dataclass
class Item:
    val: str
    timestamp: int


class KVStore:
    def __init__(self: Self) -> None:
        self.store: defaultdict = defaultdict(list)

    def __str__(self) -> str:
        return json.dumps(self.store)

    def get(self, key: str, timestamp: int) -> Any:
        target_vals: list[Item] = self.store.get(key)

        if len(target_vals) == 1 and target_vals[0].timestamp <= timestamp:
            return target_vals[0].val

        if target_vals:
            # binary search
            l_ptr, r_ptr = 0, len(target_vals) - 1
            while l_ptr <= r_ptr:
                mid = (l_ptr + r_ptr) // 2
                mid_el: Item = target_vals[mid]
                if timestamp < mid_el.timestamp:
                    r_ptr = mid - 1
                elif timestamp > mid_el.timestamp:
                    l_ptr = mid + 1
                else:
                    return mid_el.val
            return target_vals[-1].val

    def set(self, key: str, val: str, timestamp: int) -> None:
        self.store[key].append(Item(val=val, timestamp=timestamp))
