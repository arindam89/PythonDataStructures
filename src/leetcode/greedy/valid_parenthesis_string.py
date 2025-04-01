def check_valid_string(s):
    """
    LeetCode Problem 678: Valid Parenthesis String
    Link: https://leetcode.com/problems/valid-parenthesis-string/

    Problem:
    Given a string s containing only three types of characters: '(', ')' and '*', return true if the string is valid.
    The string is valid if:
    - Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    - Any right parenthesis ')' must have a corresponding left parenthesis '('.
    - Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    - '*' could be treated as a single right parenthesis ')', a single left parenthesis '(', or an empty string.

    Approach:
    - Use two variables, low and high, to track the range of possible open parentheses.
    - Increment low and high for '(', decrement low and high for ')', and adjust for '*' accordingly.
    - If high becomes negative, return False. If low is 0 at the end, the string is valid.

    Args:
        s (str): Input string.

    Returns:
        bool: True if the string is valid, False otherwise.
    """
    low = high = 0  # Tracks the range of possible open parentheses

    for char in s:
        if char == '(':
            low += 1  # Increment low for '(' as it adds an open parenthesis
            high += 1  # Increment high for '(' as it adds an open parenthesis
        elif char == ')':
            low = max(low - 1, 0)  # Decrement low for ')' but ensure it doesn't go below 0
            high -= 1  # Decrement high for ')' as it closes an open parenthesis
        else:  # char == '*'
            low = max(low - 1, 0)  # '*' can act as ')', so decrement low
            high += 1  # '*' can act as '(', so increment high

        if high < 0:  # If high becomes negative, there are unmatched ')' characters
            return False

    return low == 0  # If low is 0, all open parentheses are matched