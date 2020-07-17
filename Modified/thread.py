import threading
import time


class myThread (threading.Thread):
    def __init__(self, threadID, name, spout, bolt):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.spout = spout
        self.bolt = bolt
        self.exitFlag = 0

    def set_exitFlag(self):
        self.exitFlag = 1

    def timer(self):
        time.sleep(5)

    def run(self):
        self.bolt.set_spout(self.spout)
        self.spout.set_bolt(self.bolt)
        self.bolt.update_load()
        print("Starting " + self.spout.name + " with " + self.bolt.name + " in " +self.name)
        self.print_time()
        print("Exiting " + self.name)
        self.bolt.del_spout(self.spout)
        self.spout.del_bolt(self.bolt)
        thread4 = self.newThread()
        thread4.start()
        
    def newThread(self):
        return myThread(4, "Thread-4", self.spout, self.spout.bolt_list[0])

    def get_spout(self):
        lst = self.bolt.load
        my_dict = {i: lst[i] for i in range(len(lst))}
        key_max = min(my_dict.keys(), key=(lambda k: my_dict[k]))
        if self.spout.spout_id == self.bolt.spout_list[key_max].spout_id:
            self.set_exitFlag()

    def print_time(self):
        delay = self.spout.WAIT_TIME_SECONDS
        while True:
            if self.bolt.trigger():
                self.get_spout()
            if self.exitFlag:
                return
            time.sleep(delay)
            print(self.bolt.filter(self.spout.generate_Data()), self.name)
            print(self.bolt.load)
