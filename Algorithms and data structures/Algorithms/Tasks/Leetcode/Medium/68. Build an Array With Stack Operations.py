from typing import List


def build_array(target: List[int], n: int) -> List[str]:
    len_target = len(target)
    target_idx = 0
    operations = []

    for i in range(1, n + 1):
        operations.append("Push")

        if i == target[target_idx]:
            if target_idx == len_target - 1:
                return operations

            target_idx += 1
            continue

        else:
            operations.append("Pop")

    return operations
