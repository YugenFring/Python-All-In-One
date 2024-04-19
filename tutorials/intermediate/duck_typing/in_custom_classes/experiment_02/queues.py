from collections import deque

class Queue:
    def __init__(self):
        self._elements = deque()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()
    
    # A special method which allows this class
    # to support iterations.
    def __iter__(self):
        return iter(self._elements)
    
    # A special method which alloss this class
    # to support len() function.
    def __len__(self):
        return len(self._elements)
    
    # A special method which allows this class
    # to support reversed() fucntion.
    def __reversed__(self):
        return reversed(self._elements)

    # A special method which allow this class
    # to support membership tests.
    def __contains__(self, element):
        return element in self._elements
