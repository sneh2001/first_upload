

class Deque:

    def _init_(self):
        self.items = []

    def is_Empty(self):
        return self.items ==[0]
    
    def add_first(self, items):
        self.items.insert(0,items)
    
    def add_last(self, items):
        self.items.append(items)
        
    def delete_first(self):
        if self.is_Empty():
            raise Exception('Deque is empty')
        else:
            return self.items.pop(0)

    def delete_last(self):
        if self.is_Empty():
            raise Exception('Deque is empty')
        else:
            return self.items.pop()

    def _len_(self):
        return len(self.items)
    
    def first(self):
        if self.is_Empty():
            raise Exception('Deque is empty')
        else:
            return self.items[0]
    
    def last(self):
        if self.is_Empty():
            raise Exception('Deque is empty')
        else:
            return self.items[-1]


d=Deque()
print("Is the list empty ? :",d.is_Empty())

d.add_first(RAM)
print("After add_first(RAM)  ",d.items)
d.add_first(HARI)
print("After add_first(HARI)  ",d.items)

d.add_last(KHUSH)
print("After add_last(KHUSH)  ",d.items)
d.add_last(JAY)
print("After add_last(JAY)  ",d.items)

print("Is the list empty ? :",d.is_Empty())

print(d.delete_first())
print("After delete_first()  ",d.items)

print(d.delete_last())
print("After delete_last()  ",d.items)

print("The length:  ",d._len_())

print("The first element is  ",d.first())

print("The last element is  ",d.last())
