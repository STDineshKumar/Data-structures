""" Priotity Queue is an abstract data structure.
    Logic:
    -------
        Priority queue expects some sort of order in the data that is feed to it.
"""
import random

class PriorityQueue(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.pq = []
    
    def push(self, value):
        if len(self.pq) < self.capacity:
            self.pq.append(value)
        else:
            print("Priority queue is full!!!")

    def delMax(self):
        self.popMax()

    def popMax(self):
        max_index = self._findMaxIndex()
        self.pq[-1], self.pq[max_index] = self.pq[max_index], self.pq[-1]
        return self.pq.pop()

    def popMin(self):
        min_index = self._findMinIndex()
        self.pq[-1], self.pq[min_index] = self.pq[min_index], self.pq[-1]
        return self.pq.pop()

    def isEmpty(self):
        return False if len(self.pq) else True

    def insert(self, pos, value):
        self.pq.insert(-pos,value)

    def _findMaxIndex(self):
        max_index = 0
        for i in range(len(self.pq)):
            if self.pq[i] > self.pq[max_index]:
                max_index = i
        return max_index
            
    def _findMinIndex(self):
        min_index = 0
        for i in range(len(self.pq)):
            if self.pq[i] < self.pq[min_index]:
                min_index = i
        return min_index

if __name__ == "__main__":
    pq = PriorityQueue(10)
    for i in range(11):
        pq.push(random.randint(1, 100))
    
    print(pq.pq)
    print(pq.popMax())
    print(pq.pq)
    print(pq.popMin())