import pytest
from src.leetcode.dp.decode_ways import num_decodings

def test_num_decodings():
    assert num_decodings("12") == 2  # "AB" (1,2) and "L" (12)
    assert num_decodings("226") == 3  # "BZ" (2,26), "VF" (22,6), "BBF" (2,2,6)
    assert num_decodings("0") == 0  # No valid decoding
    assert num_decodings("06") == 0  # No valid decoding
    assert num_decodings("11106") == 2  # "AAJF" (1,1,10,6) and "KJF" (11,10,6)