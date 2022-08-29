class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.k = k
        self.q = [None]*k
        self.front=self.rear=-1

    def insertFront(self, value):
        if self.isEmpty():
            self.front, self.rear=0,0
            self.q[self.front]=value
            return True
        elif not self.isFull():
            self.front = (self.front-1)%self.k
            self.q[self.front]=value
            return True
        return False
            
    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isEmpty():
            self.front, self.rear=0,0
            self.q[self.rear]=value
            return True
        elif not self.isFull():
            self.rear = (self.rear+1)%self.k
            self.q[self.rear]=value
            return True
        return False

    def deleteFront(self):
        """
        :rtype: bool
        """
        if not self.isEmpty():
            if self.front!=self.rear:
                self.front=(self.front+1)%self.k
            else:
                self.front,self.rear=-1,-1
            return True
        return False

    def deleteLast(self):
        """
        :rtype: bool
        """
        if not self.isEmpty():
            if self.front!=self.rear:
                self.rear=(self.rear-1)%self.k
            else:
                self.rear = -1
                self.front=-1
            return True
        return False

    def getFront(self):
        """
        :rtype: int
        """
        if not self.isEmpty():
            return self.q[self.front]
        return -1
        

    def getRear(self):
        """
        :rtype: int
        """
        if not self.isEmpty():
            return self.q[self.rear]
        return -1
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.front==-1:
            return True
        return False

    def isFull(self):
        """
        :rtype: bool
        """
        if self.front == (self.rear+1)%self.k:
            return True
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
