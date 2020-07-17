import numpy as np
import time
from thread import myThread


class Cordinator:
    def __init__(self, threads, threshold):
        self.threads = threads
        self.load = [0 for x in range(len(threads))]
        self.last_count = [0 for x in range(len(threads))]
        self.current_count = [0 for x in range(len(threads))]
        self.bolt_id = [0 for x in range(len(threads))]

    def current_load(self, threads):
        l = []
        for i in threads:
            l.append(i.print_counter())
        return l

    def Convert(self, lst):
        res_dct = {lst[i]: 0 for i in range(len(lst))}
        return res_dct

    def get_bolts(self, threads):
        l = []
        for i in threads:
            l.append(i.bolt.bolt_id)
        dictionary, bolts_list = self.Convert(l), l
        return dictionary, bolts_list

    def cal_load_per_bolt(self, threads):
        dictionary, bolts_list = self.get_bolts(threads)
        for i in range(len(bolts_list)):
            dictionary[bolts_list[i]] += self.load[i]
        return dictionary

    def newThread(self, threads, spout, bolt):
        thread4 = myThread(4, "Thread-4", spout, bolt, 0)
        threads.append(thread4)
        thread4.start()

    def transfer_load(self, threads):
        my_dict = self.cal_load_per_bolt(threads)
        key_max = 0
        if bool(my_dict):
            key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
        # key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))
        if my_dict[key_max] > 25:
            threads[0].set_exitFlag()
            threads[1].set_counter()
            threads[2].set_counter()
            self.newThread(threads, threads[0].spout, threads[2].bolt)
            del(threads[0])
            self.__init__(threads, 25)

    def calculate_load(self, threads):
        delay = 2
        while True:
            time.sleep(delay)
            self.last_count = self.current_count
            self.current_count = np.array(self.current_load(threads))
            self.load = self.current_count - self.last_count
            print(self.cal_load_per_bolt(threads))
            self.transfer_load(threads)

    def get_load(self):
        return self.load
