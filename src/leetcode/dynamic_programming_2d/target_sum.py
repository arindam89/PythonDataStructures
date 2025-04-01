def find_target_sum_ways(nums, target):
    """
    Calculate the number of ways to assign symbols to make the sum equal to target.

    Args:
        nums (List[int]): List of numbers.
        target (int): Target sum.

    Returns:
        int: Number of ways to achieve the target sum.
    """
    total = sum(nums)
    if (total + target) % 2 != 0 or total < abs(target):
        return 0

    subset_sum = (total + target) // 2
    dp = [0] * (subset_sum + 1)
    dp[0] = 1

    for num in nums:
        for j in range(subset_sum, num - 1, -1):
            dp[j] += dp[j - num]

    return dp[subset_sum]