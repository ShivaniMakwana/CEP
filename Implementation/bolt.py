# Data forwarding nodes
import threading
import time
import random


class Bolt:
    def __init__(self, bolt_id, name, min_temp, max_temp):
        self.spout_id = []
        self.bolt_id = bolt_id
        self.name = name
        self.min_temp = min_temp
        self.max_temp = max_temp

    def filter(self, data):
        if data <= self.max_temp and data >= self.min_temp:
            return data

    def set_spout(self, spout):
        self.spout_id.append(spout.spout_id)

    def del_spout(self, spout_id):
        self.spout_id.remove(spout_id)
