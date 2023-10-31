from typing import Any, Self
import hashlib


class MyDictionary:
    def __init__(self) -> None:
        self.size = 10
        self.data = [None] * self.size

    def get(self: Self, key: str) -> Any:
        idx = self._hash(key=key)
        existing_elements = self.data[idx]
        if existing_elements:
            for key, value in existing_elements:
                if key == key:
                    return value

    def set(self: Self, key: str, val: Any) -> Any:
        idx = self._hash(key=key)
        # check if key already exisits
        # other append
        existing_elements = self.data[idx]
        if existing_elements:
            for idx, (k, _) in enumerate(existing_elements):
                if k == key:
                    existing_elements[idx] = (k, val)
                    return
            existing_elements.append((key, val))
        else:
            self.data[idx] = [(key, val)]

    def _hash(self: Self, key: str) -> int:
        md5_hash = hashlib.md5()
        md5_hash.update(key.encode("UTF-8"))
        md5_hex = md5_hash.hexdigest()
        md5_decimal = int(md5_hex, 16)
        return md5_decimal % 10


if __name__ == "__main__":
    dt = MyDictionary()
    dt.set("sarvesh", "sawant")
    print(dt.get("sarvesh"))
    dt.set("pradnya", "sawant")
    print(dt.get("pradnya"))
