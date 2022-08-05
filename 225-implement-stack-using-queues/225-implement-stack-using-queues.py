class MyStack:

    def __init__(self):
        self.q1=deque()
        self.q2=deque()
        

    def push(self, x: int) -> None:
    
        
        while(len(self.q1)):
            self.q2.append(self.q1.pop())
            
        self.q1.append(x)

        while(len(self.q2)):
            self.q1.append(self.q2.pop())
        
        

    def pop(self) -> int:
        if len(self.q1)==0:
            print("Underflow")
            
        front=self.q1.popleft()
        return front
        

    def top(self) -> int:
        if self.q1:
            return self.q1[0]
        
        
    
    def empty(self) -> bool:
        
          if len(self.q1)==0:
            return True
          else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()