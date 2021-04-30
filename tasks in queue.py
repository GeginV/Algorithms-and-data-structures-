def is_empty():
    return head == tail and queue[head] == 0


def size():
    if is_empty():
        return 0
    elif head == tail:
        return N_max
    elif head > tail:
        return N_max - head + tail
    else:
        return tail - head


def add():
    global tail, order
    order += 1
    queue[tail] = order
    print('Task #%d added' %(queue[tail]))
    tail = (tail + 1) % N_max


def show():
    print("Task #%d is in priority" %(queue[head]))


def do():
    global head
    print("Task #%d complete" %(queue[head]))
    queue[head] = 0
    head = (head + 1) %N_max


N_max = int(input("Define queue size:"))
commands = ['empty', 'size', 'add', 'show', 'do', 'exit']
print('List of commands: ', commands)

queue = [0 for _ in range(N_max)]
order = 0
head = 0
tail = 0

while True:
    cmd = input("Give command:")
    if cmd == "empty":
        if is_empty():
            print("Queue is empty")
        else:
            print("There are tasks in queue")
    elif cmd == "size":
        print("Tasks in queue:", size())
    elif cmd == "add":
        if size() != N_max:
            add()
        else:
            print("Queue is full")
    elif cmd == "show":
        if is_empty():
            print("Queue is empty")
        else:
            show()
    elif cmd == "do":
        if is_empty():
            print("Queue is empty")
        else:
            do()
    elif cmd == "exit":
        for _ in range(size()):
            do()
        print("Queue is empty. Shutting down")
        break
    else:
        print("Unknown command")
