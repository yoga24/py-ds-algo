from structures.queue import Queue


def hot_potato(names, num):
    game_queue = Queue()
    for name in names:
        game_queue.enqueue(name)

    while game_queue.size() > 1:
        for index in range(num - 1):
            member = game_queue.dequeue()
            game_queue.enqueue(member)

        print(game_queue.dequeue() + ' has been knocked out!')

    print("Winner is '" + game_queue.dequeue() + "'")


hot_potato(['Yoga', 'Lakshmi', "John", "Keerthy", "Mani", "Ponsubha"], 8)
