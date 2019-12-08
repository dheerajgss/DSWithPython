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

def matching(p1,p2):
    if(p1=='(' and p2 == ')'):
        return True
    elif(p1=='[' and p2==']'):
        return True
    elif(p1=='{' and p2=='}'):
        return True
    else:
        return False

def balance(stri):
    s = Stack()
    isbalanced = True
    i = 0
    while(i < len(stri) and isbalanced):
        if(stri[i] in '({['):
            s.push(stri[i])
        else:
            if(s.is_empty()):
                isbalanced = False
            else:
                top = s.popp()
                if(not(matching(top, stri[i]))):
                    isbalanced = False
        i += 1
    if(s.is_empty() and isbalanced):
        return True
    else:
        return False

def main():
    print("This program tells whether gives brackets are balanced or not.")
    stri = input("Enter some paranthesis/brackets: ")
    print(balance(stri))

main()