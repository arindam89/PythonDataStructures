"""
Test cases for the LeetCode problem: Design Twitter
Link: https://leetcode.com/problems/design-twitter/

The test cases validate the following scenarios:
1. Posting tweets and retrieving the user's own tweets.
2. Following and unfollowing users.
3. Retrieving the news feed with tweets from followed users.
"""

import unittest
from src.leetcode.heaps.design_twitter import Twitter

class TestDesignTwitter(unittest.TestCase):
    def test_case_1(self):
        twitter = Twitter()
        twitter.postTweet(1, 5)
        self.assertEqual(twitter.getNewsFeed(1), [5])  # User 1's own tweet

    def test_case_2(self):
        twitter = Twitter()
        twitter.postTweet(1, 5)
        twitter.follow(1, 2)
        twitter.postTweet(2, 6)
        self.assertEqual(twitter.getNewsFeed(1), [6, 5])  # Tweets from user 1 and 2
        twitter.unfollow(1, 2)
        self.assertEqual(twitter.getNewsFeed(1), [5])  # Only user 1's tweet

    def test_case_3(self):
        twitter = Twitter()
        twitter.postTweet(1, 5)
        twitter.postTweet(1, 3)
        twitter.postTweet(1, 101)
        twitter.postTweet(1, 13)
        twitter.postTweet(1, 10)
        twitter.postTweet(1, 2)
        twitter.postTweet(1, 94)
        twitter.postTweet(1, 505)
        twitter.postTweet(1, 333)
        twitter.postTweet(1, 22)
        twitter.postTweet(1, 11)
        self.assertEqual(len(twitter.getNewsFeed(1)), 10)  # Only 10 most recent tweets

if __name__ == "__main__":
    unittest.main()