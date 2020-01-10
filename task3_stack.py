# -*- coding:utf-8 -*-
"""
@author: Xiaoxin
@file: task3_queue.py
@time: 2020/1/10 21:53
"""

"""
Task3：根据要求完成车辆重排的程序代码

假设一列货运列车共有n节车厢，每节车厢将停放在不同的车站。假定n个车站的编号分别为1至n，货运列车按照第n站至第1站的次序经过这些车站。车厢的编号与它们的目的地相同。为了便于从列车上卸掉相应的车厢，必须重新排列车厢，使各车厢从前至后按编号1至n的次序排列。当所有的车厢都按照这种次序排列时，在每个车站只需卸掉最后一节车厢即可。

我们在一个转轨站里完成车厢的重排工作，在转轨站中有一个入轨、一个出轨和k个缓冲铁轨（位于入轨和出轨之间）。图（a）给出一个转轨站，其中有k个（k=3）缓冲铁轨H1，H2 和H3。开始时，n节车厢的货车从入轨处进入转轨站，转轨结束时各车厢从右到左按照编号1至n的次序离开转轨站（通过出轨处）。在图（a）中，n=9，车厢从后至前的初始次序为5，8，1，7，4，2，9，6，3。图（b）给出了按所要求的次序重新排列后的结果。

思路：车厢重排可以考虑栈实现和队列实现两种方法，可以重新实现栈和队列。
为了重排车厢，需从前往后依次检查入轨上的所有车厢。
如果正在检查的车厢就是下一个满足要求的车厢，可以直接把它放到出轨上。
否则，则把它移动到缓冲轨上，直到按输出顺序要求轮到它的时候才可以将他放到出轨上。
缓冲轨是按照FILO的方式使用的，因为车厢的进出都是在缓冲轨的顶端进行的。

方法参考blog: https://blog.csdn.net/jkay_wong/article/details/6830541
"""


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


class stack_train():
    def __init__(self, p, n, k):
        """

        :param p: 初始车厢排序
        :param n: 所有的车厢数目
        :param k: 缓冲轨数目
        """
        # self.my_stack = [Stack()]*k  # 缓冲轨生成  该方法会生成相同对象，必须得遍历生成多次
        self.my_stack = []
        for i in range(k):
            self.my_stack.append(Stack())
        self.minH = n + 1            # 缓冲轨中最小的车厢号
        self.minS = k                # 最小车厢号所在的缓冲轨
        self.p = p
        self.n = n
        self.k = k

    "将车厢c放入缓冲轨中"
    def hold(self, c):
        """

        :param c: 第c节进入缓冲轨的车厢
        :param minH:当前缓冲轨中编号最小的车厢
        :param minS:编号最小的车厢所在的缓冲轨
        :param my_stack:所有的缓冲轨
        :param k: 缓冲轨数目
        :param n: 最优缓冲轨的栈顶车厢编号
        :return:
        """
        # 为车厢c寻找最优的缓冲轨
        k = self.k
        n = self.n
        bestTrack = k
        bestTop = n + 1

        for i in range(k):
            if not self.my_stack[i].isEmpty():
                # print("当前的最优缓冲轨为" + str(bestTrack))
                tmp = self.my_stack[i].peek()
                if c < tmp and tmp < bestTop:
                    bestTop = tmp
                    bestTrack = i
            else:
                # print("当前的最优缓冲轨为" + str(bestTrack))
                if bestTrack == k:
                    bestTrack = i
            # print("当前的最优缓冲轨为" + str(bestTrack))
        # print("当前的最优缓冲轨为"+str(bestTrack))
        if bestTrack == k:
            "没有可用的缓冲轨"
            return False
        self.my_stack[bestTrack].push(c)
        print("将车厢"+str(c)+"移动到缓冲轨"+str(bestTrack+1))
        # 更新minH和minS
        if c < self.minH:
            self.minH = c
            self.minS = bestTrack
        return True




    def output(self):
        "输出缓冲轨"
        tmp = self.my_stack[self.minS].peek()
        self.my_stack[self.minS].pop()
        print("将车厢"+str(tmp)+"从缓冲轨"+str(self.minS+1)+"移动输出轨道")
        ## 检查缓冲轨，更新minH和minS
        self.minH = self.n + 1

        for i in range(self.k):
            if (not self.my_stack[i].isEmpty()) and (self.my_stack[i].peek() < self.minH):
                self.minH = self.my_stack[i].peek()
                self.minS = i


    def railRoad(self):
        """

        :param p: 火车原顺序 [] list
        :param n: 火车总的车厢数目
        :param k: 缓冲轨数目
        :return: 火车车厢是否重排成功
        """
        "具体思路为：首先从头到尾开始遍历车厢，如果能出轨就出轨（加上到缓冲轨进行判断），不能出轨就入轨，如果都不能入轨则重排失败"
        # myStack = [Stack()]*n  # 生成n个缓冲轨

        nowOut = 1  # 初始化输出的车厢
        p = self.p
        n = self.n
        k = self.k
        # minH = n + 1 # 初始化 缓冲轨中编号最小的车厢
        # minS = k # 初始化 编号最小的车厢所在缓冲轨的编号

        for i in p:
            # print(i)
            if i == nowOut:
                print("移动车厢"+str(i)+"从原轨道出轨道")
                nowOut += 1
                while self.minH==nowOut:
                    self.output()
                    nowOut += 1
                    if nowOut == n + 1:
                        print("所有车厢重排成功")
                        return True
            else:
                if not self.hold(i):
                    print("缓冲轨数目较少，车厢重排失败")
                    return False
        print("所有车厢重排成功")
        return True

if __name__ == "__main__":
    p = [5, 8, 1, 7, 4, 2, 9, 6, 3]
    k = 3
    n = 9
    res = stack_train(p, n, k)
    res.railRoad()











