import pytest

from binary_search.time_based_kv_store import KVStore


pytestmark = pytest.mark.timebasekv


def test_time_based_kv_store():
    cache_store = KVStore()
    cache_store.set("foo", "bar", 1)
    assert "bar" == cache_store.get("foo", 1)
    assert "bar" == cache_store.get("foo", 3)

    cache_store.set("foo", "bar2", 4)
    assert "bar2" == cache_store.get("foo", 4)
    assert "bar2" == cache_store.get("foo", 5)
