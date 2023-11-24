'''
Autor: Antonio Uribe Ramirez
lab: 3.2.1.16
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
            raise QueueError("Cola vacía")
        return self.__queue.pop()

    def isempty(self):
        return not bool(self.__queue)

class SuperQueue(Queue):
    pass

que = SuperQueue()
que.put(1)
que.put("perro")
que.put(False)

for _ in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Cola vacía")
