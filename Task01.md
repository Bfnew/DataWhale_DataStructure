# Task01：数组

## 1. 数组的定义

数组是具有一定顺序关系的若干对象组成的集合，组成数组的对象称为数组元素。

例如：

- 向量对应一维数组
- 矩阵对应二维数组

数组名表示群体的共性，即具有同一种数据类型；下标表示个体的个性，即各自占有独立的单元。

## 2. 数组的存储

**2.1 n维数组的定义**

下标由n个数组成的数组称为n维数组。

例如：

- `int[] a = new int[10]; //一维数组（线）`
- `int[ , ] a = new int[2,3];//二维数组 （面）`
- `int[ , , ] a = new int[2,3,4];//三维数组 （体）；类比：书（体）【2.页码 3.行 4.列】` 

**2.2 数组存储的特点**

- 数组元素在内存中按顺序连续存储。
- 数组的存储分配按照行（C、C++、C#等）或列（Forturn等）进行。
- 数组名表示该数组的首地址，是常量。

**2.3 常用数组的存储**

<u>一维数组`a[n]`</u>

各元素按下角标依次存放。

例：`int[] a = new int[5];`

![一维数组存储](https://img-blog.csdnimg.cn/20191218195949938.png)

<u>二维数组`a[m,n]`</u>

例：`int[ , ] a = new int[2,3];`

![二维数组存储](https://img-blog.csdnimg.cn/20191218200106993.png)

<u>三维数组`a[m,n,l]`</u>

第一维下标变化最慢，第三维（最后一维）下标变化最快。

例：`int[ , , ] a = new int[2,3,4];`

![三维数组的存储](https://img-blog.csdnimg.cn/20191218200209131.png)

## 3. 静态数组与动态数组

**3.1 静态数组**

在程序编译时分配空间的数组。

例：
`int[] a = new int[10];//静态数组（声明之后数组长度不可改变）`

**3.2 动态数组**

在程序运行时分配空间的数组（声明之后数组长度可根据问题而调整）。

![动态数组类图](https://img-blog.csdnimg.cn/2019121820102094.png)

## 4.练习参考答案

<u>1. 利用动态数组解决数据存放问题</u>

编写一段代码，要求输入一个整数`N`，用动态数组`A`来存放`2~N`之间所有5或7的倍数，输出该数组。

示例：
```c
输入：
N = 100 

输出：
5 7 10 14 15 20 21 25 28 30 35 40 42 45 49 50 55 56 60 63 65 70 75 77 80 84 85 90 91 95 98 100
```

<u>2. 托普利茨矩阵问题</u>

如果一个矩阵的每一方向由左上到右下的对角线上具有相同元素，那么这个矩阵是托普利茨矩阵。

给定一个`M x N`的矩阵，当且仅当它是托普利茨矩阵时返回`True`。

示例：

```c
输入:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]

输出: True
```
解释:

在上述矩阵中, 其对角线为:
`"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]"`。
各条对角线上的所有元素均相同, 因此答案是`True`。


<u>3. 三数之和</u>

https://leetcode-cn.com/problems/3sum/

给定一个包含 n 个整数的数组`nums`，判断`nums`中是否存在三个元素`a，b，c`，使得`a + b + c = 0`？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例：

```c
给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

分别构建三个类对上述三个问题进行解答，具体`Python`代码如下：
```python
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
```