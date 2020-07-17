# Data forwarding nodes
import threading
import time
import random


class Bolt:
    def __init__(self, bolt_id, name, min_temp, max_temp, threshold):
        self.spout_list = []
        self.bolt_id = bolt_id
        self.name = name
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.threshold = threshold
        self.load = []

    def update_load(self):
        self.load = [self.spout_list[i].load for i in range(len(self.spout_list))]

    def filter(self, data):
        if data <= self.max_temp and data >= self.min_temp:
            return data

    def set_spout(self, spout):
        self.spout_list.append(spout)

    def del_spout(self, spout):
        self.spout_list.remove(spout)

    def trigger(self):
        self.update_load()
        if sum(self.load) > self.threshold:
            return True
        return False
            
