# LeetCode 17: Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
#
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
# Return the answer in any order.
#
# Approach:
# - Use backtracking to explore all possible combinations of letters.
# - Maintain a mapping of digits to their corresponding letters.
# - At each step, append a letter corresponding to the current digit and recurse for the next digit.
# - Backtrack by removing the last added letter.

def letter_combinations(digits):
    if not digits:
        return []

    phone_map = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }

    def backtrack(index, path):
        if index == len(digits):
            # Found a valid combination
            result.append("".join(path))
            return
        # Get the letters corresponding to the current digit
        possible_letters = phone_map[digits[index]]
        for letter in possible_letters:
            # Include the letter in the combination
            path.append(letter)
            # Recurse for the next digit
            backtrack(index + 1, path)
            # Backtrack by removing the last added letter
            path.pop()

    result = []
    backtrack(0, [])
    return result