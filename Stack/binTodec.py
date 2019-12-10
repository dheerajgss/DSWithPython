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

def convert(num):
    s = Stack()
    t = num
    while(t>0):
        s.push(t%2)
        t = t // 2
    st = ''
    while(not(s.is_empty())):
        st = st + str(s.popp())
    return st

n = int(input("Enter a number: "))
print("Binary of given number is: ",convert(n))