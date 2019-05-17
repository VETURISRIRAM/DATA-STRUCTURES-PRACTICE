class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.driverQueue = []
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)
        self.driverQueue = self.queue[::-1]
        print(self.queue, self.driverQueue)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.driverQueue != []:
            poppedElement = self.driverQueue[0]
            self.driverQueue = self.driverQueue[1:]
            return poppedElement
        else:
            return None
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.driverQueue != []:
            return self.driverQueue[0]
        else:
            return None
        
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if self.driverQueue == []:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
param_3 = obj.top()
print(param_3)
param_2 = obj.pop()
print(param_2)
param_4 = obj.empty()
print(param_4)