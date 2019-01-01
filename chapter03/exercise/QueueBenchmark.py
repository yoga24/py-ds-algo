import timeit
from structures.queue import Queue as RearInsertQueue
from chapter03.exercise.QueueFrontInsertion import Queue as FrontInsertQueue

front_enqueue_setup = '''
from chapter03.exercise.QueueFrontInsertion import Queue as FrontInsertQueue
queue = FrontInsertQueue()
'''
front_enqueue_code = '''
for n in  range(10000):
    queue.enqueue(n)
'''

rear_enqueue_setup = '''
from structures.queue import Queue as RearInsertQueue
queue = RearInsertQueue()
'''
rear_enqueue_code = '''
for n in  range(10000):
    queue.enqueue(n)
'''

front_dequeue_setup = '''
from chapter03.exercise.QueueFrontInsertion import Queue as FrontInsertQueue
queue = FrontInsertQueue()
for n in  range(10000):
    queue.enqueue(n)
'''
front_dequeue_code = '''
while not queue.is_empty():
    queue.dequeue()
'''

rear_dequeue_setup = '''
from structures.queue import Queue as RearInsertQueue
queue = RearInsertQueue()
for n in  range(10000):
    queue.enqueue(n)
'''
rear_dequeue_code = '''
while not queue.is_empty():
    queue.dequeue()
'''

print('Front EnQueue Time -> '+str(timeit.timeit(front_enqueue_code, front_enqueue_setup, number=50)))
print('Rear EnQueue Time  -> '+str(timeit.timeit(rear_enqueue_code, rear_enqueue_setup, number=50)))
print('Front DeQueue Time -> '+str(timeit.timeit(front_dequeue_code, front_dequeue_setup, number=50)))
print('Rear DeQueue Time  -> '+str(timeit.timeit(rear_dequeue_code, rear_dequeue_setup, number=50)))

# front end queue insertion

