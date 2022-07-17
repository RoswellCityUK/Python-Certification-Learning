"""
Create class Stack as a data structure that allows items to be added at the top of a list,
and only removed from the top.
"""


class Stack:
    def __init__(self):
        self.__stackitems = []

    def get_stack_items(self):
        return self.__stackitems

    def get_items_number(self):
        return self.__stackitems.__len__()

    def push(self, item):
        if (type(item) is int) | (type(item) is float):
            print("Pushing element", item, "to the list:", self.__stackitems)
            self.__stackitems.insert(0, item)
        else:
            print("Stack don't accept", type(item), "- only int and float elements")

    def pop(self):
        if self.get_items_number() > 0:
            return self.__stackitems.pop(0)
        else:
            print("List is empty")
            return False


mystack = Stack()
mystack.push(10)
print(mystack.get_stack_items())
mystack.push(30)
print(mystack.get_stack_items())
mystack.push(12)
print(mystack.get_stack_items())
print(mystack.pop())
print(mystack.pop())
print(mystack.pop())
print(mystack.pop())
mystack.push(12)
mystack.push(23)
mystack.push(432)
mystack.push(132)
mystack.push(542)
mystack.push("23")
print(mystack.get_stack_items())
