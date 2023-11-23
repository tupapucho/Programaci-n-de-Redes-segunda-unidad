'''
Autor: Antonio Uribe Ramirez
lab: 3.2.1.15
fecha: 22/11/10
'''
class QueueError(Exception):
    pass

class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, elem):
        self.__queue.insert(0, elem)

    def get(self):
        if not self.__queue:
            raise QueueError("Error de Cola")
        return self.__queue.pop()

que = Queue()
que.put(1)
que.put("perro")
que.put(False)

try:
    for _ in range(4):
        print(que.get())
except QueueError:
    print("Error de Cola")
