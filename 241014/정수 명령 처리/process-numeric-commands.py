class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, A):
        self.data.append(A)
    
    def pop(self):
        if self.empty():
            return Exception("Stack is empty")
        
        return self.data.pop()
    
    def size(self):
        return len(self.data)

    def empty(self):
        return int(not self.data)
    
    def top(self):
        if self.empty():
            return Exception("Stack is empty")

        return self.data[-1]

stack = Stack()

n = int(input())

for _ in range(n):
    command = input().strip().split()  # 명령어를 입력받음 (앞뒤 공백 제거)
    
    if command[0] == "push":
        stack.push(int(command[1]))
    elif command[0] == "pop":
        print(stack.pop())
    elif command[0] == "size":
        print(stack.size())
    elif command[0] == "empty":
        print(stack.empty())
    elif command[0] == "top":
        print(stack.top())