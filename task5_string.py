# -*- coding:utf-8 -*-
"""
@author: Xiaoxin
@file: task5_string.py
@time: 2020/1/12 22:30
"""


### 第一个任务
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        else:
            maxlen = 0
            left = -1
            for i, x in enumerate(s):
                if x in s[left+1:i]:
                    maxlen = max(maxlen, i-left-1)
                    left = s[left+1:i].index(x)+left+1
            return max(maxlen, len(s)-left-1)

class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        else:
            left = 0
            lookup = set()
            n = len(s)
            max_len = 0
            cur_len = 0
            for i in range(n):
                cur_len += 1
                while s[i] in lookup:
                    lookup.remove(s[left])
                    left += 1
                    cur_len -= 1
                if cur_len > max_len:max_len = cur_len
                lookup.add(s[i])
            return max_len

"""
统计字符个数  第3个任务
只考虑大于n // 4的字符，目标找到最短的子串将这些多的字符替换掉。
窗口中s[l,r]就是子串candidate:
1）如果子串里包含了足够多要替换的字符，则l += 1， 缩小考察范围；
2）如果子串里需要换掉的字符不够，则r += 1，考察更多的字符；

"""


class Solution3:
    def balancedString(self, s):
        n = len(s)
        b = n // 4
        from collections import Counter
        counter = Counter(s)
        counter = {key: value for key, value in counter.items() if value > b}

        if not counter or n < 4:
            return 0
        rmove = True

        l, r = 0, 0
        minlen = n

        while l <= r and r < n:

            if s[r] in counter and rmove:
                counter[s[r]] -= 1
            elif l > 0 and s[l - 1] in counter and not rmove:
                counter[s[l - 1]] += 1

            if {key: value for key, value in counter.items() if value > b}:
                r += 1
                rmove = True
            else:
                minlen = min(minlen, r - l + 1)
                l += 1
                rmove = False

        return minlen

#### 第2个任务
"""
给定一个字符串s和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

思路：使用窗口滑动的方式，因单词长度相同，使用hash表来统计字符个数
"""
class Solution4:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        from collections import Counter
        if not s or not words:
            return []

        words_len = len(words[0])           # 一个单词的长度
        words_num = len(words)              # words中单词的个数
        words_cnt = Counter(words)          # {'foo': 1, 'bar': 1}
        s_len = len(s)                      # 字符串s的长度
        res = []                            # 存储起始位置

        W = words_len * words_num           # 此处窗口大小为 2*3
        left = 0
        while (left + W) <= s_len:
            tmp = []
            i = left
            for j in range(words_num):       # 将窗口内的字符串添加到tmp中
                tmp.append(s[i:i + words_len])
                i = i + words_len
            tmp = Counter(tmp)
            if tmp == words_cnt:
                res.append(left)
                left = left + 1
            else:
                left = left + 1
        return res


if __name__ == "__main__":
    a1 = Solution()
    print(a1.lengthOfLongestSubstring("abcabcbb"))

    a2 = Solution3()
    print(a2.balancedString("WWQQRRRRQRQQ"))

    a3 = Solution4()
    print(a3.findSubstring("barfoothefoobarman", ["foo","bar"]))

