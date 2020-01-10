#理论部分
"""
用数组实现一个顺序栈。
用链表实现一个链栈。
理解递归的原理。
练习部分
1. 根据要求完成车辆重排的程序代码

假设一列货运列车共有n节车厢，每节车厢将停放在不同的车站。假定n个车站的编号分别为1至n，货运列车按照第
n站至第1站的次序经过这些车站。车厢的编号与它们的目的地相同。为了便于从列车上卸掉相应的车厢，必须重新
排列车厢，使各车厢从前至后按编号1至n的次序排列。当所有的车厢都按照这种次序排列时，在每个车站只需卸掉
最后一节车厢即可。
我们在一个转轨站里完成车厢的重排工作，在转轨站中有一个入轨、一个出轨和k个缓冲铁轨（位于入轨和出轨之间）
。图（a）给出一个转轨站，其中有k个（k=3）缓冲铁轨H1，H2 和H3。开始时，n节车厢的货车从入轨处进入转轨站，
转轨结束时各车厢从右到左按照编号1至n的次序离开转轨站（通过出轨处）。在图（a）中，n=9，车厢从后至前的初
始次序为5，8，1，7，4，2，9，6，3。图（b）给出了按所要求的次序重新排列后的结果。

编写算法实现火车车厢的重排，模拟具有n节车厢的火车“入轨”和“出轨”过程。
"""
class stack(object):
    def __init__(self):
        self.stack=[]
    def append(self,value):
        self.stack.append(value)
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return False
    def top(self):
        return self.stack[-1]
def f(cars,k):
    cacheLists = []
    for i in range(k):
        cacheLists.append([])
    init = 1
    for i in cars:
        if i == init:
            print('{}号车厢入轨->出轨'.format(i))
            init += 1
            continue
        else:
            for list_item in cacheLists:
                if not list_item:
                    list_item.append(i)
                    break
                else:
                    if min(list_item) > i:
                        list_item.append(i)
                        break

    for item in cacheLists:
        for i in range(len(item)):
            last = item.pop()
            if last == init:
                print('{}号车厢入轨->出轨'.format(last))
                init += 1


car = [3, 6, 9, 2, 4, 7, 1, 8, 5]
n = 3
print(f(car, n))