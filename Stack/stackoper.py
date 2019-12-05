class Stack:
    def __init__(self):
        self.things=[]
    def push(self,item):
        self.things.append(item)
    def popp(self):
        return self.things.pop()
    def is_empty(self):
        if(self.things == []):
            return True
        else:
            return False
    def peek(self):
        if(not self.is_empty()):
            return self.things[-1]
        else:
            return False

row = Stack()
row.push('A')
row.push('B')
row.push('C')
print(row.things)
row.popp()
row.popp()
row.popp()
print(row.peek())