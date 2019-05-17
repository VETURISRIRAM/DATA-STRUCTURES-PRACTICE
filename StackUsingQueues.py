class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.driverStack = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.driverStack == []:
            self.driverStack.append(x)
        else:
            self.driverStack = [x] + self.driverStack
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.driverStack != []:
            return self.driverStack.pop()
        else:
            return None
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.driverStack != []:
            return self.driverStack[-1]
        else:
            return None
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if self.driverStack == []:
            return True
        else:
            return None
# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
# obj.push(4)
# obj.push(5)
# obj.push(6)
param_2 = obj.pop()
print('Popped Element :', param_2)
param_2 = obj.pop()
print('Popped Element :', param_2)
param_2 = obj.pop()
print('Popped Element :', param_2)
param_2 = obj.pop()
print('Popped Element :', param_2)
param_3 = obj.peek()
print('Peeked Element :', param_3)
param_4 = obj.empty()
print('Is Queue Empty :', param_4)