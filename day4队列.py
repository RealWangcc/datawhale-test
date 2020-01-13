#理论部分
"""
用数组实现一个顺序队列。
用数组实现一个循环队列。
用链表实现一个链式队列。
练习部分
1. 模拟银行服务完成程序代码。
目前，在以银行营业大厅为代表的窗口行业中大量使用排队（叫号）系统，该系统完全模拟了人群排队全过程，通过
取票进队、排队等待、叫号服务等功能，代替了人们站队的辛苦。
排队叫号软件的具体操作流程为：
顾客取服务序号
当顾客抵达服务大厅时，前往放置在入口处旁的取号机，并按一下其上的相应服务按钮，取号机会自动打印出一张服
务单。单上显示服务号及该服务号前面正在等待服务的人数。
服务员工呼叫顾客
服务员工只需按一下其柜台上呼叫器的相应按钮，则顾客的服务号就会按顺序的显示在显示屏上，并发出“叮咚”和
相关语音信息，提示顾客前往该窗口办事。当一位顾客办事完毕后，柜台服务员工只需按呼叫器相应键，即可自动呼
叫下一位顾客。
编写程序模拟上面的工作过程，主要要求如下：
程序运行后，当看到“请点击触摸屏获取号码：”的提示时，只要按回车键，即可显示“您的号码是：XXX，您前面有
YYY位”的提示，其中XXX是所获得的服务号码，YYY是在XXX之前来到的正在等待服务的人数。
用多线程技术模拟服务窗口（可模拟多个），具有服务员呼叫顾客的行为，假设每个顾客服务的时间是10000ms，时间
到后，显示“请XXX号到ZZZ号窗口！”的提示。其中ZZZ是即将为客户服务的窗口号。

"""
def getCallNumber(self):
    if self.is_empty() and self.callNumber == 0:
        self.callNumber = 1
    else:
        self.callNumber += 1
    return self.callNumber

def getLength(self):
    if self.is_empty():
        return 0
    else:
        cur = self._head
        len = 1
        while cur != self._tail:
            cur = cur.next
            len += 1
        return len

def service(self):
    self.lock.acquire()
    while True:
        time.sleep(20)
        try:
            if not self.bankQueue.is_empty():
                print('请 %d 号到 %s 号窗口' % (self.bankQueue._head.data, threading.current_thread().name))
                self.bankQueue.dequeue()
                # time.sleep(10)
            else:
                print('队列为空哦')
        finally:
            self.lock.release()