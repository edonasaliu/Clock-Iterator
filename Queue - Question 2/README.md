# Queue Implementations and ClockIterator Tests

This document provides an overview of different queue implementations in Python and includes a custom iterator class that mimics a digital clock. Additionally, it covers unit tests for the iterator class.

## 1. Clock Iterator

A `ClockIterator` is a class that simulates a digital clock, iterating over time in a 24-hour format. Below is the Python code for the `ClockIterator` class:

```python
# ClockIterator code snippet here
```

## 2. Queue Types

There are three primary types of queues:

- **Queue (FIFO Queue)**: A regular queue that operates on a First-In-First-Out basis.
- **PriorityQueue**: A queue that processes items based on their priority.
- **LifoQueue (Stack)**: A queue that operates on a Last-In-First-Out basis.

## 3. Queue Template Design

The `Queue` class in Python's standard library is designed as a template, which is then extended by `PriorityQueue` and `LifoQueue` to implement specific behaviors.

## 4. ClockIterator Unit Tests

Unit tests for the `ClockIterator` class are essential to ensure its correct functionality. Below is the Python code for testing the `ClockIterator` using the `unittest` framework:

```python
# ClockIterator Unit Tests code snippet here
```

## 5. Queue Code Snippets

Selected methods from the `Queue`, `PriorityQueue`, and `LifoQueue` classes are shown below. These methods illustrate how the classes manage their respective data structures.

```python
# Queue, PriorityQueue, and LifoQueue code snippets here
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

```

## Conclusion

Understanding these queue types and their implementations is crucial for effective programming, especially when dealing with data structures and algorithms. The `ClockIterator` and its tests serve as practical examples of applying these concepts in Python code.