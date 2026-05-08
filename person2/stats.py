# Statistics module
def mean(numbers):
    return sum(numbers) / len(numbers)
def median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    return sorted_nums[mid] if n % 2 else (sorted_nums[mid-1] + sorted_nums[mid]) / 2
# Last updated: 2025-05-08
# Last updated: 2025-05-08
