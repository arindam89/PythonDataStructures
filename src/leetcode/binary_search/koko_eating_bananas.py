# Problem: Koko Eating Bananas
# Link: https://leetcode.com/problems/koko-eating-bananas/
# Difficulty: Medium
#
# Approach:
# - Use binary search to find the minimum eating speed.
# - The search space is between 1 and the maximum number of bananas in a pile.
# - For each mid value, calculate the total hours required to eat all bananas.
# - Adjust the search space based on whether the total hours exceed the given limit.
#
# Time Complexity: O(n * log(max(piles))), where n is the number of piles.
# Space Complexity: O(1)

def min_eating_speed(piles, h):
    """
    Find the minimum eating speed to finish all bananas within h hours.

    :param piles: List[int] - A list of integers representing the number of bananas in each pile.
    :param h: int - The maximum number of hours allowed.
    :return: int - The minimum eating speed.
    """
    def can_finish(speed):
        hours = 0
        for pile in piles:
            hours += -(-pile // speed)  # Equivalent to math.ceil(pile / speed)
        return hours <= h

    left, right = 1, max(piles)
    while left < right:
        mid = left + (right - left) // 2
        if can_finish(mid):
            right = mid
        else:
            left = mid + 1

    return left