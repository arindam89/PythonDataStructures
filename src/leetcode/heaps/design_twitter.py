"""
LeetCode Problem: Design Twitter
Link: https://leetcode.com/problems/design-twitter/

Approach:
- Use a combination of hash maps and a Min-Heap to implement the required functionality.
- Maintain a global timestamp to order tweets.
- Use a hash map to store user follow relationships and another to store user tweets.
- For retrieving the news feed, use a Min-Heap to merge the most recent tweets from followed users.

Time Complexity:
- Post Tweet: O(1)
- Follow/Unfollow: O(1)
- Get News Feed: O(n log k), where n is the number of followed users and k is the number of tweets per user.

Space Complexity: O(u + t), where u is the number of users and t is the total number of tweets.
"""

import heapq
from collections import defaultdict, deque

class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timestamp = 0
        self.tweets = defaultdict(deque)  # Map userId to a deque of (timestamp, tweetId)
        self.followees = defaultdict(set)  # Map userId to a set of followees

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets[userId].appendleft((self.timestamp, tweetId))
        self.timestamp += 1

        # Keep only the 10 most recent tweets per user
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop()

    def getNewsFeed(self, userId: int) -> list[int]:
        """
        Retrieve the 10 most recent tweet IDs in the user's news feed.
        """
        min_heap = []

        # Add the user's own tweets
        for tweet in self.tweets[userId]:
            heapq.heappush(min_heap, tweet)

        # Add tweets from followees
        for followeeId in self.followees[userId]:
            for tweet in self.tweets[followeeId]:
                heapq.heappush(min_heap, tweet)

        # Extract the 10 most recent tweets
        return [tweetId for _, tweetId in heapq.nlargest(10, min_heap)]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee.
        """
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee.
        """
        self.followees[followerId].discard(followeeId)