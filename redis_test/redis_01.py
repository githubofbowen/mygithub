import time
import random
from queue import Queue
from threading import Thread


class Producer(Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            a = random.randint(0, 10)
            b = random.randint(80, 100)
            print('生产者{0}， {1}'.format(a, b))
            self.queue.put((a, b))
            time.sleep(2)


class Consumer(Thread):

    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            num_tuple = self.queue.get(block=True)
            sum_a_b = sum(num_tuple)
            print('消费者购买了多少个数字{0}+{1}={2}'.format(num_tuple[0], num_tuple[1], sum_a_b))
            time.sleep(random.randint(0, 10))


queue = Queue()
producer = Producer(queue)
consumer = Consumer(queue)

producer.start()
consumer.start()
while True:
    time.sleep(1)