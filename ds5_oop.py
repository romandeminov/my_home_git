class StackStr:
    def __init__(self):
        self.stack = []
        self.max_len = 8
        self.len = 0

    def push(self, val: str):
        if self.len >= self.max_len:
            return f'max len stack'
        elif type(val) != str:
            return f'type not str'
        else:
            self.stack.append(val)
            self.len += 1
            return f'успешно добавлено'

    def get(self):
        if self.len == 0:
            return None
        else:
            ret = self.stack.pop()
            self.len -= 1
        return ret

    def get_len(self):
        return self.len

    def empty(self):
        if self.len == 0:
            return 'Stack - пуст'
        else:
            return 'Stack - не пуст'

    def full(self):
        if self.len == self.max_len:
            return 'Stack - полон'
        else:
            return 'Stack - не полон'

    def clear(self):
        for i in range(self.len):
            self.stack.pop()
        self.len = 0

    def get_no_pop(self):
        return self.stack[-1]


my_stack = StackStr()
my_stack.push('aaaa')
my_stack.push('bbbb')
print(my_stack.stack)
my_stack.get()
my_stack.get()
print(my_stack.stack)
print(my_stack.get_len())
print(my_stack.empty())
print(my_stack.full())
my_stack.push('aaaa')
print(my_stack.get_no_pop())
print(my_stack.stack)



