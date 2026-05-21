from threading import Lock

class Foo:
    def __init__(self):
        self.l1 = Lock()
        self.l2 = Lock()
        self.l1.acquire()
        self.l2.acquire()

    def first(self, printFirst):
        printFirst()
        self.l1.release()

    def second(self, printSecond):
        self.l1.acquire()
        printSecond()
        self.l2.release()

    def third(self, printThird):
        self.l2.acquire()
        printThird()

