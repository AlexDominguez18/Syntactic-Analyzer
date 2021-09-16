class Stack():

    def __init__(self):
        self._stack = []

    def __str__(self):
        o = ""
        for i in self._stack:
            o += str(i) + " "
        return o
    
    def push(self,item):
        self._stack.append(item)
    
    def pop(self):
        return self._stack.pop()
    
    def top(self):
        return self._stack[len(self._stack)-1]

    def isEmpty(self):
        return len(self._stack) == 0

    def size(self):
        return len(self._stack)
    
    def clear(self):
        self._stack.clear()