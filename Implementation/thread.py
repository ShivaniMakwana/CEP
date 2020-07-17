import threading
import time


class myThread (threading.Thread):
    def __init__(self, threadID, name, spout, bolt, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.spout = spout
        self.bolt = bolt
        self.counter = counter
        self.bolt.set_spout(self.spout)
        self.spout.set_bolt(self.bolt)
        self.exitFlag = 0
        self._stop = threading.Event()

    def stop(self):
        self._stop.set()

    def set_exitFlag(self):
        self.exitFlag = 1

    def set_counter(self):
        self.counter = 0

    def timer(self):
        time.sleep(5)

    def run(self):
        print("Starting " + self.name)
        self.print_time()
        print("Exiting " + self.name)
        self.bolt.del_spout(self.spout.spout_id)

    def print_counter(self):
        return self.counter

    def print_time(self):
        delay = self.spout.WAIT_TIME_SECONDS
        while True:
            if self.exitFlag:
                return
            time.sleep(delay)
            self.counter += 1
            # print(self.bolt.filter(self.spout.generate_Data()), self.name)
