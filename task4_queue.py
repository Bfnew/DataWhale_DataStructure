# -*- coding:utf-8 -*-
"""
@author: Xiaoxin
@file: task4_queue.py
@time: 2020/1/12 20:49
"""

"""
模拟银行服务完成程序代码

程序运行后，当看到“请点击触摸屏获取号码：”的提示时，只要按回车键，即可显示“您的号码是：XXX，您前面有YYY位”的提示，其中XXX是所获得的服务号码，YYY是在XXX之前来到的正在等待服务的人数。
用多线程技术模拟服务窗口（可模拟多个），具有服务员呼叫顾客的行为，假设每个顾客服务的时间是10000ms(10s)，时间到后，显示“请XXX号到ZZZ号窗口！”的提示。其中ZZZ是即将为客户服务的窗口号。

主要思路：如果子线程和主线程放在一起实现就会存在问题，所以银行的服务窗口单独继承线程进行实现（怪不得说python的线程都是假的）
1.首先实现队列这个类
2.实现柜台窗口的继承函数
3.实现用户排队取号功能
"""

import time, threading

##### 实现栈这个类
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        if self.items != []:
            return self.items.pop()
        else:
            return False

    def size(self):
        return len(self.items)

    def top(self):
        if self.items != []:
            return self.items[len(self.items)-1]
        else:
            return False

### 实现银行柜台叫号功能

class Counter(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.waitQueue = Queue() ## 初始化等待的队伍
        self.lock = threading.Lock()

    def callIng(self):
        while True:
            ### 柜台一直叫号，要一直循环
            time.sleep(5)
            if not self.waitQueue.isEmpty():
                self.lock.acquire()
                print("请客户{},到{}窗口办理业务".format(self.waitQueue.top(), threading.current_thread().name))
                self.waitQueue.dequeue()
                self.lock.release()


class bankSystem:
    def __init__(self):
        self.serviceQueue = Queue()
        self.nowNum = 0
        # self.windows = k  # 银行柜台数目
        self.maxSize = 1000000

    def getNumber(self):
        if self.nowNum < self.maxSize:
            self.nowNum += 1
            return self.nowNum
        else:
            print("现在业务繁忙，请稍后再来")


if __name__ == "__main__":
    res = bankSystem()
    windowcount = 3
    serviceWindow = [None] * windowcount
    threadList = [None] * windowcount

    for i in range(windowcount):
        serviceWindow[i] = Counter()
        serviceWindow[i].waitQueue = res.serviceQueue
        threadList[i] = threading.Thread(name=(i + 1), target=serviceWindow[i].callIng, args=())
        threadList[i].start()
        # threadList[i].join()

    while True:
        input("请点击触摸屏获取号码：")
        # print()
        callNumber = res.getNumber()
        if res.serviceQueue != None:
            print("当前您的的号码为" + str(callNumber) + "，您前面还有" + str(res.serviceQueue.size()) + "个人")
            res.serviceQueue.enqueue(res.nowNum)
        else:
            print('您的号码是：%d，您前面有 0 位' % (callNumber))
        # for i  in range(windowcount):
        #     threadList[i].join()  加了join会出bug


