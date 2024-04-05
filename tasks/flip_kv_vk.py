from typing import TypeVar

__all__ = (
    "flip_kv_vk",
    "flip_kv_vk_safe",
)


KT = TypeVar("KT")
KV = TypeVar("KV")


def flip_kv_vk(d: dict[KT, KV]) -> dict[KV, KT]:
    return {v: k for k, v in d.items()}


def flip_kv_vk_safe(d: dict[KT, KV]) -> dict[KV, list[KT]]:
    conflicts_dict = {}
    
    for key, value in d.items():
        conflicts_dict = {}
    for key, value in d.items():
        if value not in conflicts_dict:
            conflicts_dict[value] = []
        conflicts_dict[value].append(key)
    return conflicts_dict

