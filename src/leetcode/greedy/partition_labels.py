def partition_labels(s):
    """
    LeetCode Problem 763: Partition Labels
    Link: https://leetcode.com/problems/partition-labels/

    Problem:
    A string s of lowercase English letters is given. We want to partition this string into as many parts as possible
    so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

    Approach:
    - Use a dictionary to store the last occurrence of each character in the string.
    - Iterate through the string and track the end of the current partition.
    - When the current index matches the end of the partition, finalize the partition and start a new one.

    Args:
        s (str): Input string.

    Returns:
        List[int]: List of integers representing the size of each partition.
    """
    last_occurrence = {char: idx for idx, char in enumerate(s)}  # Map each character to its last occurrence
    partitions = []  # List to store the size of each partition
    start, end = 0, 0  # Start and end of the current partition

    for i, char in enumerate(s):
        end = max(end, last_occurrence[char])  # Update the end of the current partition
        if i == end:  # If the current index matches the end of the partition
            partitions.append(end - start + 1)  # Add the size of the partition to the list
            start = i + 1  # Start a new partition

    return partitions