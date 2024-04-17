from queues import Queue

my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

# Use duck typing with special methods.
a = [item for item in my_queue]
b = len(my_queue)
c = list(reversed(my_queue))
d = 2 in my_queue

print(a)
print(b)
print(c)
print(d)