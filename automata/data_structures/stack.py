class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append((item))

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)

    def top(self):
        return self.stack[self.size() - 1]

    def __contains__(self, item):
        for x in self.stack:
            #print ("in Stack" + str(x))
            if x == item:
                return True

        return False


    def __str__(self):
        output = "[  "
        for x in self.stack:
            output += str(x)
            output += ", "

        return output[:-2] + " ]"