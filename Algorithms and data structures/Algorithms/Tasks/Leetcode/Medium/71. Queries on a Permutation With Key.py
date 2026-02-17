from typing import List


def process_queries(queries: List[int], m: int) -> List[int]:
    m_range = [i for i in range(1, m + 1)]

    result = []

    for i in queries:
        idx = m_range.index(i)
        result.append(idx)
        m_range = [m_range[idx]] + m_range[:idx] + m_range[idx + 1:]

    return result


# ChatGPT solution
def process_queries(queries: List[int], m: int) -> List[int]:
    m_range = list(range(1, m + 1))
    result = []

    for i in queries:
        idx = m_range.index(i)
        result.append(idx)

        m_range.pop(idx)
        m_range.insert(0, i)

    return result
