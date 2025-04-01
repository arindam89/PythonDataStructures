from collections import Counter

def is_n_straight_hand(hand, group_size):
    """
    LeetCode Problem 846: Hand of Straights
    Link: https://leetcode.com/problems/hand-of-straights/

    Problem:
    Given an array of integers hand, where hand[i] is the value of the ith card, and an integer group_size,
    return true if it is possible to rearrange the cards into one or more groups of size group_size,
    where each group consists of group_size consecutive cards.

    Approach:
    - Use a Counter to count the occurrences of each card.
    - Sort the cards and try to form groups of consecutive cards.
    - For each card, reduce its count and the count of the next group_size - 1 cards.
    - If any card cannot form a group, return False.

    Args:
        hand (List[int]): List of integers representing the hand of cards.
        group_size (int): Size of each group.

    Returns:
        bool: True if possible, False otherwise.
    """
    if len(hand) % group_size != 0:
        return False  # Total cards must be divisible by group_size

    count = Counter(hand)  # Count occurrences of each card
    for card in sorted(count):  # Process cards in sorted order
        while count[card] > 0:  # While there are cards of this value
            for i in range(card, card + group_size):  # Check the next group_size - 1 cards
                if count[i] <= 0:  # If any card is missing, return False
                    return False
                count[i] -= 1  # Reduce the count of the card

    return True