class Queue:
    def _init(self, maxsize):
        self.queue = []

    def _qsize(self):
        return len(self.queue)

    def _put(self, item):
        self.queue.append(item)

    def _get(self):
        return self.queue.pop(0)

class PriorityQueue(Queue):
    def _put(self, item):
        heapq.heappush(self.queue, item)

    def _get(self):
        return heapq.heappop(self.queue)

class LifoQueue(Queue):
    def _put(self, item):
        self.queue.append(item)

    def _get(self):
        return self.queue.pop()
