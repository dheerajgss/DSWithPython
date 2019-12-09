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

def reverse(sting):
    s = Stack()
    for i in range(len(sting)):
        s.push(sting[i])
    for i in range(len(sting)):
        print(s.popp(),end='')
    print()
    return

def main():
    s = input("Enter a string: ")
    print("Reversed string is: ",end='')
    reverse(s)

main()