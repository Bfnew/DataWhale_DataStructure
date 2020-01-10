# -*- coding:utf-8 -*-
"""
@author: Xiaoxin
@file: task1_array.py
@time: 2020/1/5 21:33
"""

class Solution1:
    """
    1. 利用动态数组解决数据存放问题

    编写一段代码，要求输入一个整数N，用动态数组A来存放2~N之间所有5或7的倍数，输出该数组。
    思路：遍历2至N之间的整数，然后选出能5或者7的倍数放入该数组，最后输出
    """
    def array1(self, N):
        res = []
        for i in range(2, N+1):
            if (i % 5) == 0 or (i % 7) == 0:
                res.append(i)
        return res

class Solution2:
    """
    2.托普利茨矩阵问题

    托普利茨矩阵：对角线的值相等（M*N）
    则可以发现，矩阵上一行的前N-1个值[:-1]==矩阵下一行的后N-1个值[1:]的值
    """
    def isToeplitzMatrix(self, matrix):
        for i in range(len(matrix) - 1):
            if not matrix[i][:-1] == matrix[i+1][1:]:
                return False
        return True

class Solution3:
    """
    3. 三数之和
    给定一个包含 n 个整数的数组nums，判断nums中是否存在三个元素a，b，c，使得a + b + c = 0？找出所有满足条件且不重复的三元组。
    结果须去重

    思路：1，先将数组排序。
         2，排序后，可以按照TwoSum的思路来解题。怎么解呢？可以将num[i]的相反数即-num[i]作为target，然后从i+1到len(num)-1的数组元素中寻找两个数使它们的和为-num[i]就可以了。下标i的范围是从0到len(num)-3。
         3，这个过程要注意去重。
    """
    def threeSum(self, nums):
        "1.首先对输入的数组进行排序"
        nums.sort()
        # print(nums)
        res = [] # 用于保存结果
        for i in range(len(nums)):
            # 去掉重复值 1
            if i == 0 or nums[i] > nums[i-1]:
                m = i + 1
                n = len(nums) - 1
                while m < n:
                    s = nums[i] + nums[m] + nums[n]
                    if s == 0:
                        res.append([nums[i], nums[m], nums[n]])
                        ## m 和 n就不能重复了
                        m += 1
                        n -= 1
                        ### 去掉重复值
                        while m < n and nums[m] == nums[m-1]:
                            m += 1
                        while m < n and nums[n] == nums[n+1]:
                            n -= 1
                    elif s > 0:
                        n -= 1
                    else:
                        m += 1
        return res



if __name__ == '__main__':
    sol1 = Solution1()
    output1 = sol1.array1(100)
    print(output1)

    matrix = [
        [1, 2, 3, 4],
        [5, 1, 2, 3],
        [9, 5, 1, 2]
    ]
    sol2 = Solution2()
    output2 = sol2.isToeplitzMatrix(matrix)
    print(output2)

    nums = [-1, 0, 1, 2, -1, -4]
    sol3 = Solution3()
    output3 = sol3.threeSum(nums)
    print(output3)