"""
53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and
return its sum.
"""


def max_cross_subarray(arr, mid, low, high):
    now_left = arr[mid]
    left = arr[mid]
    for i in range(mid - 1, low - 1, -1):
        now_left = now_left + arr[i]
        if now_left > left:
            left = now_left
    now_right = arr[mid + 1]
    right = arr[mid + 1]
    for j in range(mid + 2, high + 1):
        now_right = now_right + arr[j]
        if now_right > right:
            right = now_right
    return left + right


def max_subarray_a(arr, low, high):
    if high == low:
        return arr[low]
    else:
        mid = (low + high) // 2
        m1 = max_subarray_a(arr, low, mid)
        m2 = max_subarray_a(arr, mid + 1, high)

        m3 = max_cross_subarray(arr, mid, low, high)

        result = max(m1, m2, m3)
        return result


def max_subarray_b(arr):
    if not arr:
        return 0

    cur_sum = max_sum = arr[0]
    for num in arr[1:]:
        cur_sum = max(num, cur_sum + num)
        max_sum = max(max_sum, cur_sum)

    return max_sum


if __name__ == '__main__':
    a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    max_a = max_subarray_a(a, 0, len(a) - 1)
    max_b = max_subarray_b(a)
    print(max_a)
    print(max_b)
