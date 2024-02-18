from typing import List


# my solution
def find_poisoned_duration(time_series: List[int], duration: int) -> int:
    if len(time_series) == 0:
        return 0

    if len(time_series) == 1:
        return duration

    result = 0
    for i in range(1, len(time_series)):
        diff = time_series[i] - time_series[i - 1]
        if diff >= duration:
            result += duration
        else:
            result += diff
    result += duration

    return result


def find_poisoned_duration(time_series: List[int], duration: int) -> int:
    total_time = 0

    for i in range(len(time_series) - 1):
        time_diff = time_series[i + 1] - time_series[i]
        total_time += min(time_diff, duration)

    # Add the duration for the last attack since it will always last for the full duration
    total_time += duration

    return total_time
